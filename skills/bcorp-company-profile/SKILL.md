---
name: bcorp-company-profile
description: Caractérise une entreprise pour la certification B Corp et vérifie son éligibilité (exigences de base FR1, FR2, FR3 de la V2.2) : taille et secteur relevés sur la plateforme B Lab, entité qualifiée, industries exclues, exigence légale, Risk Tool. Produit le profil lu par le gap analysis et une fiche de caractérisation. Utiliser quand l'utilisatrice dit « caractérisation », « éligibilité B Corp », « questionnaire de caractérisation », « le client est-il éligible », « profil B Corp », ou démarre une mission B Corp.
---

# Caractérisation et éligibilité (module 2)

## Garde-fous

- **Taille et secteur ne se calculent jamais.** Ils viennent de la plateforme B Lab : export PDF de la page de profil / scoping, ou déclaration manuelle de l'utilisatrice. Ne jamais les déduire d'un effectif ou d'un chiffre d'affaires.
- Chaque question est rattachée à un code du référentiel (`references/questions.json`). Le texte EN des critères fait foi ; la traduction FR des questions est à relire.
- Une réponse manquante donne « À confirmer », jamais « Éligible ».
- Le verdict reste « sous réserve » : les réponses se vérifient sur pièce pendant le diagnostic.

## Étapes

1. **Source du profil.** Demander avec AskUserQuestion : l'export PDF de la page de profil B Lab du client, ou à défaut ses réponses manuelles. Avec l'export, y lire taille, secteur, industrie et, s'ils y figurent, les réponses du Risk Tool, en citant la page.
2. **Questionnaire.** Poser les questions de `${CLAUDE_PLUGIN_ROOT}/skills/bcorp-company-profile/references/questions.json` qui ne sont pas déjà couvertes par l'export, en une ou deux salves AskUserQuestion (questions fermées ; pourcentages de CA pour FR1.2). Ne pas reposer une question dont la réponse figure dans l'export ou dans le `CLAUDE.md` du client ; si une source du client contredit la réponse, le signaler.
3. **Écrire `reponses.json`** dans le dossier de travail :
   ```json
   {"client": "...", "source_profil": "Export PDF plateforme B Lab", "taille": "Medium",
    "secteur": "Wholesale/Retail", "industrie": "", "horizon": 3, "date_depot": "...",
    "co_prestataire": "", "options_retenues": [],
    "FR1.1.1.a": "oui", "FR1.1.1.b": "oui", "FR1.1.1.c": "oui", "FR1.1.2": "non",
    "FR1.2.1": 0, "FR1.2.2": 0, "FR1.2.3": 0, "FR1.2.4": "non applicable", "FR1.2.5": "non",
    "FR1.5.3": "non", "FR2.1": "non",
    "FR3.1.a": "non", "...": "...", "FR3.1.n": "non"}
   ```
4. **Évaluer** :
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/bcorp-company-profile/scripts/eligibility.py" reponses.json "<dossier de travail>"
   ```
   Produit `profil.json` (lu tel quel par `bcorp-gap-analysis`) et `fiche_caracterisation.md` : verdict, statut par exigence (Éligible, Bloquant, À confirmer, À faire, Non applicable) et motif.
5. **Restituer** : le verdict, les points bloquants d'abord, puis les « À faire » (modification des statuts, rapport public pour une filiale, Risk Tool). Pour chaque « oui » au Risk Tool, lire le fichier du standard indiqué dans la fiche et dire quelles sous-exigences s'ajoutent.
6. **Mémoire projet** : acter le profil avec `project-memory` (`create_decision`, domaine `cadrage`), en citant la source.

## Suite

`profil.json` porte `risk_tool_oui` : le gap analysis (`bcorp-gap-analysis`) ajoute alors automatiquement les sous-exigences déclenchées, marque « NA » celles qui sont remplacées, et signale celles à relire avec l'impact potentiel (colonne Clarification).
