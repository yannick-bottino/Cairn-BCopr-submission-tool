import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills" / "bcorp-company-profile" / "scripts"))
sys.path.insert(0, str(ROOT / "skills" / "bcorp-gap-analysis" / "scripts"))

import bcorp_ref as ref  # noqa: E402
import eligibility as el  # noqa: E402
import build_gap_excel as bg  # noqa: E402

RISK = {f"FR3.1.{c}": "non" for c in "abcdefghijklmn"}


def answers(**over):
    a = {
        "client": "ClientTest", "source_profil": "Export PDF plateforme B Lab",
        "taille": "Medium", "secteur": "Wholesale/Retail", "industrie": "",
        "horizon": 3, "co_prestataire": "", "options_retenues": [], "date_depot": "Avril 2027",
        "FR1.1.1.a": "oui", "FR1.1.1.b": "oui", "FR1.1.1.c": "oui",
        "FR1.1.2": "non",
        "FR1.2.1": 0, "FR1.2.2": 0, "FR1.2.3": 0, "FR1.2.4": "non applicable",
        "FR1.2.5": "non",
        "FR1.5.3": "non",
        "FR2.1": "non",
        **RISK,
    }
    a.update(over)
    return a


def test_questions_cite_only_real_codes():
    r = ref.Referentiel.load()
    for q in el.load_questions():
        assert r.get(q["code"]), q["id"]
        assert q["question"] and q["type"] in {"oui/non", "pourcentage", "choix"}


def test_risk_tool_questions_cover_all_14():
    ids = {q["id"] for q in el.load_questions() if q["code"].startswith("FR3.1.")}
    assert ids == set(RISK)


def test_eligible_company():
    res = el.evaluate(answers())
    assert res.verdict == "Éligible sous réserve"
    assert res.by_code["FR2.1"].status == "À faire"         # statuts à modifier : action, pas blocage
    assert not [c for c in res.checks if c.status == "Bloquant"]


@pytest.mark.parametrize("over, code", [
    ({"FR1.1.1.b": "non"}, "FR1.1"),
    ({"FR1.1.2": "oui"}, "FR1.1"),
    ({"FR1.2.1": 1.0}, "FR1.2"),
    ({"FR1.2.2": 3}, "FR1.2"),
    ({"FR1.2.4": 55}, "FR1.2"),
])
def test_blocking_rules(over, code):
    res = el.evaluate(answers(**over))
    assert res.verdict == "Non éligible en l'état"
    assert res.by_code[code].status == "Bloquant"


def test_below_one_percent_is_ok():
    assert el.evaluate(answers(**{"FR1.2.1": 0.9})).by_code["FR1.2"].status == "Éligible"


def test_v16_recertification_defers_fr12():
    res = el.evaluate(answers(**{"FR1.2.1": 2, "FR1.2.5": "oui"}))
    assert res.by_code["FR1.2"].status == "À faire"
    assert "Year 3" in res.by_code["FR1.2"].reason


def test_unanswered_question_is_to_confirm():
    a = answers()
    del a["FR1.1.1.c"]
    assert el.evaluate(a).by_code["FR1.1"].status == "À confirmer"


def test_risk_tool_yes_lists_additional_requirements():
    res = el.evaluate(answers(**{"FR3.1.c": "oui", "FR3.1.n": "oui"}))
    assert res.by_code["FR3.1"].status == "À faire"
    assert res.risk_yes == ["FR3.1.c", "FR3.1.n"]


def test_risk_tool_not_applicable_to_micro():
    res = el.evaluate(answers(taille="Micro"))
    assert res.by_code["FR3.1"].status == "Non applicable"


def test_subsidiary_must_publish_full_report():
    res = el.evaluate(answers(**{"FR1.5.3": "oui"}))
    assert res.by_code["FR1.5"].status == "À faire"


def test_profile_source_required():
    with pytest.raises(ValueError, match="source_profil"):
        el.evaluate(answers(source_profil="calcul"))
    with pytest.raises(ValueError):
        el.evaluate(answers(taille="Moyenne"))


def test_outputs_feed_gap_generator(tmp_path):
    src = tmp_path / "reponses.json"
    src.write_text(json.dumps(answers(**{"FR3.1.c": "oui"}), ensure_ascii=False), encoding="utf-8")
    profil, fiche = el.run(src, tmp_path)
    data = json.loads(profil.read_text(encoding="utf-8"))
    assert data["risk_tool_oui"] == ["FR3.1.c"]
    assert data["eligibilite"]["verdict"] == "Éligible sous réserve"
    assert bg.build(data, tmp_path / "gap.xlsx").exists()
    text = fiche.read_text(encoding="utf-8")
    assert "FR3.1.c" in text and "resources/standards-v2.2/0-FR-exigences-de-base/FR3.1.c.md" in text
    with pytest.raises(FileExistsError):
        el.run(src, tmp_path)
