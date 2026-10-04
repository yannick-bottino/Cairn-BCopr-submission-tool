---
name: bcorp-platform-plan
description: Prépare le plan de saisie B Corp pour app.bcorporation.net : par fiche (code plateforme), le commentaire validé à coller, les pièces à attacher et leurs commentaires de preuve, lot par lot. Aucune automatisation du navigateur. Utiliser quand l'utilisatrice dit « plan de saisie », « prépare la saisie plateforme », « quoi coller sur la plateforme », « checklist d'upload », ou prépare la soumission B Corp d'un client.
---

# Plan de saisie plateforme (module 5)

Le plugin ne pilote pas app.bcorporation.net. Il produit un plan à coller à la main, lot par lot. Raisons : les CGU de B Lab interdisent les « automatic devices », l'upload ouvre un sélecteur de fichiers natif, et le gain réel est dans la qualité des commentaires, pas dans le clic.

## Garde-fous

- **Rien n'entre dans le plan sans validation** : un commentaire proposé par Claude doit être « Validé » dans l'onglet « Propositions » du gap analysis ; un commentaire saisi par la consultante est réputé validé.
- Statut cible : toujours « En cours ». Jamais « Terminé : Preuve Prêt » (c'est le client qui bascule après dépôt réel).
- Ne jamais toucher aux dates d'échéance ni aux assignations sur la plateforme.
- Seule la colonne « Commentaire soumission dossier pour l'auditeur » sort de l'Excel. Diagnostic, actions, priorités, responsables et commentaires internes ne sortent jamais.

## Étapes

1. Vérifier que les commentaires du lot sont validés (onglet « Propositions ») et, si le module 4 a tourné, que le plan de preuves est validé.
2. Générer le plan d'un lot (une Impact Area, code plateforme : FR, PSG, FW, JEDI, HR, CA, ESC, GACA) :
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/bcorp-platform-plan/scripts/platform_plan.py" "<gap>.xlsx" "<Client> x Anchor Strategy_Mission B Corp - Plan de saisie PSG_YYYYMMDD.xlsx" --lot PSG --preuves "<plan de preuves>.xlsx"
   ```
   Une ligne par fiche : commentaire à coller (critères regroupés « Critère 1.1.1 : … » quand la fiche en a plusieurs), fichiers à attacher (chemins dans le dossier de preuves rangé), commentaires de preuve, statut cible, case « Fait ».
3. Restituer le lot : nombre de fiches, fiches sans pièce, fiches dont un critère n'a pas encore de commentaire validé.
4. L'utilisatrice saisit sur la plateforme, coche « Fait », puis passe au lot suivant. Pour retrouver une fiche : `${CLAUDE_PLUGIN_ROOT}/skills/bcorp-platform-plan/references/platform_map.md` (code FR ↔ code plateforme, ordre des Impact Areas, filtres Année).
5. Après saisie, consigner le lot dans la mémoire projet (`project-memory`, `log_action`).
