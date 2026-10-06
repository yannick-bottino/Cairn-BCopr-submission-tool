---
name: bcorp-evidence-pack
description: Prépare le dossier de preuves B Corp à partir d'un gap analysis complété : liste des preuves par exigence, rapprochement avec les fichiers du client, commentaires de preuve, puis rangement par copie dans une arborescence par Impact Area et par code. Utiliser quand l'utilisatrice dit « dossier de preuves », « liste des preuves », « commentaires de preuve », « range les preuves », « réorganise le dossier de preuves », ou prépare la soumission B Corp d'un client.
---

# Dossier de preuves B Corp (module 4)

Règle de conception : Claude propose, le script applique, l'Excel garde la trace.

## Garde-fous

- Le dossier du client (OneDrive) est en **lecture seule** : les scripts refusent d'écrire dedans. Le rangement se fait par **copie** dans un dossier cible distinct, jamais par déplacement.
- Rien n'est copié sans « Décision = Validé » dans le plan, et `apply_reorg.py` simule tant que `--execute` n'est pas passé.
- Aucun fichier existant n'est écrasé : un doublon identique est signalé « déjà présent », un fichier différent « conflit ».
- Les commentaires de preuve sont publiables sur la plateforme : mêmes règles que le commentaire auditeur (voir `${CLAUDE_PLUGIN_ROOT}/shared/style/voix-julie.md`), contrôlées par le script (codes du référentiel, aucun manque, ni tiret cadratin ni Markdown).
- Avant de modifier un livrable existant, lire les décisions actives (`project-memory`).

## Étapes

1. **Entrée** : le gap analysis complété, avec la colonne « Preuves (& intitulés associés) » remplie (une preuve par ligne « - » ou « > »). Prérequis : `pip install openpyxl`.
2. **Commentaires de preuve.** Pour chaque preuve attendue, rédiger un commentaire court (document, date, page, ce qu'il prouve) en lisant le fichier du standard `${CLAUDE_PLUGIN_ROOT}/resources/standards-v2.2/<Impact Area>/<code>.md`. Les écrire dans `commentaires_preuves.json` :
   ```json
   [{"req_id": "PSG1.1-1.1.1", "preuve": "Statuts à jour", "commentaire": "Statuts du 15/01/2024, art. 2 p.1 : raison d'être."}]
   ```
   Passer un échantillon de 3 commentaires dans `humanize-output` puis `de-slop`.
3. **Plan** :
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/bcorp-evidence-pack/scripts/evidence_plan.py" "<gap>.xlsx" "<dossier preuves client>" "<Client> x Anchor Strategy_Mission B Corp - Plan de preuves_YYYYMMDD.xlsx" commentaires_preuves.json
   ```
   Onglet « Plan de preuves » : une ligne par preuve attendue, statut Trouvé / Ambigu / Manquant, fichier source, autres candidats, chemin proposé `<n>. <sigle> <Impact Area>/<Code exigence>/<Code>_<critère>_<intitulé>.<ext>`. Onglet « Fichiers non rattachés » : ce que le client a fourni et qui ne sert encore à aucune exigence.
4. **Restituer** : nombre de preuves trouvées, ambiguës, manquantes ; liste des manquantes par Impact Area (ce sont les demandes à faire au client). Ne jamais présenter un « Trouvé » comme une preuve suffisante : le rapprochement porte sur le nom du fichier, pas sur son contenu.
5. **Validation** : l'utilisatrice relit le plan dans Excel, corrige au besoin « Fichier source » (cas Ambigu) et passe les lignes à « Validé ».
6. **Rangement** : simulation, puis copie après accord explicite.
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/bcorp-evidence-pack/scripts/apply_reorg.py" plan.xlsx "<dossier preuves client>" "<dossier cible>"
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/bcorp-evidence-pack/scripts/apply_reorg.py" plan.xlsx "<dossier preuves client>" "<dossier cible>" --execute
   ```
   Le journal `_journal_copies.csv` (horodatage, source, destination, empreinte SHA-256) reste dans le dossier cible. Nommer le plan avec `file-naming-standard`.

## Limites

- Rapprochement par nom de fichier : un fichier mal nommé sort en « Manquant », un nom générique peut sortir en « Trouvé » à tort. Toujours relire.
- Les commentaires de preuve ne sont pas encore repris automatiquement dans le plan de saisie plateforme (module 5).
