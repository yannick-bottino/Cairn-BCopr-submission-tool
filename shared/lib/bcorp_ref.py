"""Référentiel B Lab Standards V2.2 : lecture du CSV, codes FR <-> EN, applicabilité.

Seule source des codes d'exigence : resources/standards-v2.2/bcorp_v2.2_requirements.csv,
extrait du PDF officiel (resources/standards-v2.2/_source/).
Tout code absent de ce fichier est refusé (UnknownCode).
"""
from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REF_DIR = ROOT / "shared" / "referentiel"
STD_DIR = ROOT / "resources" / "standards-v2.2"
CSV_PATH = STD_DIR / "bcorp_v2.2_requirements.csv"
CRITERIA_EN_PATH = STD_DIR / "criteres_en.csv"
CRITERIA_FR_PATH = STD_DIR / "criteres_fr.csv"
AREAS_PATH = REF_DIR / "impact_areas.json"

# Coquilles d'ids de critères imprimées dans le PDF (et reprises par le CSV) : (code, id imprimé) -> id corrigé
ID_FIXES = {("FW1.1", "1.2.3"): "1.1.3"}
DEADLINE_YEAR = {"Before Year 0": 0, "Year 0": 0, "Year 3": 3, "Year 5": 5}

SIZES = ["Company without workers", "Micro", "Small", "Medium", "Large", "X Large", "XX Large"]
SECTORS = [
    "Service with Minor Environmental Footprint",
    "Service with Significant Environmental Footprint",
    "Wholesale/Retail",
    "Manufacturing",
    "Agriculture/Growers",
]
HORIZONS = (0, 3, 5)

_CODE_RE = re.compile(r"^\s*([A-Za-z]+)\s*(\d.*?)\s*$")


class UnknownCode(KeyError):
    """Code absent du référentiel V2.2 : ne jamais l'inventer."""


@dataclass(frozen=True)
class ImpactArea:
    code: str
    prefix_excel: str
    name_fr: str
    name_en: str
    colors: tuple[str, ...]


@dataclass(frozen=True)
class Criterion:
    id: str
    text_en: str
    text_fr: str
    deadline: str      # Before Year 0 | Year 0 | Year 3 | Year 5

    @property
    def year(self) -> int:
        return DEADLINE_YEAR[self.deadline]


@dataclass
class Requirement:
    code: str                 # code plateforme, ex. PSG1.1
    code_excel: str           # ex. MGPP 1.1
    impact_area: str          # ex. PSG
    requirement_code: str     # ex. PSG1
    requirement_en: str
    type_ligne: str           # sous_exigence | option | question_risk_tool
    title_en: str
    title_fr: str
    year: int                 # 0, 3 ou 5
    criteria_ids: list[str]
    page_pdf: str
    tracks: list[tuple[str, str, str]] = field(repr=False)  # (taille, secteur, industrie)
    evidence_examples: str = ""
    criteria: list[Criterion] = field(default_factory=list, repr=False)

    def criteria_until(self, horizon: int) -> list[Criterion]:
        """Critères dont l'échéance propre tombe dans l'horizon retenu."""
        return [c for c in self.criteria if c.year <= horizon]

    @property
    def req_ids(self) -> list[str]:
        return [f"{self.code}-{c}" for c in self.criteria_ids] or [self.code]

    def applies_to(self, size: str, sector: str) -> str | None:
        """Renvoie l'industrie concernée ('All' si toutes), ou None si non applicable."""
        hit = None
        for tsz, tse, tind in self.tracks:
            if tsz == size and tse in ("All", sector):
                if tind == "All":
                    return "All"
                hit = tind
        return hit


class Referentiel:
    def __init__(self, rows: list[Requirement], areas: dict[str, ImpactArea], order: list[str]):
        self.rows = rows
        self.areas = areas
        self.order = order
        self._by_code = {r.code.upper(): r for r in rows}
        self._excel_to_site = {a.prefix_excel: a.code for a in areas.values()}

    @classmethod
    def load(cls, csv_path: Path = CSV_PATH, areas_path: Path = AREAS_PATH) -> "Referentiel":
        meta = json.loads(Path(areas_path).read_text(encoding="utf-8"))
        texts_en = _read_criteria(CRITERIA_EN_PATH, "texte_en")
        deadlines = _read_criteria(CRITERIA_EN_PATH, "echeance_critere")
        texts_fr = _read_criteria(CRITERIA_FR_PATH, "texte_fr")
        areas = {
            k: ImpactArea(k, v["prefix_excel"], v["name_fr"], v["name_en"], tuple(v["colors"]))
            for k, v in meta["areas"].items()
        }
        rows = []
        with open(csv_path, encoding="utf-8-sig", newline="") as f:
            for x in csv.DictReader(f):
                ia = areas[x["impact_topic_code"]]
                tracks = [tuple(t.split(" | ")) for t in x["track_factors_brut"].split(" || ") if t]
                ids = [ID_FIXES.get((x["code"], c.strip()), c.strip())
                       for c in x["criteres_conformite_ids"].split(",") if c.strip()]
                ids = list(dict.fromkeys(ids))
                year = int(x["echeance"].replace("Year", ""))
                criteria = [Criterion(i, texts_en.get((x["code"], i), ""), texts_fr.get((x["code"], i), ""),
                                      deadlines.get((x["code"], i)) or f"Year {year}") for i in ids]
                rows.append(Requirement(
                    code=x["code"],
                    code_excel=_excel_code(ia.prefix_excel, x["code"][len(ia.code):]),
                    impact_area=ia.code,
                    requirement_code=x["requirement_code"],
                    requirement_en=x["requirement_en"],
                    type_ligne=x["type_ligne"],
                    title_en=x["intitule_en"],
                    title_fr=x["intitule_fr"],
                    year=year,
                    criteria_ids=ids,
                    page_pdf=x["page_pdf"],
                    tracks=tracks,
                    evidence_examples=x["preuves_exemples_kb"],
                    criteria=criteria,
                ))
        return cls(rows, areas, meta["order"])

    # --- codes ---------------------------------------------------------------

    def get(self, code: str) -> Requirement:
        return self._by_code[self.to_site(code).upper()]

    def to_site(self, raw: str) -> str:
        m = _CODE_RE.match(raw or "")
        if not m:
            raise UnknownCode(raw)
        prefix, rest = m.group(1).upper(), m.group(2).replace(" ", "")
        prefix = self._excel_to_site.get(prefix, prefix)
        row = self._by_code.get(f"{prefix}{rest}".upper())
        if row is None:
            raise UnknownCode(raw)
        return row.code

    def to_excel(self, raw: str) -> str:
        return self.get(raw).code_excel

    def impact_area(self, code: str) -> ImpactArea:
        return self.areas[code]

    # --- applicabilité -------------------------------------------------------

    def applicable(self, size: str, sector: str, horizon: int) -> list[Requirement]:
        if size not in SIZES:
            raise ValueError(f"Taille inconnue : {size!r} (attendu : {SIZES})")
        if sector not in SECTORS:
            raise ValueError(f"Secteur inconnu : {sector!r} (attendu : {SECTORS})")
        if horizon not in HORIZONS:
            raise ValueError(f"Horizon inconnu : {horizon!r} (attendu : {HORIZONS})")
        return [r for r in self.rows if r.year <= horizon and r.applies_to(size, sector)]


def _read_criteria(path: Path, column: str) -> dict[tuple[str, str], str]:
    if not Path(path).exists():
        return {}
    with open(path, encoding="utf-8-sig", newline="") as f:
        return {(x["code"], x["critere_id"]): x[column] for x in csv.DictReader(f)}


def _excel_code(prefix_excel: str, rest: str) -> str:
    return f"{prefix_excel} {rest}"

