#!/usr/bin/env python3
"""
Génère la base documentaire Markdown du standard B Lab V2.2 (un fichier par bloc du CSV).

Usage : python3 tools/build_standard_md.py [--pdf <Body-of-Knowledge.pdf>] [--out resources/standards-v2.2]

Sorties (dans --out) :
- <n>-<CODE>-<slug FR>/<code plateforme>.md : un fichier par bloc de
  resources/standards-v2.2/bcorp_v2.2_requirements.csv (frontmatter YAML + texte EN verbatim) ;
- <n>-<CODE>-<slug FR>/_index.md et _index.md racine ;
- criteres_en.csv : un critère de conformité par ligne (code, critere_id, texte_en, page, echeance_critere).

Principes : le CSV fixe la liste des blocs, leurs étendues de pages (page_pdf ..
page_pdf_fin_bloc) et les ids de critères ; le texte vient du PDF, nettoyé des pieds de
page (clean_lines de tools/extract_referentiel.py) et des césures. Rien n'est reformulé.
Dépendance : PyMuPDF (pip install pymupdf).
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "shared" / "lib"))

import pymupdf as fitz  # noqa: E402
from extract_referentiel import SECTION_HEADERS, SIZES, clean_lines  # noqa: E402
from bcorp_ref import SECTORS, Referentiel  # noqa: E402

DEFAULT_PDF = ROOT / "resources" / "standards-v2.2" / "_source" / \
    "B-Lab-Standards-V2.2_Body-of-Knowledge_EN_2026-02-20.pdf"
DEFAULT_OUT = ROOT / "resources" / "standards-v2.2"
CSV_PATH = ROOT / "resources" / "standards-v2.2" / "bcorp_v2.2_requirements.csv"
SOURCE = "B Lab Standards V2.2, 20/02/2026"
GENERE_PAR = "tools/build_standard_md.py, ne pas modifier à la main"

# Sections reprises dans les .md (clé interne -> titre Markdown)
KEPT = {
    "cc": "Compliance criteria",
    "intent": "Intent",
    "clar": "Clarifying the compliance criteria",
    "apply": "Applying the criteria",
}
# Lignes qui marquent la fin du dernier bloc d'une Impact Area (pages d'introduction de la suivante)
HARD_STOPS = {"Intent", "Outcome", "Requirements Summary", "Terms and Definitions", "Scope"}

# Coquilles d'ids de critères dans le PDF (et donc dans le CSV) : (code, id imprimé) -> id corrigé
ID_FIXES = {("FW1.1", "1.2.3"): "1.1.3"}
PRINTED_IDS = {(code, fixed): printed for (code, printed), fixed in ID_FIXES.items()}
# Échéance propre d'un critère : marquage en tête de texte (ex. « For Year 5, the company ... »)
DEADLINE_RE = re.compile(r"^(For|Before|By) Year ([035])\b")


def fixed_ids(code, ids):
    return [ID_FIXES.get((code, c), c) for c in ids]


def criterion_deadline(text, year):
    """(echeance_critere, marquage brut du PDF ou None).

    Valeurs : Before Year 0 / Year 0 / Year 3 / Year 5. « For Year N » et « By Year N » -> Year N ;
    « Before Year 0 » est conservé ; « Before Year 3 » -> Year 3 (à réaliser au plus tard pour Year 3).
    Sans marquage : l'année de la sous-exigence.
    """
    m = DEADLINE_RE.match(text)
    if not m:
        return f"Year {year}", None
    raw = m.group(0)
    if raw == "Before Year 0":
        return raw, raw
    return f"Year {m.group(2)}", raw


BULLET_RE = re.compile(r"^(•|o |◦|▪|– |- |[a-z]\) |[ivx]+\) |\[[0-9a-z.,;\s]+\] ?)")


# --------------------------------------------------------------------------- texte

class Text:
    """Nettoyage du texte : vocabulaire du PDF pour trancher les césures."""

    def __init__(self, doc):
        self.vocab = set()
        for page in doc:
            for ln in page.get_text().split("\n"):
                toks = re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)*", ln)
                for t in toks[:-1]:  # le dernier mot d'une ligne peut être une césure
                    self.vocab.add(t.lower())

    def join(self, a: str, b: str) -> str:
        """Concatène deux lignes physiques d'un même paragraphe."""
        m = re.search(r"([A-Za-z]+)-$", a)
        if m:
            n = re.match(r"([A-Za-z]+)", b)
            if n:
                whole = (m.group(1) + n.group(1)).lower()
                hyph = (m.group(1) + "-" + n.group(1)).lower()
                if whole in self.vocab and hyph not in self.vocab:
                    return a[:-1] + b
            return a + b
        return a + " " + b

    def paragraphs(self, lines):
        """Regroupe les lignes physiques en paragraphes (puces, sous-points, phrases)."""
        paras = []
        for s in lines:
            if not paras or BULLET_RE.match(s) or re.search(r"[.:;?!]$", paras[-1]):
                paras.append(s)
            else:
                paras[-1] = self.join(paras[-1], s)
        return paras


def dedupe(paras):
    """Le PDF répète parfois des paragraphes (ex. FR3.1.a, FR3.1.e) : on garde la 1re occurrence.

    Comparaison à la ponctuation finale près ; renvoie (paragraphes, nb retirés).
    """
    seen, out = set(), []
    for p in paras:
        key = p.rstrip(" .")
        if len(key) > 40 and key in seen:
            continue
        seen.add(key)
        out.append(p)
    return out, len(paras) - len(out)


def md_lines(paras):
    """Paragraphes -> Markdown : puces en listes, le reste en paragraphes."""
    out = []
    last_letter = None  # dernier sous-point a), b)... : distingue i) lettre / i) romain
    for p in paras:
        m = re.match(r"^([a-z]+)\) ", p)
        roman = bool(m and re.fullmatch(r"[ivx]+", m.group(1)) and last_letter
                     and not (len(m.group(1)) == 1 and ord(m.group(1)) == ord(last_letter) + 1))
        if m and not roman and len(m.group(1)) == 1:
            last_letter = m.group(1)
        elif not m:
            last_letter = None if not p.startswith(("•", "o ", "◦")) else last_letter
        if p.startswith(("• ", "▪ ")):
            item = "- " + p[2:]
        elif p.startswith("•"):
            item = "- " + p[1:].lstrip()
        elif p.startswith(("o ", "◦ ")):
            item = "  - " + p[2:]
        elif roman:
            item = "  - " + p
        elif m:
            item = "- " + p
        else:
            item = None
        if item is None:
            if out and out[-1] != "":
                out.append("")
            out.append(p)
            out.append("")
        else:
            out.append(item)
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out)


# --------------------------------------------------------------------------- PDF

def block_lines(doc, start, end):
    """Lignes (texte, page) du bloc, pieds de page retirés."""
    return [(s, p) for p in range(start, end + 1) for s in clean_lines(doc[p - 1].get_text())]


def sections(lines):
    """Découpe le bloc en sections à partir de 'Compliance Criteria:'."""
    out = {k: [] for k in KEPT}
    apply_title = None
    stop_page = None
    cur = None
    started = False
    for s, p in lines:
        if not started:
            started = s == "Compliance Criteria:"
            cur = "cc" if started else None
            continue
        if s in HARD_STOPS or s == "Track factors:":
            stop_page = p
            break
        if s == "Compliance Criteria:":
            cur = "cc"
        elif s == "Intent:":
            cur = "intent"
        elif s == "Clarifying the Compliance Criteria:":
            cur = "clar"
        elif s.startswith("Applying the Criteria"):
            cur = "apply"
            apply_title = apply_title or s.rstrip(":")
        elif s.startswith(SECTION_HEADERS):
            cur = None
        elif cur:
            out[cur].append((s, p))
    last = lines[-1][1] if lines else None
    end = stop_page - 1 if stop_page else last
    return out, apply_title, end


def split_criteria(cc, ids):
    """Découpe 'Compliance Criteria' selon les ids du CSV.

    Renvoie ({id: ([(ligne, page)], page)}, préambule, ids dans l'ordre du PDF).
    Chaque id est cherché en début de ligne ; à défaut, en milieu de ligne (la ligne
    est alors coupée). L'ordre du CSV n'est pas toujours celui du PDF (ex. PSG2.1).
    """
    lines = list(cc)
    rx = {c: re.compile(r"(?:^|(?<=\s))" + re.escape(c) + r"\.?(?=\s|$)") for c in ids}

    def line_start(c):
        return next((k for k, (s, _) in enumerate(lines) if rx[c].match(s)), None)

    for c in ids:
        if line_start(c) is None:
            for k, (s, p) in enumerate(lines):
                m = rx[c].search(s)
                if m and m.start() > 0:
                    lines[k:k + 1] = [(s[:m.start()].rstrip(), p), (s[m.start():], p)]
                    break
    starts = sorted((k, c) for c in ids if (k := line_start(c)) is not None)
    res = {}
    for n, (k, cid) in enumerate(starts):
        stop = starts[n + 1][0] if n + 1 < len(starts) else len(lines)
        chunk = lines[k:stop]
        first = re.sub(r"^" + re.escape(cid) + r"\.?\s*", "", chunk[0][0])
        body = ([(first, chunk[0][1])] if first else []) + chunk[1:]
        res[cid] = (body, chunk[0][1])
    pre = lines[:starts[0][0]] if starts else lines
    return res, pre, [c for _, c in starts] + [c for c in ids if c not in res]


# --------------------------------------------------------------------------- Markdown

def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def q(v):
    """Scalaire YAML sûr (chaîne JSON = YAML valide)."""
    return json.dumps(v, ensure_ascii=False)


def cell(s):
    return s.replace("|", "\\|").replace("\n", " ")


def tracks_of(row):
    return [t.split(" | ") for t in row["track_factors_brut"].split(" || ") if t]


def render_block(row, req, area, txt, secs, apply_title, crit, pre, pdf_order, end_page):
    ids = fixed_ids(req.code, req.criteria_ids)
    tracks = tracks_of(row)
    appl = [t for t in tracks if t[1] != "None"]
    fm = ["---",
          f"code: {q(req.code)}",
          f"code_fr: {q(req.code_excel)}",
          f"impact_area: {q(area.code)}",
          f"impact_area_fr: {q(area.name_fr)}",
          f"requirement_code: {q(req.requirement_code)}",
          f"type: {q(req.type_ligne)}",
          f"year: {req.year}",
          "criteria: [" + ", ".join(q(c) for c in ids) + "]",
          f"pages: {q(row['page_pdf'] + '-' + str(end_page))}",
          "applicabilite:" + ("" if appl else " []")]
    for t in appl:
        fm.append(f"  - {{taille: {q(t[0])}, secteur: {q(t[1])}, industrie: {q(t[2])}}}")
    fm += [f"source: {q(SOURCE)}", f"genere_par: {q(GENERE_PAR)}", "---", ""]

    b = [f"# {req.code} ({req.code_excel}) : {req.title_en}", ""]
    if req.title_fr:
        b += [f"*Intitulé FR (traduction à relire) : {req.title_fr}*", ""]
    b += [f"Impact Area : {area.name_en} ({area.name_fr}). Pages PDF {row['page_pdf']}-{end_page}. "
          f"Échéance : Year {req.year}.", ""]
    b += ["## Requirement", ""]
    if req.requirement_en:
        b += [f"**{req.requirement_code}** : {req.requirement_en}", ""]
    b += [f"**{req.code}** : {req.title_en}", ""]

    b += ["## Compliance criteria", ""]
    if pre:
        b += [md_lines(txt.paragraphs([s for s, _ in pre])), ""]
    for printed in pdf_order:
        cid = ID_FIXES.get((req.code, printed), printed)
        lines = crit.get(printed, ([], None))[0]
        paras = txt.paragraphs([s for s, _ in lines])
        dl, raw = criterion_deadline(paras[0] if paras else "", req.year)
        b += [f"### {cid}", ""]
        b += [f"*Échéance du critère : {dl}" + (f" (marquage PDF : « {raw} »)*" if raw
                                                 else " (celle de la sous-exigence)*"), ""]
        if cid != printed:
            b += [f"> Anomalie du PDF : ce critère est imprimé « {printed} » (coquille). L'id corrigé "
                  f"{cid} est retenu ici et dans tout le plugin ; le CSV conserve l'id imprimé {printed}.", ""]
        b += [md_lines(paras), ""]
        fr = next((c.text_fr for c in req.criteria if c.id == cid and c.text_fr), "")
        if fr:
            b += [f"*Traduction FR (à relire, compilation tierce) :* {fr}", ""]

    for key in ("intent", "clar", "apply"):
        if secs[key]:
            b += [f"## {KEPT[key]}", ""]
            if key == "apply" and apply_title:
                b += [f"*{apply_title}*", ""]
            paras, dropped = dedupe(txt.paragraphs([s for s, _ in secs[key]]))
            b += [md_lines(paras), ""]
            if dropped:
                b += [f"*({dropped} paragraphe(s) répété(s) à l'identique dans le PDF, non repris.)*", ""]

    b += ["## Applicabilité", "",
          "| Taille | " + " | ".join(SECTORS) + " |",
          "|---|" + "---|" * len(SECTORS)]
    for size in reversed(SIZES):
        cells = []
        for sector in SECTORS:
            hits = [t[2] for t in tracks if t[0] == size and t[1] in ("All", sector)]
            if not hits:
                cells.append("Non")
            elif "All" in hits:
                cells.append("Oui")
            else:
                cells.append("Oui (" + cell(", ".join(dict.fromkeys(hits))) + ")")
        b.append(f"| {size} | " + " | ".join(cells) + " |")
    b.append("")
    if row["applicabilite_autre"]:
        b += [f"Synthèse : {row['applicabilite_autre']}.", ""]

    if req.evidence_examples:
        b += ["## Exemples de preuves (KB B Lab, résumé automatique à relire)", "", req.evidence_examples, ""]
    return "\n".join(fm + b).rstrip() + "\n"


def index_table(reqs, link):
    t = ["| Code | Code FR | Intitulé | Type | Year | Lien |", "|---|---|---|---|---|---|"]
    for r in reqs:
        title = r.title_fr or r.title_en
        t.append(f"| {r.code} | {r.code_excel} | {cell(title)} | {r.type_ligne} | {r.year} | [{r.code}.md]({link(r)}) |")
    return t


def build(pdf, out):
    out = Path(out)
    ref = Referentiel.load()
    with open(CSV_PATH, encoding="utf-8-sig", newline="") as f:
        rows = {x["code"]: x for x in csv.DictReader(f)}
    doc = fitz.open(pdf)
    txt = Text(doc)

    folders = {}
    for n, code in enumerate(ref.order):
        a = ref.impact_area(code)
        folders[code] = f"{n}-{code}-{slugify(a.name_fr)}"

    # Nettoyage des fichiers générés précédemment (le dossier _source est préservé)
    if out.exists():
        for d in out.iterdir():
            if d.is_dir() and re.match(r"^\d+-[A-Z]+-", d.name):
                for p in d.glob("*.md"):
                    p.unlink()
                if not any(d.iterdir()):
                    d.rmdir()
    out.mkdir(parents=True, exist_ok=True)

    crit_rows, problems = [], []
    for req in ref.rows:
        row = rows[req.code]
        area = ref.impact_area(req.impact_area)
        lines = block_lines(doc, int(row["page_pdf"]), int(row["page_pdf_fin_bloc"]))
        secs, apply_title, end_page = sections(lines)
        printed_ids = [PRINTED_IDS.get((req.code, c), c) for c in req.criteria_ids]
        crit, pre, pdf_order = split_criteria(secs["cc"], printed_ids)
        for cid in pdf_order:
            if cid not in crit or not crit[cid][0]:
                problems.append(f"{req.code}:{cid}")
                continue
            body, page = crit[cid]
            paras = txt.paragraphs([s for s, _ in body])
            crit_rows.append({"code": req.code, "critere_id": ID_FIXES.get((req.code, cid), cid),
                              "texte_en": "\n".join(paras), "page": page,
                              "echeance_critere": criterion_deadline(paras[0], req.year)[0]})
        d = out / folders[req.impact_area]
        d.mkdir(exist_ok=True)
        (d / f"{req.code}.md").write_text(
            render_block(row, req, area, txt, secs, apply_title, crit, pre, pdf_order, end_page), encoding="utf-8")

    for code in ref.order:
        a = ref.impact_area(code)
        reqs = [r for r in ref.rows if r.impact_area == code]
        lines = [f"# {code} ({a.prefix_excel}) : {a.name_fr} / {a.name_en}", "",
                 f"{len(reqs)} blocs. Source : {SOURCE}. Fichiers générés par tools/build_standard_md.py.", ""]
        lines += index_table(reqs, lambda r: f"{r.code}.md")
        (out / folders[code] / "_index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    lines = ["# Standard B Corp V2.2 : base documentaire", "",
             f"Source : {SOURCE} (PDF dans `_source/`). {len(ref.rows)} blocs, généré par tools/build_standard_md.py.", "",
             "## Mode d'emploi (LLM)", "",
             "1. Chercher un bloc par son code plateforme (ex. `PSG1.1`, `JEDI2.a`, `FR3.1.a`) : fichier `<code>.md` dans le dossier de son Impact Area.",
             "2. Un code FR (ex. `MGPP 1.1`) se convertit via la colonne Code FR ci-dessous.",
             "3. Chaque fichier contient le texte EN verbatim : exigence, critères de conformité (`### <id>`), intent, clarifications, applicabilité.",
             "4. Les intitulés FR et exemples de preuves viennent de la KB B Lab (traduction / résumé automatique, à relire).",
             "5. Pour filtrer (taille, secteur, échéance), utiliser le CSV `resources/standards-v2.2/bcorp_v2.2_requirements.csv`, qui reste la source machine ; `criteres_en.csv` donne un critère par ligne.",
             ""]
    for code in ref.order:
        a = ref.impact_area(code)
        reqs = [r for r in ref.rows if r.impact_area == code]
        lines += [f"## [{code} : {a.name_fr}]({folders[code]}/_index.md)", ""]
        lines += index_table(reqs, lambda r: f"{folders[r.impact_area]}/{r.code}.md")
        lines.append("")
    (out / "_index.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    with open(out / "criteres_en.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["code", "critere_id", "texte_en", "page", "echeance_critere"], lineterminator="\n")
        w.writeheader()
        w.writerows(crit_rows)

    print(f"{len(ref.rows)} blocs -> {out} ; {len(crit_rows)} critères avec texte", file=sys.stderr)
    if problems:
        print(f"Critères sans texte ({len(problems)}) : {', '.join(problems)}", file=sys.stderr)
    return problems


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--pdf", default=str(DEFAULT_PDF))
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    a = ap.parse_args(argv)
    build(a.pdf, a.out)


if __name__ == "__main__":
    main()
