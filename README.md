# Anchor Strategy B Corp tool

Plugin Claude Code / Cowork privé d'Anchor Strategy pour préparer la certification B Corp (B Lab Standards V2.2, 20/02/2026).

Usage réservé à Anchor Strategy : voir `LICENSE`.

## Modules

| # | Module | Skill | État |
|---|---|---|---|
| 1 | Audit de data room | `bcorp-dataroom-audit` | à construire |
| 2 | Caractérisation et éligibilité | `bcorp-company-profile` | socle prêt (applicabilité ; taille et secteur relevés sur la plateforme, jamais calculés) |
| 3 | Excel de gap analysis | `bcorp-gap-analysis` | v0.2 : génération + propositions rédigées (`fill_gap.py`) |
| 4 | Preuves et commentaires de preuve | `bcorp-evidence-pack` | à construire |
| 5 | Plan de saisie plateforme | `bcorp-platform-plan` | à construire (copier-coller + checklist, pas d'automatisation navigateur) |

## Installation

```
/plugin marketplace add yannick-bottino/Cairn-BCopr-submission-tool
/plugin install anchor-strategy-bcorp-tool@anchor-strategy-bcorp
```

Prérequis Python : `pip install openpyxl` (et `pymupdf` pour régénérer la base documentaire).

Le plugin est autoporteur : les skills transverses qu'il appelle (`project-memory`, `file-naming-standard`, `humanize-output`, `de-slop`, `folder-analyzer-optimizer`) sont embarqués dans `skills/`, seul emplacement chargé par Claude Code et par Cowork. Voir `THIRD_PARTY_NOTICES.md`.

Cowork : `python3 tools/package_plugin.py` produit `dist/anchor-strategy-bcorp-tool-<version>.zip`, à téléverser.

## Structure

- `resources/standards-v2.2/` : PDF officiel (`_source/`), référentiel machine (`bcorp_v2.2_requirements.csv`), un fichier Markdown par sous-exigence rangé par Impact Area, `criteres_en.csv` (texte et échéance de chaque critère), `criteres_fr.csv` (traductions à relire). Les .md se régénèrent avec `python3 tools/build_standard_md.py`.
- `shared/referentiel/` : Impact Areas (noms FR/EN, préfixes, couleurs).
- `shared/lib/bcorp_ref.py` : lecture du référentiel, conversion des codes, applicabilité, taille.
- `shared/style/voix-julie.md` : guide de rédaction des cellules (exemples anonymisés).
- `skills/<module>/` : un skill par module, avec ses scripts.
- `tests/` : `python3 -m pytest`.

## Règles

- Règle stricte : tout skill appelé est embarqué dans `skills/` (test `tests/test_self_contained.py`). Règles complètes du dépôt : `.claude/CLAUDE.md`.

- Aucun code d'exigence hors du référentiel.
- Aucune donnée client dans ce dépôt.
- Rien n'est publié sur app.bcorporation.net sans validation, lot par lot.
