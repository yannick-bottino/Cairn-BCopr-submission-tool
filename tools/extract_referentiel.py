#!/usr/bin/env python3
"""
Extraction du référentiel B Lab Standards V2.2 (Body of Knowledge, PDF "all.pdf")
vers un CSV machine-readable : une ligne par sous-exigence (bloc "Track factors").

Usage : python3 extract_referentiel.py <chemin/all.pdf> <sortie.csv> [kb_evidence.json]

Principes :
- Aucun code n'est inventé : chaque code vient du champ "ID:" du bloc "Track factors"
  du PDF (ou de la liste des codes de critères de conformité lus dans le PDF).
- L'applicabilité (taille x secteur x industrie) est lue dans la table "Track factors".
- L'échéance vient du champ "From Year N".
- preuves_type_heuristique : catégories déduites par mots-clés du texte des critères
  de conformité (heuristique, à valider).
- intitule_fr / preuves_exemples_kb : jointure optionnelle avec un JSON issu des
  articles "Exemples de preuves" de la KB B Lab (FR), clé = code EN.
Dépendance : PyMuPDF (pip install pymupdf).
"""
import csv, json, re, sys
import pymupdf as fitz

SIZES = ["Company without workers", "Micro", "Small", "Medium", "Large", "X Large", "XX Large"]
SIZE_SET = set(SIZES)
TOPICS = [  # (code, nom EN, page de début - 1-indexée, d'après la table des matières du PDF)
    ("FR", "Foundation Requirements", 8),
    ("PSG", "Purpose & Stakeholder Governance", 145),
    ("FW", "Fair Work", 287),
    ("JEDI", "Justice, Equity, Diversity & Inclusion", 405),
    ("HR", "Human Rights", 538),
    ("CA", "Climate Action", 748),
    ("ESC", "Environmental Stewardship & Circularity", 854),
    ("GACA", "Government Affairs & Collective Action", 1148),
]
FOOTER_RE = re.compile(r"^B Lab Standards V2\.2 ©B Lab Company February 20, 2026$")
SECTION_HEADERS = ("Intent:", "Clarifying the Compliance Criteria:", "Applying the Criteria",
                   "Implementation Resources:", "Further Guidance:", "Recommendations:",
                   "Interoperability:", "Track factors:")
# Préfixes FR utilisés par la KB B Lab en français (dossiers de la solution 43000372544)
PREFIX_FR = {"FR": "EB", "PSG": "MGPP", "FW": "TE", "JEDI": "JEDI", "HR": "DH", "CA": "AC", "ESC": "GEC", "GACA": "APAC"}
CODE_RE = r"(?:FR|PSG|FW|JEDI|HR|CA|ESC|GACA)\d+(?:\.\d+)*(?:\.[a-z]|[a-z])?"


def topic_of_page(p):
    cur = TOPICS[0]
    for t in TOPICS:
        if p >= t[2]:
            cur = t
    return cur


def clean_lines(text):
    out = []
    for ln in text.split("\n"):
        s = ln.strip()
        if not s or FOOTER_RE.match(s) or re.fullmatch(r"\d{1,4}", s):
            continue
        out.append(s)
    return out


def is_equity_line(s):
    rest = s
    for tok in sorted(SIZES, key=len, reverse=True):
        rest = rest.replace(tok, "")
    return rest.replace("/", "").strip() == "" or s == "None"


def parse_id_table(page):
    words = page.get_text("words")
    hdr = [w for w in words if w[4] == "Sub-requirement"]
    idh = [w for w in words if w[4] == "ID:"]
    y0 = max(w[3] for w in hdr + idh)
    foot = min([w[1] for w in words if w[4] == "©B"] or [10000])
    cols = {"id": [], "year": [], "eq": [], "txt": []}
    for w in sorted(words, key=lambda w: (round(w[1]), w[0])):
        if w[1] <= y0 + 2 or w[1] >= foot - 2:
            continue
        if w[4] == str(page.number + 1) and w[0] > 700:  # numéro de page
            continue
        x = w[0]
        key = "id" if x < 140 else "year" if x < 210 else "eq" if x < 345 else "txt"
        cols[key].append(w[4])
    code = " ".join(cols["id"]).strip()
    year_s = " ".join(cols["year"])
    ym = re.search(r"Year (\d+)", year_s)
    assert re.fullmatch(CODE_RE, code), (page.number + 1, code)
    assert ym, (page.number + 1, year_s)
    txt = " ".join(cols["txt"])
    txt = re.sub(r"(\w)- (\w)", r"\1\2", txt)
    return code, "Year" + ym.group(1), " ".join(cols["eq"]), txt


def evidence_heuristic(txt):
    t = txt.lower()
    cats = []
    rules = [
        ("politique/procédure documentée", r"\bpolic(y|ies)\b|\bprocedure\b|documented process|\bprocess\b"),
        ("publication / accès public", r"publicly|public(ly)? available|discloses|webpage|website|public report"),
        ("approbation instance dirigeante", r"highest governing body|executive team|approved by"),
        ("registre / trace interne", r"\brecords?\b|\btracks?\b|\blog\b"),
        ("données chiffrées / calcul", r"calculat|measure|inventory|data|percentage|%"),
        ("évaluation / analyse", r"assess|evaluat|analysis|saliency|materiality"),
        ("plan / stratégie / objectifs", r"\bplan\b|strategy|targets?|objectives?"),
        ("consultation parties prenantes / salariés", r"survey|consult|feedback|discussion|engag"),
        ("vérification tierce", r"third[- ]party|verif|assurance|certif"),
        ("contrat / engagement signé", r"signs?|agreement|contract|letter"),
        ("formation / communication interne", r"training|guidance|communicat"),
    ]
    for label, rx in rules:
        if re.search(rx, t):
            cats.append(label)
    return "; ".join(cats)


def main(pdf, out_csv, kb_json=None):
    doc = fitz.open(pdf)
    pages = [p.get_text() for p in doc]
    kb = json.load(open(kb_json)) if kb_json else {}

    # Index linéaire (ligne, page)
    lines = []
    for i, t in enumerate(pages):
        for s in clean_lines(t):
            lines.append((s, i + 1))

    # Résumés de requirements (niveau 1, ex. "PSG1 The company ...")
    req_titles = {}
    for s, p in lines:
        m = re.match(r"^((?:FR|PSG|FW|JEDI|HR|CA|ESC|GACA)\d+) (The .+|.+)$", s)
        if m and m.group(1) not in req_titles:
            req_titles[m.group(1)] = s[len(m.group(1)) + 1:]

    rows = []
    idx = [k for k, (s, _) in enumerate(lines) if s == "Track factors:"]
    for n, k in enumerate(idx):
        page = lines[k][1]
        nxt = idx[n + 1] if n + 1 < len(idx) else len(lines)
        # Heading : lignes de la même page avant "Track factors:"
        j = k - 1
        head = []
        while j >= 0 and lines[j][1] == page:
            head.insert(0, lines[j][0]); j -= 1
        heading = " ".join(head)
        # Track table
        j = k + 1
        assert lines[j][0] == "Size" and lines[j + 2][0] == "Industry", (page, lines[j:j+3])
        j += 3
        track = []
        while lines[j][0] != "ID:":
            s = lines[j][0]
            if s in SIZE_SET:
                track.append([s, lines[j + 1][0], ""]); j += 2
            else:
                track[-1][2] = (track[-1][2] + " " + s).strip(); j += 1
        # ID block : lu par coordonnées (colonnes ID | Year | Equity | Text) car
        # l'extraction texte linéaire fusionne parfois les cellules.
        while lines[j][0] != "ID:":
            j += 1
        id_page = lines[j][1]
        code, year, equity, subtext = parse_id_table(doc[id_page - 1])
        while not lines[j][0].startswith("Sub-requirement text:"):
            j += 1
        j += 1
        # Compliance criteria
        cc, cc_start = [], None
        for q in range(j, nxt):
            if lines[q][0] == "Compliance Criteria:":
                cc_start = q; break
        if cc_start is not None:
            for q in range(cc_start + 1, nxt):
                s = lines[q][0]
                if s.startswith(SECTION_HEADERS):
                    break
                cc.append(s)
        cc_text = " ".join(cc)
        cc_ids = [m.rstrip(".") for m in re.findall(r"(?:^|(?<= ))(\d+\.(?:\d+[a-z]?|[a-z])\.(?:[a-z]\.)?\d+)\.? ", cc_text)]
        end_page = (lines[nxt][1] - 1) if nxt < len(lines) else lines[-1][1]

        appl = [t for t in track if t[1] != "None"]
        sizes_app = []
        for t in appl:
            if t[0] not in sizes_app:
                sizes_app.append(t[0])
        all_sectors = all(t[1] == "All" for t in appl)
        all_ind = all(t[2] == "All" for t in appl)
        if not appl:
            autre = "Aucune taille applicable par défaut (activée via Risk Tool FR3.1 ou option)"
        else:
            parts = []
            if not all_sectors:
                bysize = {}
                for t in appl:
                    bysize.setdefault(t[0], []).append(t[1] + ("" if t[2] == "All" else f" [{t[2]}]"))
                parts.append(" | ".join(f"{s}: {', '.join(v)}" for s, v in bysize.items()))
            elif not all_ind:
                parts.append(" | ".join(f"{t[0]}: industrie {t[2]}" for t in appl))
            autre = "; ".join(parts) if parts else "Tous secteurs / toutes industries"
        tcode, tname, _ = topic_of_page(page)
        parent = re.match(r"^((?:FR|PSG|FW|JEDI|HR|CA|ESC|GACA)\d+)", code).group(1)
        k_ev = kb.get(code, {})
        if code.startswith("FR3.1."):
            kind = "question_risk_tool"
        elif re.search(r"(\.[a-z]|\d[a-z])$", code):
            kind = "option"
        else:
            kind = "sous_exigence"
        rows.append({
            "impact_topic_code": tcode,
            "impact_topic": tname,
            "requirement_code": parent,
            "requirement_en": req_titles.get(parent, ""),
            "code": code,
            "type_ligne": kind,
            "intitule_en": subtext,
            "intitule_fr": k_ev.get("titre_fr", ""),
            "applicabilite_taille": " / ".join(sizes_app) if sizes_app else "Aucune (par défaut)",
            "applicabilite_autre": autre,
            "echeance": year,
            "equity_mechanism_eligible_sizes": equity,
            "nb_criteres_conformite": len(dict.fromkeys(cc_ids)),
            "criteres_conformite_ids": ", ".join(dict.fromkeys(cc_ids)),
            "preuves_type_heuristique": evidence_heuristic(cc_text),
            "preuves_exemples_kb": k_ev.get("preuves", ""),
            "code_fr_kb": k_ev.get("code_fr", ""),
            "code_fr_derive": PREFIX_FR[tcode] + code[len(tcode):],
            "jalons_internes_year3_5": "oui" if re.search(r"Year[s]? ?[35]|Years 3 and 5", cc_text) else "",
            "page_pdf": page,
            "page_pdf_fin_bloc": end_page,
            "track_factors_brut": " || ".join(" | ".join(t) for t in track),
        })
    with open(out_csv, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print(f"{len(rows)} sous-exigences extraites -> {out_csv}")


if __name__ == "__main__":
    main(*sys.argv[1:])
