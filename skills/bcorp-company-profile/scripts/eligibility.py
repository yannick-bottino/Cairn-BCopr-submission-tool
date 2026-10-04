#!/usr/bin/env python3
"""Caractérisation et éligibilité B Corp (exigences de base FR1, FR2, FR3 de la V2.2).

Usage :
    python3 eligibility.py <reponses.json> <dossier_sortie>

reponses.json : profil relevé sur la plateforme (client, source_profil, taille, secteur, industrie,
horizon…) + une réponse par question de references/questions.json (clé = id de la question).
Sorties (jamais écrasées) : profil.json, lu tel quel par le module 3, et fiche_caracterisation.md.

Le script ne calcule ni la taille ni le secteur : il vérifie seulement qu'ils viennent de la plateforme.
"""
from __future__ import annotations

import json
import sys
from dataclasses import dataclass, field
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "bcorp-gap-analysis" / "scripts"))
import build_gap_excel as bg  # noqa: E402

ref = bg.ref
QUESTIONS = HERE.parent / "references" / "questions.json"
ELIGIBLE, BLOCKING, TO_CONFIRM, TO_DO, NA = "Éligible", "Bloquant", "À confirmer", "À faire", "Non applicable"
PROFILE_KEYS = ["client", "source_profil", "taille", "secteur", "industrie", "horizon", "mecanisme_equite",
                "date_depot", "co_prestataire", "options_retenues"]


@dataclass
class Check:
    code: str
    status: str
    reason: str


@dataclass
class Result:
    checks: list[Check] = field(default_factory=list)
    risk_yes: list[str] = field(default_factory=list)

    @property
    def by_code(self) -> dict[str, Check]:
        return {c.code: c for c in self.checks}

    @property
    def verdict(self) -> str:
        statuses = {c.status for c in self.checks}
        if BLOCKING in statuses:
            return "Non éligible en l'état"
        if TO_CONFIRM in statuses:
            return "Éligibilité à confirmer"
        return "Éligible sous réserve"


def load_questions() -> list[dict]:
    return json.loads(QUESTIONS.read_text(encoding="utf-8"))["questions"]


def _yes(value) -> bool | None:
    if isinstance(value, bool):
        return value
    v = str(value).strip().lower() if value is not None else ""
    return {"oui": True, "non": False}.get(v)


def _pct(value) -> float | None:
    if value is None or str(value).strip() == "":
        return None
    try:
        return float(str(value).replace(",", ".").replace("%", ""))
    except ValueError:
        return None


def _validate_profile(a: dict) -> None:
    if a.get("source_profil") not in bg.PROFILE_SOURCES:
        raise ValueError(f"source_profil obligatoire, parmi {bg.PROFILE_SOURCES}")
    if a.get("taille") not in ref.SIZES:
        raise ValueError(f"taille inconnue : {a.get('taille')!r} ; relever la taille affichée par la plateforme")
    if a.get("secteur") not in ref.SECTORS:
        raise ValueError(f"secteur inconnu : {a.get('secteur')!r} ; relever le secteur affiché par la plateforme")


def evaluate(a: dict) -> Result:
    _validate_profile(a)
    res = Result()

    # FR1.1 : qualification de l'entité
    entity = [_yes(a.get(k)) for k in ("FR1.1.1.a", "FR1.1.1.b", "FR1.1.1.c")]
    excluded = _yes(a.get("FR1.1.2"))
    if False in entity:
        res.checks.append(Check("FR1.1", BLOCKING, "1.1.1 : société immatriculée, 12 mois d'activité et CA majoritairement concurrentiel exigés."))
    elif excluded:
        res.checks.append(Check("FR1.1", BLOCKING, "1.1.2 : catégorie exclue (associations et entités publiques : seulement avec approbation de B Lab)."))
    elif None in entity or excluded is None:
        res.checks.append(Check("FR1.1", TO_CONFIRM, "Réponse manquante sur 1.1.1 ou 1.1.2."))
    else:
        res.checks.append(Check("FR1.1", ELIGIBLE, "1.1.1 et 1.1.2 satisfaits d'après les réponses."))

    # FR1.2 : industries incompatibles
    shares = {k: _pct(a.get(k)) for k in ("FR1.2.1", "FR1.2.2", "FR1.2.3")}
    utility = a.get("FR1.2.4")
    utility_pct = None if str(utility).strip().lower() in ("non applicable", "na", "") else _pct(utility)
    over = [k for k, v in shares.items() if v is not None and v >= 1]
    if utility_pct is not None and utility_pct >= 50:
        over.append("FR1.2.4")
    if over:
        if _yes(a.get("FR1.2.5")):
            res.checks.append(Check("FR1.2", TO_DO, f"Seuil dépassé ({', '.join(over)}), mais recertification V1.6 : FR1.2 exigible en Year 3 (1.2.5)."))
        else:
            res.checks.append(Check("FR1.2", BLOCKING, f"Seuil dépassé : {', '.join(over)} (1 % du CA ; 50 % du mix pour un producteur d'énergie)."))
    elif None in shares.values():
        res.checks.append(Check("FR1.2", TO_CONFIRM, "Part de CA manquante sur 1.2.1, 1.2.2 ou 1.2.3."))
    else:
        res.checks.append(Check("FR1.2", ELIGIBLE, "Moins de 1 % du CA dans les industries listées."))

    # FR1.5 : transparence
    sub = _yes(a.get("FR1.5.3"))
    if sub:
        res.checks.append(Check("FR1.5", TO_DO, "1.5.3 : filiale ou grande société cotée : rapport BIA entièrement public, actionnaires majoritaires identifiés."))
    elif sub is None:
        res.checks.append(Check("FR1.5", TO_CONFIRM, "Réponse manquante sur 1.5.3."))
    else:
        res.checks.append(Check("FR1.5", ELIGIBLE, "Profil public standard."))

    # FR2.1 : exigence légale
    legal = _yes(a.get("FR2.1"))
    if legal is False:
        res.checks.append(Check("FR2.1", TO_DO, "2.1.1 : modifier les statuts (ou la forme juridique) pour intégrer la gouvernance des parties prenantes."))
    elif legal is None:
        res.checks.append(Check("FR2.1", TO_CONFIRM, "Réponse manquante sur 2.1.1."))
    else:
        res.checks.append(Check("FR2.1", ELIGIBLE, "Statuts déjà conformes d'après les réponses (à vérifier sur pièce)."))

    # FR3.1 : Risk Tool (exempté pour Micro et Company without workers, PDF p.53)
    if a["taille"] in ("Micro", "Company without workers"):
        res.checks.append(Check("FR3.1", NA, "Risk Tool non applicable à cette taille."))
    else:
        risk = {f"FR3.1.{c}": _yes(a.get(f"FR3.1.{c}")) for c in "abcdefghijklmn"}
        res.risk_yes = [k for k, v in risk.items() if v]
        missing = [k for k, v in risk.items() if v is None]
        if missing:
            res.checks.append(Check("FR3.1", TO_CONFIRM, f"Questions du Risk Tool sans réponse : {', '.join(missing)}."))
        elif res.risk_yes:
            res.checks.append(Check("FR3.1", TO_DO, f"Réponses « oui » : {', '.join(res.risk_yes)} ; sous-exigences additionnelles à intégrer."))
        else:
            res.checks.append(Check("FR3.1", ELIGIBLE, "Aucune réponse « oui » au Risk Tool."))
    return res


def _standard_file(code: str) -> str:
    root = ref.STD_DIR
    hit = next(root.glob(f"*/{code}.md"), None)
    return str(hit.relative_to(root.parents[1])) if hit else ""


def run(src: Path, out_dir: Path) -> tuple[Path, Path]:
    a = json.loads(Path(src).read_text(encoding="utf-8"))
    out_dir = Path(out_dir)
    profil, fiche = out_dir / "profil.json", out_dir / "fiche_caracterisation.md"
    for p in (profil, fiche):
        if p.exists():
            raise FileExistsError(f"{p} existe déjà : le script n'écrase jamais un fichier.")
    res = evaluate(a)
    data = {k: a[k] for k in PROFILE_KEYS if k in a}
    data["reponses"] = {q["id"]: a.get(q["id"]) for q in load_questions()}
    data["risk_tool_oui"] = res.risk_yes
    data["eligibilite"] = {"verdict": res.verdict, "controles": [vars(c) for c in res.checks]}
    out_dir.mkdir(parents=True, exist_ok=True)
    profil.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [f"# Fiche de caractérisation B Corp : {a['client']}", "",
             f"Source du profil : {a['source_profil']}. Taille : {a['taille']}. Secteur : {a['secteur']}."
             + (f" Industrie : {a['industrie']}." if a.get("industrie") else ""), "",
             f"**Verdict : {res.verdict}**", "",
             "| Exigence | Statut | Motif |", "|---|---|---|"]
    lines += [f"| {c.code} | {c.status} | {c.reason} |" for c in res.checks]
    if res.risk_yes:
        lines += ["", "## Risk Tool : sous-exigences additionnelles à lire", ""]
        lines += [f"- {code} : `{_standard_file(code)}`" for code in res.risk_yes]
    lines += ["", "Référentiel : B Lab Standards V2.2 (20/02/2026). Les réponses restent à vérifier sur pièce lors du diagnostic."]
    fiche.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return profil, fiche


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    for p in run(Path(sys.argv[1]), Path(sys.argv[2])):
        print(p)
