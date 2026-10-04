# Anchor Strategy B Corp tool

Plugin Claude Code / Cowork privé d'Anchor Strategy pour préparer la certification B Corp (B Lab Standards V2.2, 20/02/2026).

Usage réservé à Anchor Strategy : voir `LICENSE`.

## Modules

| # | Module | Skill | État |
|---|---|---|---|
| 1 | Audit de data room | `bcorp-dataroom-audit` | à construire |
| 2 | Caractérisation et éligibilité | `bcorp-company-profile` | socle prêt (`size_category`, applicabilité) |
| 3 | Excel de gap analysis | `bcorp-gap-analysis` | v0.1 : génération de la structure |
| 4 | Preuves et commentaires de preuve | `bcorp-evidence-pack` | à construire |
| 5 | Plan de saisie plateforme | `bcorp-platform-plan` | à construire (copier-coller + checklist, pas d'automatisation navigateur) |

## Installation

```
/plugin marketplace add yannick-bottino/Cairn-BCopr-submission-tool
/plugin install anchor-strategy-bcorp-tool@anchor-strategy-bcorp
```

Prérequis Python : `pip install openpyxl`. Dépend des skills transverses de `consulting-skills` (`project-memory`, `file-naming-standard`, `humanize-output`, `de-slop`).

## Structure

- `shared/referentiel/` : référentiel V2.2 (184 blocs, codes EN et FR), Impact Areas, seuils de taille.
- `shared/lib/bcorp_ref.py` : lecture du référentiel, conversion des codes, applicabilité, taille.
- `shared/style/voix-julie.md` : guide de rédaction des cellules (exemples anonymisés).
- `skills/<module>/` : un skill par module, avec ses scripts.
- `tests/` : `python3 -m pytest`.

## Règles

- Aucun code d'exigence hors du référentiel.
- Aucune donnée client dans ce dépôt.
- Rien n'est publié sur app.bcorporation.net sans validation, lot par lot.
