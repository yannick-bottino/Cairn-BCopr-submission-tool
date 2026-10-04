# Carte de app.bcorporation.net (relevé terrain du 17-18/09/2026, anonymisé)

Source : skill b-corp-platform-navigation. **Décision du 04/10/2026 : le plugin n'automatise pas le navigateur.** Les méthodes de clic décrites plus bas sont un relevé historique : ne pas les exécuter. Cette fiche sert à guider la saisie manuelle (où cliquer, quel code, quel statut).


# Naviguer sur la plateforme B Corp (app.bcorporation.net)

Ce skill documente le fonctionnement du tracker de certification B Lab Standards v2.2 ("Exigences de performance"), testé et validé en conditions réelles sur le compte [Client B] ([Client B]) les 17-18/09/2026.

## Pré-requis

La session utilise le navigateur intégré (Claude_Browser). Le compte est déjà authentifié dans les cas testés. Si une page de connexion apparaît, s'arrêter et demander à l'utilisateur de se connecter — ne jamais saisir d'identifiants.

Si le domaine n'a pas encore été autorisé pour le navigateur, appeler `request_access` avec `scope: "site"` sur `https://app.bcorporation.net` avant de continuer.

**Presse-papier** : une interaction sur le site (probablement un bouton "copier" caché) a déclenché un accès au presse-papier système pendant les tests. Le site peut donc modifier le presse-papier de l'utilisateur de son propre chef — ne jamais supposer que son contenu vient d'une action de Claude, et prévenir l'utilisateur si on lui demande de coller quelque chose juste après avoir navigué ici.

## Cartographie du site

### Page hub "Exigences de performance"

URL de base : `/fr-fr/company/<company_id>/standards/assessment/<assessment_id>?role=team-leader` (accessible via Évaluation → Exigences de performance). Elle affiche 7 cartes, une par Impact Area, chacune menant à une page de catégorie dédiée.

### Table de correspondance Impact Area ↔ préfixe de code

**Piège fréquent : le Code de l'Excel (ex. "APAC 1.1") ne correspond pas littéralement au code affiché sur le site (ex. "GACA 1.1").** Le nom français long (utilisé dans l'Excel, colonne A "Impact Area" et colonne D "Code") et le préfixe court affiché sur le site (dans le titre de chaque fiche et les codes d'exigence) suivent une correspondance fixe à connaître par cœur plutôt qu'à deviner :

| Impact Area (Excel / nom long site) | Préfixe court (site) |
|---|---|
| Mission et gouvernance des parties prenantes (MGPP) | PSG |
| Travail équitable (TE) | FW |
| Justice, équité, diversité et inclusion (JEDI) | JEDI (identique) |
| Droits humains (DH) | HR |
| Action climatique (AC) | CA |
| Gestion environnementale et circularité (GEC) | ESC |
| Affaires publiques et action collective (APAC) | GACA |

Le titre d'une fiche affiche toujours les deux, ex. "Mission et gouvernance des parties prenantes 1.1 (PSG1.1)" ou "Affaires publiques et action collective 1.1 (GACA1.1)". Pour retrouver une fiche à partir d'un Code Excel, convertir d'abord via cette table plutôt que de chercher le préfixe Excel tel quel sur le site.

### Filtre "Année" et exigences pluriannuelles

Chaque page de catégorie a un bouton dropdown "Année" en haut à droite. Valeurs observées : "Tous", "Année 0", "Année 3", "Année 5". Sur le compte testé, "Année 3" et "Année 5" sont verrouillées (icône cadenas, grisées, non cliquables) — probablement débloquées plus tard dans le cycle de certification, une fois les jalons précédents atteints. Ça correspond aux dossiers "Année 3" / "Année 5" vus dans l'arborescence locale de preuves du client pour JEDI : certains sous-items ne deviennent pertinents/à documenter qu'à ces échéances.

Un toggle "Développer tout" à côté du filtre Année déplie/replie d'un coup toutes les descriptions courtes de la page.

### Vue liste vs fiche détaillée

Sur la page de catégorie, chaque ligne d'exigence a déjà, sans ouvrir "Voir les détails" : le code, une description courte, une pastille d'année (ex. "Y0"), un mini-dropdown de statut, une icône calendrier (date d'échéance) et une icône silhouette (assignee). **Pour changer uniquement le statut, c'est utilisable directement depuis la liste** (plus rapide que d'ouvrir la fiche). En revanche, ajouter ou lire un commentaire, voir le détail des critères de conformité, ou attacher une preuve nécessite d'ouvrir la fiche complète via "Voir les détails".

### Navigation entre catégories

En bas de chaque page de catégorie, des liens "Précédent:" / "Suivant:" permettent de passer à la catégorie suivante dans un ordre fixe : MGPP → TE → JEDI → DH → AC → GEC → APAC (la dernière n'a pas de "Suivant", revenir à la page hub pour recommencer ou changer de catégorie directement).

### Catégories à structure "menu à choix" (JEDI et APAC/GACA)

Contrairement aux autres catégories où chaque sous-exigence numérotée est obligatoire, **JEDI et APAC (GACA)** ont des exigences qui fonctionnent comme un menu : une exigence numérotée (ex. "JEDI 2", "GACA 2") regroupe plusieurs sous-items lettrés parmi lesquels l'entreprise choisit lesquels mettre en œuvre, plutôt que de devoir tous les remplir :
- JEDI 2 : sous-items 2.a à 2.s, chacun tagué par phase ("[Socle de base]", "[Sur le lieu de travail]", "[Au-delà du lieu de travail]") — ces tags indiquent à quel stade de maturité JEDI le sous-item est pertinent, et recoupent les échéances Année 3 / Année 5 mentionnées plus haut.
- GACA 2 : sous-items 2.1a à 2.1e.

En pratique, si l'Excel ne mentionne qu'une partie des lettres (ex. seulement JEDI 2.a et 2.g), c'est normal et attendu — ne pas chercher à documenter les lettres non retenues par le client sans confirmation.

## Parcours pour ouvrir une fiche

1. Nav du bas/haut → "Évaluation" → "Exigences de performance" (ou directement si déjà sur cette page).
2. Choisir la catégorie (Impact Area) concernée, la liste des sous-exigences apparaît avec leur Statut courant ("Non démarré", etc.).
3. Utiliser `find` sur le Code recherché (converti via la table ci-dessus si besoin, ex. "GACA 1.1" pour "APAC 1.1") pour localiser son bloc, puis cliquer le bouton "Voir les détails" associé (les refs "Voir les détails" sont nombreuses sur la page — bien vérifier qu'on clique celui du bon bloc, pas le premier de la liste).

## Structure d'une fiche d'exigence

- **Critères de conformité X.X.X** : texte de référence B Lab, lecture seule.
- **Commentaires** (onglet, avec zone de texte + bouton "Envoyer") : commentaire interne à l'équipe ("Les commentaires ne sont visibles que dans l'espace de travail de votre équipe"). C'est ici que va le texte de la colonne Q de l'Excel, reformaté pour la lecture humaine (voir skill `b-corp-gap-analysis-excel`, section "Mise en forme du commentaire").
- **Propriétés** : Statut (dropdown), Date d'échéance, Assignee, Année.
- **Preuve** : par critère de conformité, un bouton "Attacher une preuve".

## Modifier le Statut

Options du dropdown : "Non démarré", "En cours", "Terminé : Preuve Prêt" (pas d'autre option constatée).

**Règle validée avec la cliente : toujours choisir "En cours" lors d'une mise à jour automatisée, jamais "Terminé : Preuve Prêt".** Cette dernière option affirme que la preuve est jointe ; c'est la cliente qui la sélectionne elle-même, à la main, une fois le fichier réellement déposé sur la fiche. Ne passer outre cette règle que si l'utilisateur le demande explicitement pour un cas précis.

Comportement UI à connaître : le dropdown est un vrai toggle — cliquer dessus une fois l'ouvre, un clic "perdu" ou une lecture de page (`read_page`) juste après peut le refermer avant l'interaction suivante. Méthode fiable :
1. `computer` action `left_click` sur les coordonnées du bouton dropdown (pas besoin de ref).
2. `computer` action `screenshot` pour confirmer que les 3 options sont visibles.
3. `computer` action `left_click` sur les coordonnées de l'option voulue (les refs obtenus par `find`/`read_page` juste avant peuvent déjà être stale — préférer les coordonnées lues sur le screenshot qui vient d'être pris).
4. Revérifier avec `get_page_text` que le Statut affiché a changé.

### Raccourci depuis la vue liste

Comme noté plus haut, un mini-dropdown de statut existe directement sur chaque ligne dans la page de catégorie — même comportement de toggle, même méthode de vérification, mais évite d'ouvrir la fiche complète quand seul le statut doit changer.

## Ajouter un commentaire

1. Repérer le textbox via `find` ("Tapez votre commentaire") pour obtenir sa ref.
2. Reformater le texte source (colonne Q de l'Excel) selon la règle du skill `b-corp-gap-analysis-excel` (phrase d'intro + puces "- " une par ligne de preuve/justification).
3. Utiliser `form_input` avec cette ref pour injecter le texte reformaté directement (plus fiable que de simuler la frappe ; les sauts de ligne et tirets passent correctement).
4. Cliquer le bouton "Envoyer" **par sa ref** obtenue via `read_page` juste avant le clic (un clic par simple coordonnée peut ne rien faire si le bouton a été re-rendu entre temps — observé pendant les tests).
5. Vérifier avec `get_page_text` que le commentaire apparaît désormais dans le fil, signé et daté, et correctement mis en forme (sauts de ligne et puces conservés).

### Corriger un commentaire déjà publié

Il n'existe pas d'option "Modifier" sur un commentaire posté, seulement "Supprimer le commentaire" (menu "..." à droite du commentaire, sous forme d'icône trois points — le clic peut sembler ne rien faire immédiatement, revérifier avec `read_page`/`get_page_text` après coup ; le commentaire supprimé reste visible sous la forme "<commentaire supprimé>"). Pour corriger : supprimer l'ancien, puis reposter un nouveau commentaire correctement formaté (les deux restent visibles dans l'historique, l'ancien marqué comme supprimé — ce n'est pas gênant puisque ce fil est interne).

## Champs à ne pas toucher par défaut

Date d'échéance et Assignee : ne pas les renseigner sauf demande explicite de l'utilisateur — par défaut Julie gère elle-même ces aspects et n'assigne personne d'autre.

## Limite structurelle confirmée : le dépôt de preuves n'est PAS automatisable

Le bouton "Attacher une preuve" → "Sélectionner un fichier" ouvre une **boîte de dialogue système native** (sélecteur de fichier macOS), pas un composant web. Ceci a été testé en conditions réelles, y compris avec le contrôle complet de l'ordinateur ("computer use") activé côté utilisateur :
- Les outils de navigateur (clic, lecture de page) ne voient pas cette fenêtre : elle est hors du DOM de la page.
- Même avec le contrôle total de l'écran accordé, la fenêtre appartient au processus de l'application hôte (l'app Claude elle-même), qui est exclue par construction de la liste des applications pilotables — c'est une sentinelle de sécurité, pas une question de permissions.
- **Conclusion : ne pas retenter d'activer "computer use" dans le but d'attacher un fichier sur ce site — la limite est structurelle et confirmée, pas contournable.**

L'onglet alternatif "Plateforme de documents" (choisir un document déjà présent dans le "Hub de documents" plutôt que d'en uploader un nouveau) existe dans la modale mais n'était pas cliquable/fonctionnel lors des tests, et le Hub était vide côté [Client B] — à revérifier si un jour le Hub est peuplé, mais ne pas en dépendre.

**Conduite à tenir** : Claude peut identifier la question, retrouver/désigner le bon fichier de preuve, mettre à jour le Statut (toujours "En cours") et poster le Commentaire reformaté. Le dépôt physique du fichier et le passage à "Terminé" restent des actions manuelles de l'utilisateur — le signaler clairement plutôt que de tenter un contournement.