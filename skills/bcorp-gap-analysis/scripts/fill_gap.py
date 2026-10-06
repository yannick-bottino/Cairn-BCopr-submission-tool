#!/usr/bin/env python3
"""Écrit les propositions de Claude dans un gap analysis B Corp, sans jamais écraser la saisie humaine.

Usage :
    python3 fill_gap.py <gap.xlsx> <propositions.json> <sortie.xlsx>

propositions.json : [{"req_id": "PSG1.1-1.1.1", "champs": {"Diagnostic & gap analysis": "...", ...}}, ...]

Règles :
- le fichier source n'est jamais modifié, la sortie ne doit pas exister ;
- seules les colonnes rédactionnelles sont modifiables, et seulement si la cellule est vide ;
- les valeurs des listes déroulantes sont vérifiées ;
- tout code d'exigence cité dans un texte doit exister dans le référentiel V2.2 ;
- chaque cellule écrite est surlignée et tracée dans l'onglet « Propositions » au statut « À valider ».
"""
from __future__ import annotations

import datetime as dt
import json
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path

import openpyxl
from openpyxl.styles import PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_gap_excel as bg  # noqa: E402

ref = bg.ref
GAP_SHEET = "3. Gap analysis"
LOG_SHEET = "Propositions"
PROPOSAL_COLOR = "FFF59D"
COMMENT = "Commentaire soumission dossier pour l'auditeur"
WRITABLE = {
    "Niveau de conformité", "Diagnostic & gap analysis", "Actions recommandées",
    "Priorité B Corp (Anchor)", "Preuves (& intitulés associés)", COMMENT,
    "Typologie du gap (Anchor)", "Criticité (Anchor)", "Justification de la typologie (Anchor)",
}
PREFIXES = "EB|MGPP|TE|JEDI|DH|AC|GEC|APAC|FR|PSG|FW|HR|CA|ESC|GACA"
# Code cité : préfixe + numéro contenant au moins un point (PSG1.1, APAC 1.1.1, JEDI 2.g, GACA2.3c, JEDI2.a.1)
CODE_RE = re.compile(rf"\b({PREFIXES}) ?(\d+(?:\.\d+)*(?:\.?[a-z]+)?(?:\.\d+)*)\b")
DATE_RE = re.compile(r"\d{1,2}/\d{1,2}|\b20\d{2}\b|\bT[1-4]\b|Year \d|janvier|février|mars|avril|mai|juin|"
                     r"juillet|août|septembre|octobre|novembre|décembre", re.I)


@dataclass
class Report:
    written: int = 0
    skipped: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def check_codes(text: str, r: ref.Referentiel) -> None:
    for m in CODE_RE.finditer(text):
        if "." not in m.group(2):
            continue                          # « CA 2024 », « FR 2 sites » : pas un code
        raw = f"{m.group(1)}{m.group(2)}"
        try:
            r.to_site(raw)
            continue
        except ref.UnknownCode:
            pass
        head, _, _ = m.group(2).rpartition(".")
        try:
            req = r.get(f"{m.group(1)}{head}")
            if m.group(2) in req.criteria_ids:
                continue
        except ref.UnknownCode:
            pass
        raise ValueError(f"Code inconnu du référentiel V2.2 dans le texte : {m.group(0)}")


def check_style(column: str, text: str, warnings: list[str], req_id: str) -> None:
    if "—" in text:
        raise ValueError(f"{req_id} / {column} : tiret cadratin interdit")
    if "**" in text or "- [ ]" in text or re.search(r"(?m)^#", text):
        raise ValueError(f"{req_id} / {column} : Markdown interdit dans l'Excel")
    if column == COMMENT:
        if re.search(r"Manquant|Question à poser", text):
            raise ValueError(f"{req_id} : le commentaire auditeur ne mentionne jamais un manque ni une question")
        if re.search(r"en cours", text, re.I) and not DATE_RE.search(text):
            warnings.append(f"{req_id} : « en cours » sans jalon daté ; ajouter le jalon et le porteur (fonction)")


def fill(src: Path, proposals: list[dict], out: Path) -> Report:
    src, out = Path(src), Path(out)
    if out.exists():
        raise FileExistsError(f"{out} existe déjà : le script n'écrase jamais un fichier.")
    r = ref.Referentiel.load()
    wb = openpyxl.load_workbook(src)
    ws = wb[GAP_SHEET]
    headers = [c.value for c in ws[1]]
    col = {h: i + 1 for i, h in enumerate(headers)}
    rows = {ws.cell(i, col["req_id"]).value: i for i in range(2, ws.max_row + 1)}

    report, writes = Report(), []
    for p in proposals:                       # 1. tout valider avant d'écrire quoi que ce soit
        rid = p["req_id"]
        if rid not in rows:
            raise KeyError(f"req_id absent de l'Excel : {rid}")
        for column, value in p["champs"].items():
            if column not in WRITABLE:
                raise ValueError(f"Colonne non modifiable par Claude : {column}")
            value = str(value).strip()
            if column in bg.LISTS and value not in bg.LISTS[column]:
                raise ValueError(f"{rid} / {column} : valeur « {value} » hors liste {bg.LISTS[column]}")
            check_codes(value, r)
            check_style(column, value, report.warnings, rid)
            cell = ws.cell(rows[rid], col[column])
            if cell.value not in (None, ""):
                report.skipped.append(f"{rid} / {column} : cellule déjà remplie, non modifiée")
                continue
            writes.append((rid, column, value, cell))

    fill_ = PatternFill("solid", fgColor=PROPOSAL_COLOR)
    log = _log_sheet(wb)
    today = dt.date.today().isoformat()
    for rid, column, value, cell in writes:   # 2. écrire et tracer
        cell.value = value
        cell.fill = fill_
        log.append([rid, ws.cell(rows[rid], col["Code plateforme"]).value, column, "À valider", today, value])
        report.written += 1

    shutil.copyfile(src, out)                 # garde les propriétés du classeur, puis réécrit le contenu
    wb.save(out)
    return report


def _log_sheet(wb):
    if LOG_SHEET in wb.sheetnames:
        return wb[LOG_SHEET]
    ws = wb.create_sheet(LOG_SHEET)
    bg._header(ws, ["req_id", "Code plateforme", "Colonne", "Statut", "Date", "Texte proposé"],
               {"Colonne": 30, "Texte proposé": 90})
    dv = DataValidation(type="list", formula1='"À valider,Validé,Rejeté"', allow_blank=False)
    dv.add("D2:D5000")
    ws.add_data_validation(dv)
    return ws


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    proposals = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    rep = fill(Path(argv[0]), proposals, Path(argv[2]))
    print(f"{rep.written} cellule(s) écrite(s), {len(rep.skipped)} ignorée(s).")
    for line in rep.skipped + rep.warnings:
        print(f"- {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
