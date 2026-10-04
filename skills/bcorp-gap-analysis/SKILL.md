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

1. **Profil client.** Lire le `CLAUDE.md` du dossier client. Compléter ce qui manque avec AskUserQuestion, en une seule salve :
   - taille B Lab : si l'effectif ETP et le CA sont connus, calculer avec `bcorp_ref.size_category(etp, ca_usd)` (règle de la plus petite des deux tailles). La taille reste « À confirmer » tant que `size_thresholds.json` n'est pas vérifié ;
   - secteur B Lab (> 10 % du CA en produits fabriqués en propre = Manufacturing ; produits physiques non fabriqués, y compris une marque qui sous-traite = Wholesale/Retail) ;
   - horizon (0, 3 ou 5), co-prestataire éventuel, options de menu retenues (codes plateforme, ex. `JEDI2.g`).
2. **Écrire `profil.json`** dans le dossier de travail :
   ```json
   {"client": "...", "taille": "Medium", "secteur": "Wholesale/Retail", "industrie": "",
    "horizon": 3, "mecanisme_equite": "À confirmer", "date_depot": "...",
    "co_prestataire": "...", "options_retenues": [], "effectif": "...", "ca": "..."}
   ```
3. **Générer** :
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/bcorp-gap-analysis/scripts/build_gap_excel.py" profil.json "<Client> x Anchor Strategy_Mission B Corp - Gap analysis_YYYYMMDD.xlsx"
   ```
   Prérequis : `pip install openpyxl`.
4. **Contrôler et restituer** : nombre de lignes par Impact Area (onglet 6), options masquées, lignes propres au secteur. Dire clairement ce qui reste à confirmer (taille, secteur, textes des critères).

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
- Le remplissage assisté des colonnes rédactionnelles (`fill_gap.py`) n'est pas encore construit.
