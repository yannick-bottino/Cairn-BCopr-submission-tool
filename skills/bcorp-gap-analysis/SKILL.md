---
name: bcorp-gap-analysis
description: Génère l'Excel de gap analysis B Corp (B Lab Standards V2.2) d'un client, filtré par taille, secteur et horizon, au format Anchor Strategy (8 onglets, codes FR et codes plateforme). Utiliser quand l'utilisatrice dit « gap analysis B Corp », « génère l'Excel B Corp », « prépare le gap analysis de <client> », « référentiel filtré », ou démarre le diagnostic B Corp d'un nouveau client.
---

# Gap analysis B Corp (module 3)

Règle de conception : Claude propose, le script applique, l'Excel garde la trace.

## Garde-fous

- Seule source des codes : `${CLAUDE_PLUGIN_ROOT}/resources/standards-v2.2/bcorp_v2.2_requirements.csv`. Le script refuse tout code absent. Ne jamais écrire un code à la main dans l'Excel.
- Ne jamais écrire dans un dossier client OneDrive : générer dans le dossier de travail, puis laisser l'utilisatrice déposer le fichier.
- Le script n'écrase jamais un fichier existant. Pour une nouvelle version, changer le nom (convention `file-naming-standard`).
- Avant de modifier un livrable existant, lire les décisions actives du projet (`project-memory`, `read_active_decisions`).

## Étapes

1. **Profil client.** Si le module 2 a tourné (`bcorp-company-profile`), utiliser directement son `profil.json` et passer à l'étape 3. Sinon, lire le `CLAUDE.md` du dossier client. La taille et le secteur B Lab ne se calculent jamais : ils viennent de la plateforme B Lab. Demander à l'utilisatrice, avec AskUserQuestion, l'une des deux sources :
   - **l'export PDF de la page de profil / scoping B Lab** du client : y lire la taille, le secteur, l'industrie et les réponses du Risk Tool telles qu'affichées, et citer la page ;
   - **à défaut, ses réponses manuelles** : taille, secteur et industrie tels qu'affichés sur la plateforme.

   Ne jamais déduire une taille d'un effectif ou d'un chiffre d'affaires, même si ces données figurent dans la data room. Si l'export et les documents du client divergent, le signaler sans trancher.

   Demander aussi : horizon (0, 3 ou 5), co-prestataire éventuel, options de menu retenues (codes plateforme, ex. `JEDI2.g`).
2. **Écrire `profil.json`** dans le dossier de travail :
   ```json
   {"client": "...", "taille": "Medium", "secteur": "Wholesale/Retail", "industrie": "",
    "horizon": 3, "mecanisme_equite": "À confirmer", "date_depot": "...",
    "co_prestataire": "...", "options_retenues": [],
    "source_profil": "Export PDF plateforme B Lab"}
   ```
   `source_profil` est obligatoire : `Export PDF plateforme B Lab` ou `Déclaration manuelle`. Le script refuse le profil sans elle.
3. **Générer** :
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/bcorp-gap-analysis/scripts/build_gap_excel.py" profil.json "<Client> x Anchor Strategy_Mission B Corp - Gap analysis_YYYYMMDD.xlsx"
   ```
   Prérequis : `pip install openpyxl`.
4. **Contrôler et restituer** : nombre de lignes par Impact Area (onglet 6), options masquées, lignes propres au secteur. Dire clairement ce qui reste à confirmer (traductions FR des critères, options retenues).

## Remplir les cellules (propositions de Claude)

Travailler **une Impact Area à la fois** (un lot), dans l'ordre EB, MGPP, TE, JEDI, DH, AC, GEC, APAC.

1. Lire les décisions actives du projet (`project-memory`) et les documents du client (miroir Markdown de la data room si disponible).
2. Pour chaque ligne du lot, lire le fichier du standard `${CLAUDE_PLUGIN_ROOT}/resources/standards-v2.2/<Impact Area>/<code>.md` : critère, intention, clarifications.
3. Rédiger en appliquant `${CLAUDE_PLUGIN_ROOT}/shared/style/voix-julie.md`. Une ligne sans document qui la prouve reste à 0 ou 1, jamais à 2. Laisser vide plutôt que d'inventer.
4. Écrire `propositions_<lot>.json` :
   ```json
   [{"req_id": "PSG1.1-1.1.1", "champs": {
      "Niveau de conformité": "1",
      "Diagnostic & gap analysis": "...",
      "Actions recommandées": "1. ...",
      "Preuves (& intitulés associés)": "Preuves attendues :\n- ...",
      "Commentaire soumission dossier pour l'auditeur": "...\n- Pièces jointes : ...",
      "Typologie du gap (Anchor)": "Correctif mineur / pièce à produire",
      "Criticité (Anchor)": "3-Modéré",
      "Justification de la typologie (Anchor)": "..."}}]
   ```
   Colonnes autorisées : celles ci-dessus et « Priorité B Corp (Anchor) ». Le `req_id` vient de la colonne masquée de l'Excel.
5. Appliquer dans un **nouveau** fichier :
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/bcorp-gap-analysis/scripts/fill_gap.py" "<gap>.xlsx" propositions_<lot>.json "<gap>_<lot>.xlsx"
   ```
   Le script refuse le lot entier si un code cité n'existe pas, si une valeur sort des listes, si le texte contient un tiret cadratin ou du Markdown, ou si le commentaire auditeur mentionne un manque. Il n'écrit jamais dans une cellule déjà remplie : il la signale.
6. Restituer : nombre de cellules écrites, cellules ignorées, avertissements (« en cours » sans jalon). Passer 3 commentaires auditeur du lot dans `humanize-output` puis `de-slop`, pas tous.
7. L'utilisatrice relit dans Excel (cellules surlignées en jaune) et passe chaque ligne de l'onglet « Propositions » à « Validé » ou « Rejeté ». **Seuls les commentaires « Validé » pourront être repris dans le plan de saisie plateforme.**

## Ce que contient l'Excel

- `3. Gap analysis` : une ligne par critère de conformité ; les questions du Risk Tool (FR3.1.a à n) tiennent sur une ligne chacune. `Code exigence` = sigle FR (MGPP 1.1), `Code plateforme` = code affiché sur app.bcorporation.net (PSG1.1). `req_id` (masquée) est la clé entre modules.
- Colonnes jamais publiées sur la plateforme : Diagnostic, Actions, Priorités, Responsable, Équipe projet, Commentaires, colonnes Anchor et co-prestataire. Seul le commentaire auditeur est publiable, après validation.
- `Plateforme : statut` reprend les statuts réels du site : Non démarré, En cours, Terminé : Preuve Prêt.

## Lire le standard

Pour toute ligne, lire `${CLAUDE_PLUGIN_ROOT}/resources/standards-v2.2/_index.md` puis le fichier `<code plateforme>.md` (critères, intention, clarifications, applicabilité). Ne jamais diagnostiquer de mémoire.

## Rédaction des cellules

Pour toute proposition de diagnostic, d'actions, de preuves attendues ou de commentaire auditeur, appliquer `${CLAUDE_PLUGIN_ROOT}/shared/style/voix-julie.md`. Écrire en français. Toujours séparer preuve et intention. Par défaut, une ligne est « à confirmer », jamais « couverte » sans document cité.

## Limites connues (v0.1)

- Textes des critères : traduction FR (compilation tierce, à relire) pour 174 critères sur 594 ; les autres affichent le texte officiel EN préfixé `[EN]`. Le texte de référence de chaque sous-exigence est dans `${CLAUDE_PLUGIN_ROOT}/resources/standards-v2.2/<Impact Area>/<code>.md`.
- 61 sous-exigences n'ont pas d'intitulé FR : la colonne affiche l'intitulé EN préfixé `[EN]`.
