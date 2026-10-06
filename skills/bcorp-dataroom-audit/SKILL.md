---
name: bcorp-dataroom-audit
description: Audite la data room d'un client en vue du diagnostic et du gap analysis B Corp : inventaire des documents, doublons et versions, pièces clés absentes, miroir Markdown pour la lecture, vue par pilier « ce qui existe / ce qui manque » et note de diagnostic. Utiliser quand l'utilisatrice dit « audite la data room », « analyse les documents du client », « inventaire des pièces », « qu'est-ce qui manque dans le dossier », ou démarre le diagnostic B Corp d'un client.
---

# Audit de data room (module 1)

Statut : construit, **pas encore éprouvé sur une data room réelle**. Au premier usage, relire l'inventaire avec l'utilisatrice et corriger `references/classification.json` si le pré-tri se trompe.

## Garde-fous

- Le dossier client (OneDrive) est en **lecture seule** : `inventory.py` refuse d'écrire dedans. Le miroir Markdown se fait sur une **copie de travail**, jamais dans le dossier client.
- Le classement par mots-clés est un pré-tri. Claude arbitre en lisant les documents, et ne cite que des Impact Areas au stade de l'audit : les codes d'exigence viennent au gap analysis, depuis le référentiel.
- Séparer toujours **preuve** et **intention** : une feuille de route, un projet ou un engagement n'est pas une preuve.
- Ne jamais déduire la taille ou le secteur B Lab des documents (règle du module 2). Un écart entre sources (effectif, CA) va dans « Points à fiabiliser ».
- Avant de modifier un livrable existant, lire les décisions actives (`project-memory`).

## Étapes

1. **Inventaire** (lecture seule, sans copie) :
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/bcorp-dataroom-audit/scripts/inventory.py" "<dossier client>" "<Client> x Anchor Strategy_Mission B Corp - Inventaire data room_YYYYMMDD.xlsx"
   ```
   Onglets : « Inventaire » (type et Impact Areas pressentis, doublons, versions antérieures), « Pièces clés » (Kbis, statuts, actionnariat, liasses, organigramme, bilan carbone…), « Vue par pilier ». Prérequis : `pip install openpyxl`.
2. **Copie de travail et miroir Markdown.** Copier la data room dans le dossier de mission (`cp -R "<dossier client>" "<dossier de mission>/_data_room"`), puis lancer `folder-analyzer-optimizer` sur cette copie. Il produit `_parsed/` (un `.md` par document, index par dossier). Tous les docs se lisent ensuite via `_parsed/_index.md`.
3. **Lecture par pilier.** Pour chaque Impact Area, lire les documents pressentis (via `_parsed/`) et la fiche d'intention du standard (`${CLAUDE_PLUGIN_ROOT}/resources/standards-v2.2/_index.md`). Remplir dans l'onglet « Vue par pilier » : « Ce qui existe (preuve) » (document + date), « Ce qui manque (Year 0) », « Points à fiabiliser » (incohérences entre documents, chiffres divergents). Écrire dans une copie de l'inventaire, jamais dans le dossier client.
4. **Note de diagnostic** (Markdown ou Word), dans la voix de `${CLAUDE_PLUGIN_ROOT}/shared/style/voix-julie.md`, structure :
   `1. En une phrase` → `2. Ce que la data room contient` → `3. Lecture par pilier : ce qui existe (preuve) / ce qui manque (Year 0)` → `4. Pièces clés absentes` → `5. Points à fiabiliser avant tout usage B Corp` (liste numérotée) → `6. Demandes au client` → `Sources`.
   Passer la note dans `humanize-output` puis `de-slop`. Nommer avec `file-naming-standard`.
5. **Suite** : l'inventaire et le miroir alimentent le gap analysis (`bcorp-gap-analysis`, colonne Diagnostic) et le plan de preuves (`bcorp-evidence-pack`). Consigner l'audit dans la mémoire projet (`project-memory`, `log_action`).
