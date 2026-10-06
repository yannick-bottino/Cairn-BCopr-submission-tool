#!/usr/bin/env python3
"""Plan de preuves B Corp : rapproche les preuves attendues du gap analysis des fichiers du client.

Usage :
    python3 evidence_plan.py <gap.xlsx> <dossier_preuves_client> <plan.xlsx> [commentaires.json]

- Lit la colonne « Preuves (& intitulés associés) » de l'onglet « 3. Gap analysis ».
- Parcourt le dossier du client en lecture seule et propose, pour chaque preuve attendue,
  le fichier le plus proche (Trouvé / Ambigu / Manquant) et un chemin de rangement normalisé.
- commentaires.json (optionnel) : [{"req_id": ..., "preuve": ..., "commentaire": ...}] ; les
  commentaires de preuve sont contrôlés comme le commentaire auditeur (codes, style, aucun manque).
- Toute ligne est au statut « À valider » : rien n'est copié avant validation (apply_reorg.py).
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "bcorp-gap-analysis" / "scripts"))
import build_gap_excel as bg  # noqa: E402
import fill_gap as fg  # noqa: E402

ref = bg.ref
PLAN_SHEET = "Plan de preuves"
ORPHANS_SHEET = "Fichiers non rattachés"
PREUVES = "Preuves (& intitulés associés)"
HEADERS = ["req_id", "Code exigence", "Code plateforme", "Critère", "Preuve attendue", "Statut",
           "Fichier source", "Score", "Autres candidats", "Chemin proposé", "Commentaire de preuve", "Décision"]
FOUND, AMBIGUOUS, MISSING = "Trouvé", "Ambigu", "Manquant"
THRESHOLD, MARGIN = 0.5, 0.15
STOPWORDS = {"de", "du", "des", "la", "le", "les", "l", "d", "et", "en", "au", "aux", "a", "un", "une",
             "pour", "par", "sur", "avec", "dans", "ou", "the", "of", "and", "vdef", "final", "def", "copie"}
IGNORED = {".DS_Store", "Thumbs.db", "desktop.ini"}


def parse_items(cell: str | None) -> list[str]:
    """Une preuve par ligne « - » ou « > » ; sinon la cellule entière. Les en-têtes sont ignorés."""
    if not cell or not str(cell).strip():
        return []
    lines = [ln.strip() for ln in str(cell).splitlines() if ln.strip()]
    bullets = [re.sub(r"^[-–>•]\s*", "", ln) for ln in lines if re.match(r"^[-–>•]", ln)]
    return bullets or [ln for ln in lines if not ln.endswith(":")]


def tokens(text: str) -> set[str]:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    words = re.findall(r"[a-z]+|\d+", text)
    return {w for w in words if w not in STOPWORDS and not re.fullmatch(r"v\d*", w)}


def score(item: str, path: Path) -> float:
    a, b = tokens(item), tokens(path.stem)
    if not a or not b:
        return 0.0
    common = len(a & b)
    return max(common / len(a), common / len(b))


def list_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*")
                  if p.is_file() and p.name not in IGNORED and not any(part.startswith(".") for part in p.relative_to(root).parts))


def slug(text: str, limit: int = 50) -> str:
    text = re.sub(r'[<>:"/\\|?*\n]', " ", text).strip()
    return re.sub(r"\s+", "-", text)[:limit].strip("-")


def destination(r, code: str, criterion: str, item: str, ext: str) -> str:
    req = r.get(code)
    ia = r.impact_area(req.impact_area)
    folder = f"{r.order.index(ia.code)}. {ia.prefix_excel} {ia.name_fr}"
    stem = f"{req.code_excel.replace(' ', '')}_{criterion}_{slug(item)}" if criterion else \
        f"{req.code_excel.replace(' ', '')}_{slug(item)}"
    return f"{folder}/{req.code_excel}/{stem}{ext}"


def _inside(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def build_plan(gap: Path, source: Path, out: Path, comments_path: Path | None = None) -> Path:
    gap, source, out = Path(gap), Path(source), Path(out)
    if _inside(out, source):
        raise ValueError("Le plan ne s'écrit jamais dans le dossier source du client (lecture seule).")
    if out.exists():
        raise FileExistsError(f"{out} existe déjà : le script n'écrase jamais un fichier.")
    r = ref.Referentiel.load()
    comments = _load_comments(comments_path, r)

    ws = openpyxl.load_workbook(gap, data_only=True)[fg.GAP_SHEET]
    headers = [c.value for c in ws[1]]
    files = list_files(source)
    used: set[Path] = set()

    wb = openpyxl.Workbook()
    plan = wb.active
    plan.title = PLAN_SHEET
    bg._header(plan, HEADERS, {"Preuve attendue": 45, "Fichier source": 50, "Chemin proposé": 60,
                               "Commentaire de preuve": 60, "Autres candidats": 40})
    for row in ws.iter_rows(min_row=2, values_only=True):
        rec = dict(zip(headers, row))
        rid = rec["req_id"]
        code, _, criterion = rid.partition("-")
        for item in parse_items(rec.get(PREUVES)):
            ranked = sorted(((score(item, f), f) for f in files), key=lambda x: -x[0])
            best = ranked[0] if ranked else (0.0, None)
            second = ranked[1][0] if len(ranked) > 1 else 0.0
            if best[0] < THRESHOLD:
                status, chosen = MISSING, None
            elif second >= THRESHOLD and best[0] - second < MARGIN:
                status, chosen = AMBIGUOUS, None
            else:
                status, chosen = FOUND, best[1]
                used.add(chosen)
            others = [str(f.relative_to(source)) for s, f in ranked[:3] if s >= THRESHOLD and f != chosen]
            ext = chosen.suffix if chosen else ""
            plan.append([
                rid, rec["Code exigence"], code, criterion, item, status,
                str(chosen.relative_to(source)) if chosen else "",
                round(best[0], 2), " | ".join(others),
                destination(r, code, criterion, item, ext) if chosen else "",
                comments.get((rid, _norm(item)), ""), "À valider",
            ])
    dv = DataValidation(type="list", formula1='"À valider,Validé,Rejeté"', allow_blank=False)
    dv.add(f"L2:L{max(plan.max_row, 2)}")
    plan.add_data_validation(dv)

    orphans = wb.create_sheet(ORPHANS_SHEET)
    bg._header(orphans, ["Fichier", "Dossier"], {"Fichier": 60, "Dossier": 40})
    for f in files:
        if f not in used:
            orphans.append([f.name, str(f.parent.relative_to(source))])
    out.parent.mkdir(parents=True, exist_ok=True)
    wb.save(out)
    return out


def _norm(text: str) -> str:
    return " ".join(str(text).split()).lower()


def _load_comments(path, r) -> dict:
    if not path:
        return {}
    out, warnings = {}, []
    for c in json.loads(Path(path).read_text(encoding="utf-8")):
        text = str(c["commentaire"]).strip()
        fg.check_codes(text, r)
        fg.check_style(fg.COMMENT, text, warnings, c["req_id"])
        out[(c["req_id"], _norm(c["preuve"]))] = text
    for w in warnings:
        print(f"- {w}", file=sys.stderr)
    return out


if __name__ == "__main__":
    if len(sys.argv) not in (4, 5):
        sys.exit(__doc__)
    print(build_plan(*[Path(a) for a in sys.argv[1:]]))
