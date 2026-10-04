"""Base documentaire Markdown du standard B Lab V2.2 (tools/build_standard_md.py).

Le générateur est lancé une fois par session vers un dossier temporaire ; les tests
lisent ces fichiers, puis vérifient que le dossier commité (resources/standards-v2.2)
est identique à une génération fraîche.
"""
import csv
import filecmp
import re
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "resources" / "standards-v2.2" / "bcorp_v2.2_requirements.csv"
COMMITTED = ROOT / "resources" / "standards-v2.2"
PDF = COMMITTED / "_source" / "B-Lab-Standards-V2.2_Body-of-Knowledge_EN_2026-02-20.pdf"
ORDER = ["FR", "PSG", "FW", "JEDI", "HR", "CA", "ESC", "GACA"]

pytestmark = pytest.mark.skipif(not PDF.exists(), reason="PDF source B Lab absent")


@pytest.fixture(scope="session")
def rows():
    with open(CSV_PATH, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


@pytest.fixture(scope="session")
def out_dir(tmp_path_factory):
    out = tmp_path_factory.mktemp("standards-v2.2")
    subprocess.run(
        [sys.executable, str(ROOT / "tools" / "build_standard_md.py"), "--pdf", str(PDF), "--out", str(out)],
        check=True, capture_output=True, text=True,
    )
    return out


def area_dirs(out):
    return sorted(p for p in out.iterdir() if p.is_dir() and not p.name.startswith("_"))


def block_files(out):
    return sorted(p for d in area_dirs(out) for p in d.glob("*.md") if p.name != "_index.md")


def split_md(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    assert m, f"frontmatter absent : {path}"
    return yaml.safe_load(m.group(1)), m.group(2)


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


# Coquille du PDF reprise par le CSV : FW1.1.3 imprimé « 1.2.3 »
ID_FIXES = {("FW1.1", "1.2.3"): "1.1.3"}


def ids(row):
    raw = dict.fromkeys(c.strip() for c in row["criteres_conformite_ids"].split(",") if c.strip())
    return [ID_FIXES.get((row["code"], c), c) for c in raw]


@pytest.fixture(scope="session")
def criteres_csv(out_dir):
    with open(out_dir / "criteres_en.csv", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def test_area_folders_in_order(out_dir):
    names = [d.name for d in area_dirs(out_dir)]
    assert [n.split("-")[1] for n in names] == ORDER
    assert names[0] == "0-FR-exigences-de-base"
    assert names[1] == "1-PSG-mission-et-gouvernance-des-parties-prenantes"
    for i, n in enumerate(names):
        assert n.startswith(f"{i}-{ORDER[i]}-")


def test_one_md_per_csv_code_in_right_folder(out_dir, rows):
    folders = {d.name.split("-")[1]: d for d in area_dirs(out_dir)}
    for r in rows:
        assert (folders[r["impact_topic_code"]] / f"{r['code']}.md").is_file(), r["code"]


def test_no_md_outside_csv(out_dir, rows):
    codes = {r["code"] for r in rows}
    found = {p.stem for p in block_files(out_dir)}
    assert found == codes


def test_frontmatter_consistent_with_csv(out_dir, rows):
    by_code = {p.stem: p for p in block_files(out_dir)}
    for r in rows:
        fm, body = split_md(by_code[r["code"]])
        assert fm["code"] == r["code"]
        assert fm["impact_area"] == r["impact_topic_code"]
        assert fm["requirement_code"] == r["requirement_code"]
        assert fm["type"] == r["type_ligne"]
        assert fm["year"] == int(r["echeance"].replace("Year", ""))
        assert fm["criteria"] == ids(r)
        start, end = map(int, fm["pages"].split("-"))
        assert start == int(r["page_pdf"]) and start <= end <= int(r["page_pdf_fin_bloc"])
        assert fm["source"] == "B Lab Standards V2.2, 20/02/2026"
        assert fm["genere_par"].startswith("tools/build_standard_md.py")
        assert re.fullmatch(r"[A-Z]+ \S+", fm["code_fr"])
        expected = [t.split(" | ") for t in r["track_factors_brut"].split(" || ") if t]
        expected = [{"taille": a, "secteur": b, "industrie": c} for a, b, c in expected if b != "None"]
        assert fm["applicabilite"] == expected
        assert body.lstrip().startswith(f"# {r['code']} ({fm['code_fr']}) : ")
        assert "## Compliance criteria" in body and "## Applicabilité" in body


def test_psg11_code_fr(out_dir):
    fm, _ = split_md(out_dir / "1-PSG-mission-et-gouvernance-des-parties-prenantes" / "PSG1.1.md")
    assert fm["code_fr"] == "MGPP 1.1"


def criterion_texts(body):
    """{id: texte} lu sous '## Compliance criteria' (sous-titres '### <id>')."""
    sec = re.search(r"^## Compliance criteria\n(.*?)(?=^## |\Z)", body, re.S | re.M).group(1)
    parts = re.split(r"^### (\S+)\n", sec, flags=re.M)
    return {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}


def test_every_criterion_has_text_in_md(out_dir, rows):
    by_code = {p.stem: p for p in block_files(out_dir)}
    missing = []
    for r in rows:
        _, body = split_md(by_code[r["code"]])
        texts = criterion_texts(body)
        for c in ids(r):
            if not texts.get(c):
                missing.append(f"{r['code']}:{c}")
    assert not missing, missing


def test_every_criterion_in_criteres_csv(criteres_csv, rows):
    got = {(x["code"], x["critere_id"]): x for x in criteres_csv}
    expected = [(r["code"], c) for r in rows for c in ids(r)]
    assert len(criteres_csv) == len(expected)
    for k in expected:
        assert k in got, k
        assert got[k]["texte_en"].strip(), k
        assert got[k]["page"].isdigit(), k


DEADLINES = [
    ("ESC1.1", "1.1.7", "Year 5"),
    ("ESC1.2", "1.2.4", "Year 5"),
    ("ESC1.3", "1.3.5", "Year 5"),
    ("ESC1.4", "1.4.3", "Year 5"),
    ("ESC1.4", "1.4.2", "Before Year 0"),
    ("ESC1.4", "1.4.1", "Year 0"),  # sans marquage : année de la sous-exigence
]


@pytest.mark.parametrize("code,cid,expected", DEADLINES)
def test_criterion_deadline(out_dir, criteres_csv, code, cid, expected):
    row = next(x for x in criteres_csv if x["code"] == code and x["critere_id"] == cid)
    assert row["echeance_critere"] == expected
    _, body = split_md(out_dir / "6-ESC-gestion-environnementale-et-circularite" / f"{code}.md")
    assert criterion_texts(body)[cid].startswith(f"*Échéance du critère : {expected}")


def test_deadline_values_and_default(criteres_csv, rows):
    years = {r["code"]: r["echeance"].replace("Year", "Year ") for r in rows}
    for x in criteres_csv:
        assert x["echeance_critere"] in {"Before Year 0", "Year 0", "Year 3", "Year 5"}
        if not re.match(r"(For|Before|By) Year", x["texte_en"]):
            assert x["echeance_critere"] == years[x["code"]], (x["code"], x["critere_id"])


def test_fw11_typo_corrected(out_dir, criteres_csv):
    fm, body = split_md(out_dir / "2-FW-travail-equitable" / "FW1.1.md")
    assert fm["criteria"] == ["1.1.1", "1.1.2", "1.1.3"]
    texts = criterion_texts(body)
    assert "All employees receive a copy of their employment contract or offer letter from the company." in texts["1.1.3"]
    assert "Anomalie du PDF" in texts["1.1.3"] and "« 1.2.3 »" in texts["1.1.3"]
    assert ("FW1.1", "1.1.3") in {(x["code"], x["critere_id"]) for x in criteres_csv}


def test_no_footer_in_md(out_dir):
    for p in out_dir.rglob("*.md"):
        t = p.read_text(encoding="utf-8")
        assert "©B Lab Company" not in t, p
        assert "B Lab Standards V2.2 ©" not in t, p


VERBATIM = [
    ("1-PSG-mission-et-gouvernance-des-parties-prenantes/PSG1.1.md", "1.1.1",
     "sets out the specific positive and meaningful impact the company intends to make on society or the environment, or both"),
    ("3-JEDI-justice-equite-diversite-inclusion/JEDI2.a.md", "2.a.2",
     "The company assigns accountability for the JEDI commitment to the executive team or highest governing body."),
    ("0-FR-exigences-de-base/FR3.1.a.md", "3.1.a.5",
     "[XX Large companies in all sectors] If Yes, the company considers the potential impact (see Intent) in their "
     "Human Rights Saliency Assessment (HR2.1)."),
]


@pytest.mark.parametrize("rel,cid,fragment", VERBATIM)
def test_verbatim_fragments(out_dir, criteres_csv, rel, cid, fragment):
    _, body = split_md(out_dir / rel)
    assert fragment in norm(criterion_texts(body)[cid])
    code = Path(rel).stem
    row = next(x for x in criteres_csv if x["code"] == code and x["critere_id"] == cid)
    assert fragment in norm(row["texte_en"])


def test_psg11_sections(out_dir):
    _, body = split_md(out_dir / "1-PSG-mission-et-gouvernance-des-parties-prenantes" / "PSG1.1.md")
    for h in ("## Requirement", "## Intent", "## Clarifying the compliance criteria", "## Applying the criteria",
              "## Exemples de preuves (KB B Lab, résumé automatique à relire)"):
        assert h in body, h
    assert "d) is approved by the company’s highest governing body." in body
    assert "Further Guidance" not in body  # on s'arrête aux sections demandées
    assert "aligns with the purpose clause of the B Corp legal requirement" in norm(body)


def test_indexes(out_dir, rows):
    root = (out_dir / "_index.md").read_text(encoding="utf-8")
    for r in rows:
        assert f"{r['code']}.md" in root, r["code"]
    for d in area_dirs(out_dir):
        idx = (d / "_index.md").read_text(encoding="utf-8")
        for p in d.glob("*.md"):
            if p.name != "_index.md":
                assert f"]({p.name})" in idx


INPUT_FILES = {"bcorp_v2.2_requirements.csv", "criteres_fr.csv"}  # entrées, pas des sorties du générateur


def test_committed_folder_is_up_to_date(out_dir):
    fresh = sorted(p.relative_to(out_dir) for p in out_dir.rglob("*") if p.is_file())
    committed = sorted(p.relative_to(COMMITTED) for p in COMMITTED.rglob("*")
                       if p.is_file() and "_source" not in p.parts
                       and p.name not in INPUT_FILES)
    assert fresh == committed, "relancer : python3 tools/build_standard_md.py"
    stale = [str(p) for p in fresh if not filecmp.cmp(out_dir / p, COMMITTED / p, shallow=False)]
    assert not stale, f"fichiers périmés (relancer le générateur) : {stale[:5]}"


def test_french_translation_is_shown_and_flagged():
    md = next(COMMITTED.rglob("PSG1.1.md")).read_text(encoding="utf-8")
    assert "Traduction FR (à relire, compilation tierce)" in md
