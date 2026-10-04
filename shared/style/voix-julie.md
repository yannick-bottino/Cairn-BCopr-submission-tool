# Voix de Julie : guide de style des cellules de gap analysis B Corp (module 3)

Référence principale : gap analysis [Client A] vF (onglet « 3. Gap analysis », 175 lignes), lue cellule par cellule. Complément : gap analysis [Client B] (VF du 23/07/2026). Registre visé : le registre sharp de Julie, « straight to the point, pragmatique : c'est ma manière de fonctionner et ça plaît aux clients ».

Sources citées : [vF code] = cellule de la vF [Client A] (colonnes I Diagnostic, J Actions, R Preuves, S Commentaire auditeur, Z Justification typologie) ; [N§x] = research/03-[Client B].md ; [GA] = skill b-corp-gap-analysis-excel ; [P] = proposal-rse/references/profil.md. Les verbatim sont recopiés tels quels, coquilles comprises ; « / » marque un retour à la ligne dans la cellule ; « […] » marque une coupe. Noms de personnes remplacés par leur fonction entre crochets, montants par [montant].

## 0. Registre sharp : critères

Julie écrit dans deux registres. Le registre (a) est le sien ; le registre (b) est celui des cellules générées puis peu retouchées. On vise (a).

Critères mesurés sur la vF (cellules I et J non vides, hors « NA ») :

| Critère | (a) sharp | (b) rapport / généré |
|---|---|---|
| Longueur médiane Diagnostic (I) | 147 caractères | 565 caractères |
| Longueur médiane Actions (J) | 268 caractères | 455 caractères |
| Puces « > » dans I | 0 (verdict en 1 ou 2 phrases) | 2 et plus, une par source croisée |
| Items numérotés dans J | 0 à 2 | 3 et plus |
| Marqueurs Julie dans J (« suffit », « --> », « ATTENTION », « Si … : », « OU », « + », question directe) | 19 cellules sur 29 | 12 sur 54 |
| Formules de remplissage (« en fournissent le cadre », « Aucune action de la feuille de route… », source en en-tête systématique) | 0 | 30 cellules J sur 54 |

Une cellule est sharp si elle tient en 300 caractères sans formule de remplissage, ou en 500 caractères avec un marqueur Julie (option minimale, piège, conséquence, branche conditionnelle).

Répartition par ligne (95 lignes à contenu substantiel ; les 80 autres sont NA ou vides) : 37 sharp, 58 rapport.

| Impact Area | Sharp | Rapport |
|---|---|---|
| TE | 13 | 4 |
| GEC | 12 | 9 |
| DH | 6 | 3 |
| APAC | 2 | 2 |
| JEDI | 1 | 3 |
| MGPP | 3 | 13 |
| EB | 0 | 21 |
| AC | 0 | 3 |

Sections où le sharp domine : TE 1.1, TE 1.2, TE 2.2, TE 4.1 (6 lignes sur 6), GEC 1.1, GEC 1.6, DH 1.2, DH 2.1, DH 3.1. Les EB, MGPP 1.1 à 2.1, GEC 1.7 et AC 2.1 sont le registre (b) : c'est ce qu'il faut raccourcir.

Six traits du registre sharp :
1. Verdict d'abord, en une phrase, souvent par le droit français : « Le bulletin de paie français est […] normalisé depuis 2018 […] -> le critère est donc satisfait en pratique » [vF TE 2.2.2].
2. Une action, une preuve : « Fournir un bulletin de paie anonymisé » [vF TE 2.2.2].
3. Documenter plutôt que créer : « le travail restant consiste à le documenter, pas à le créer » [vF TE 4.1.1].
4. Mutualiser : « Une seule enquête peut couvrir cette sous-exigence et l'exigence MGPP6.3 […], ce qui évite une seconde campagne » [vF TE 4.1.2].
5. Brancher selon la réponse : « Si un site ressort en zone de risque : … / Sinon : rédiger une note datée concluant à l'absence de site en zone de risque » [vF GEC 1.4.4].
6. Ligne feuille de route seulement si elle apporte quelque chose. Les lignes sharp de TE et GEC n'en ont souvent pas ; les lignes générées en ajoutent une par réflexe.

## 1. Principes

1. Preuve d'abord. Chaque cellule répond à une seule question : qu'est-ce qui prouve, qu'est-ce qui manque pour prouver. Une intention, un projet ou une feuille de route ne sont pas des preuves.
2. Sourcer avant d'affirmer, sans en-tête mécanique. Le document et sa date quand ils portent le constat ; « Aucun élément dans les documents disponibles. » quand rien n'est trouvé (35 cellules de la vF).
3. Option minimale suffisante, dite noir sur blanc : « Un CR de réunion ou une signature datée sur le document suffit. » [vF AC 2.1.1]. Dire aussi ce qu'il ne faut pas faire : « Ne pas limiter la portée aux salariés de [Client A] » [vF DH 1.2.4].
4. Trancher. Une reco, pas un menu ; « OU » seulement entre deux options équivalentes. « ATTENTION : » pour un piège, « --> » pour la conséquence.
5. Prêt à l'emploi. Verbes à l'infinitif, texte d'attestation ou de clause déjà rédigé après « stipulant que : » (11 cellules J).
6. Code du critère, numéro d'action et nom de document cités, jamais inventés.
7. Sobre. Phrases courtes, présent, 3e personne. Ni Markdown, ni gras, ni emoji, ni adjectif d'emphase.
8. Sans blâme. L'écart est un écart entre référentiels, pas une faute des équipes.

## 2. Grammaire par type de cellule

### 2.1 Diagnostic & gap analysis (I)

Ordre :
1. Verdict ou constat sourcé, en une phrase.
2. Faits complémentaires en puces « > », seulement s'ils changent la conclusion (2 au plus en registre sharp).
3. « Manquant : » + une phrase (23 cellules).
4. « Question à poser à [fonction] : » + la question, si une info bloque la conclusion (18 cellules). Forme la plus nette : « Question à poser à la direction financière : un actionnaire détient-il plus de 50 % du capital ? » [vF EB 1.5.3]. Destinataire par sa fonction, jamais par son prénom ; pas de « Question : » nu ni de destinataire placé après les deux-points.
5. NA : « Conclusion provisoire : sous-exigence réputée inapplicable » (+ réserve si besoin : « , sous réserve de confirmation RH. » [vF TE 1.2.1]).

Longueur cible : 150 à 300 caractères ; 600 au plus quand plusieurs sources se contredisent (EB 1.4.1).

Verbatim sharp :
- [vF TE 1.1.1] « Le cadre contractuel français (Code du travail) impose déjà par défaut des contrats écrits et signés pour les CDI / CDD, avec toutes les mentions obligatoires (a-c) demandées par FW 1.1.1. »
- [vF TE 1.1.3] « Aucun élément dans les documents disponibles. / La remise d'un exemplaire signé au salarié relève de la pratique courante en France, mais aucune pièce du dossier ne l'atteste ni ne décrit le circuit de remise »
- [vF TE 2.2.2] « Aucun élément dans les documents disponibles / Le bulletin de paie français est mensuel et normalisé depuis 2018 : il fait apparaître le salaire de base, les autres composantes de la rémunération et l'ensemble des cotisations et retenues, regroupées par risque -> le critère est donc satisfait en pratique »
- [vF TE 4.1.2] « Le NPS collaborateur mesure une intention de recommandation ; rien n'indique qu'il couvre deux des six thèmes exigés (satisfaction, bien-être, sentiment d'appartenance, se sentir engagé, être engagé, sécurité psychologique) / - L'action S.2.2 vise un sondage annuel sur la qualité de vie au travail, ce qui ouvrirait le thème du bien-être, mais sa valeur de référence est à zéro dans la roadmap: ce sondage n'a pas encore eu lieu. »
- [vF TE 4.1.5] « Deux campagnes consécutives, 2024 et 2025, sont citées par le diagnostic [co-prestataire], ce qui établit une pratique annuelle. / L'action S.2.1 va plus loin en visant un relevé trimestriel / Manquant : la récurrence n'est formalisée dans aucun document de cadrage, »
- [vF GEC 1.6.1] « [Client A] ne détient, ne transporte ni n'abat d'animaux. Conclusion provisoire : sous-exigence réputée inapplicable »

Contre-exemple (b) [vF EB 1.4.1, extrait] : « Aucun élément dans les documents disponibles sur un circuit de validation des données transmises à B Lab. / > Le PV de constatation DDPP de Paris (contrôle du 05.05.2025) relève des chiffres publiés non conformes […] / > Effectif : [effectif] (bilan carbone [prestataire carbone], août 2024-août 2025) contre environ 100 personnes […] / > Part des recharges en volume 2025 : 12 % […] / > Échéance B Corp : « fin 2026 » […] ». Moins Julie : cinq puces et 1 000 caractères pour une conclusion qui tient en une ligne (« les chiffres divergent, aucun valideur nommé »).

### 2.2 Actions recommandées (J)

Ordre :
1. Verbe à l'infinitif (Récupérer, Fournir, Rédiger, Faire confirmer par écrit, Ajouter, Documenter). Une action seule n'a pas de numéro ; au-delà, « 1. 2. 3. ».
2. La preuve à garder en fin d'item (« et archiver une copie comme preuve »).
3. L'option minimale (« … suffit »), le piège (« ATTENTION : »), la conséquence (« --> »), la branche (« Si … : » / « Sinon : »).
4. Attestation ou clause : « Rédiger une attestation signée par [fonction] stipulant que : « … » », texte prêt.
5. Rattachement feuille de route, seulement s'il apporte une information : « L'action X porte… ; aucune ne couvre… » quand une action proche existe sans couvrir le point ; « Aucune action de la feuille de route ne couvre ce point. » quand c'est utile au client de le savoir. Pas de « -> Les actions … en fournissent le cadre. » par réflexe (26 lignes « -> » dans la vF, presque toutes en registre b).

Longueur cible : 1 à 3 items, 100 à 300 caractères.

Verbatim sharp :
- [vF TE 4.1.3] « Ajouter au mail du questionnaire 2026  la mention explicite du caractère facultatif de la participation, et archiver une copie comme preuve »
- [vF TE 2.2.2] « Fournir un  bulletin de paie anonymisé »
- [vF MGPP 4.2.3] « Nommer un membre du CODIR responsable du respect de la politique, nomination stipulée dans le CR de CODIR qui approuve la politique. »
- [vF TE 3.2.3] « 1.Instituer une restitution systématique après chaque consultation : résultats, décisions retenues, décisions écartées et motifs / 2. Le team meeting hebdomadaire et la Team Vision trimestrielle sont les canaux existants  --> il suffit d'y inscrire ce point à l'ordre du jour et d'en garder une trace écrite »
- [vF TE 4.1.1] « Récupérer les campagnes de NPS collaborateur  2024, 2025  et vérifier que les questions portent sur le vécu des salariés, et pas seulement sur leur intention de recommander l'entreprise. Les actions S.2.1 et S.2.2 couvrent le dispositif : le travail restant consiste à le documenter, pas à le créer. + fournir les résultats consolidés »
- [vF AC 2.1.1, extrait] « 2. Le plan doit être approuvé formellement par la direction. Un CR de réunion ou une signature datée sur le document suffit. […] / ATTENTION : mentionner que l'entreprise s''engage à soutenir l'ambition mondiale de limiter le réchauffement climatique à 1,5°C -->pas nécessaire d'aligner le plan carbone sur une trajectoire 1.5°C »

Attestation type [vF EB 1.2.1] : « Rédiger une attestation signée par la direction financière stipulant que : « [Client A] ne réalise aucun chiffre d'affaires dans les secteurs exclus par B Lab (énergies fossiles, jeux d'argent, pornographie, prisons et centres de détention, tabac, armement). » Joindre la ventilation du chiffre d'affaires par gamme de l'exercice de référence. »

Rattachement utile [vF TE 2.2.1] : « L'action S.2.4 porte le volet avantages sociaux et l'action G.4.7 l'étude du partage de la valeur ; aucune ne couvre les mécanismes de fixation des salaires »

Contre-exemple (b) [vF GEC 1.7.2, fin] : « -> Les actions E.6.1, G.2.2, G.2.5 et E.5.1 en fournissent le cadre ; la cartographie globale des risques ESG confiée à [co-prestataire] porte le livrable. » Moins Julie : quatre numéros d'action énumérés sans dire ce qui reste à faire, après trois items déjà longs.

À ne pas faire : laisser une question ouverte dans J (« Compris dans la cartographie des risques d'[co-prestataire] ? ») ; la poser dans I en « Question à poser ». Recopier le critère B Lab en liste a) b) c) dans l'action. Nommer un porteur par son prénom (« --> par [prénom] ») : la colonne Responsable existe.

### 2.3 Preuves attendues (R)

Ordre : « Preuves attendues : » (ou « Preuve attendue : »), ligne vide, puis une pièce par tiret « - », chacune avec sa forme vérifiable (datée, signée, URL, capture). NA : « Aucune pièce attendue. » + le motif.

Longueur cible : 1 à 3 tirets (médiane vF : 165 caractères).

Verbatim sharp :
- [vF DH 1.2] « Preuves attendues : / - Politique droits humains publiée sur le site de [Client A], datée et versionnée / - Extrait de CR approuvant le texte / - URL et capture de la page publique »
- [vF GEC 1.4.4] « Preuves attendues : / - Extraction de l'outil de risque hydrique / - Relevés de consommation en mètres cubes des sites concernés ou note de conclusion négative datée »
- [vF GEC 1.3.3] « Preuve attendue : / - Note de justification du choix de l'indicateur eau, validée en comité RSE »
- [vF EB 1.2.3] « Aucune pièce attendue. / - La non-applicabilité se déclare directement sur la plateforme / - Justification : code APE et description d'activité »
- [vF JEDI 2.c] « Sans objet si l'option n'est pas retenue. / - Verser au dossier la note d'arbitrage qui justifie d'avoir écarté cette branche »
- [vF EB 1.4.3] « Preuves attendues : / - Agreement for B Corp Certification signé et daté »

À ne pas faire : six pièces dont trois « à produire » (EB 1.3.1) ; un paragraphe sans tirets (AC 2.1.2) ; des chevrons « > » à la place des tirets (TE 3.2).

### 2.4 Commentaire soumission dossier pour l'auditeur (S)

Ordre :
1. Phrase d'affirmation à la 3e personne, au présent ou au passé composé, terminée par « : » quand des puces suivent.
2. Faits datés et chiffrés, pointeurs précis (document, page, date).
3. Si plusieurs justifications : puces « - », une par ligne.
4. Clôture des sous-critères quand c'est vrai : « Les N critères a/b/c sont couverts. » [N§3.3].
5. Action en cours, si elle existe : « - En cours de déploiement : [objet], [jalon : date ou échéance], porté par [fonction] » (voir §4 règle 2).
6. Dernière ligne : « - Pièces jointes au dossier : … » (la vF écrit aussi « - Pièces jointes : »).
NA : « NA. » + le motif en une phrase.

Longueur cible : 250 à 500 caractères (médiane vF : 482).

Verbatim sharp :
- [vF TE 4.1.1] « [Client A] mesure chaque année la perception de ses collaborateurs par un NPS interne, en progression entre 2024 et 2025. / - Mesure portée par l'action S.2.1 (relevé trimestriel, cible > 35 %), complétée par l'action S.2.2 (sondage annuel sur les attentes en matière de qualité de vie au travail) / - Pièces jointes : questionnaire et résultats »
- [vF EB 1.2.1] « L'intégralité du chiffre d'affaires de [Client A] provient de la conception et de la commercialisation de produits cosmétiques (code APE 4645Z) : / - Aucune part du CA ne provient des industries listées : production d'énergies fossiles, jeux d'argent, pornographie, établissements pénitentiaires, tabac, armement / - [Client A] n'est pas une société de services financiers et ne gère aucun actif pour compte de tiers / - Pièces jointes : attestation de la direction financière, comptes annuels »
- [vF EB 1.1.1] « [Client A] est une société commerciale française en activité depuis plus de douze mois : / - Chiffre d'affaires : [montant] sur l'exercice [exercice], pour [effectif] ETP / - Activité : conception et vente de produits cosmétiques sur un marché concurrentiel / - Pièces jointes au dossier : extrait Kbis, statuts en vigueur, comptes annuels »
- [vF GEC 1.7.3] « Les travaux d'évaluation environnementale de [Client A] datent tous de 2026 : / - Bilan carbone 2024-2025 remis en avril 2026 ([prestataire carbone]) / - Diagnostic durabilité et matrice de matérialité de septembre 2026 ([co-prestataire]) / - Feuille de route RSE V2 du 31 mars 2026 / La consolidation de ces travaux en une évaluation unique datée est engagée. »
- [vF MGPP 3.2.3] « [Client A] recense les réclamations de sa clientèle et les suit par thèmes dans le cadre de son dispositif qualité, adossé à la cosmétovigilance et à la procédure de rappel produit. / - Le suivi est actif et donne lieu à une classification des motifs / - L'extension du recensement aux autres parties prenantes et la production d'un reporting consolidé font l'objet de l'action G.4.9 de la feuille de route RSE, dont la cible est la totalité des remontées traitées »
- [vF GEC 1.2.1] « [Client A] a réalisé un bilan carbone sur les trois scopes pour la période août 2024 à août 2025 ([prestataire carbone], avril 2026). / - Les consommations énergétiques du siège (électricité) et de la flotte de véhicules (carburant) ont été collectées en données physiques et servent de base au scope 1 et au scope 2 / - Le tableur de collecte est disponible / - La reconduction annuelle de la mesure est en cours de mise en place »

- [GA, [Client B] MGPP 1.1, clôture des sous-critères] « La raison d'être de [Client B] couvre les 4 critères a/b/c/d : / - Figure dans les statuts signés par le Président […] / - Publiée publiquement sur le site […] / - Reprise dans la présentation officielle de l'agence (même document, p.6) »

Les exemples GEC 1.7.3, MGPP 3.2.3 et GEC 1.2.1 ont la bonne longueur mais leur dernière ligne « en cours » n'a ni jalon ni porteur. Forme attendue : « - En cours de déploiement : reconduction annuelle de la mesure énergie, prochaine mesure sur l'exercice [échéance], portée par [fonction] ».

Contre-exemple (b) [vF AC 2.1.2, extrait] : « [Client A] a réalisé son bilan carbone 2024-2025 sur les trois scopes selon la méthode GHG Protocol ([prestataire carbone], avril 2026) : [valeur] tCO2e, dont 98 % de scope 3. Un plan d'action climat en quatre piliers stratégiques […] a été défini de façon SMART […]. La trajectoire chiffrée et son approbation formelle sont en cours de finalisation. » Moins Julie : un bloc de 700 caractères sans puces ni pièces jointes, et un « en cours » sans jalon ni porteur.

À ne pas faire : mentionner un manque ; recopier le diagnostic ; nommer Anchor, le [co-prestataire] ou une personne par son prénom (la vF le fait en MGPP 5.1 : remplacer par les fonctions) ; garder un tiret cadratin (la vF en a deux, EB 1.1.2 et EB 1.3.1).

### 2.5 Justification de la typologie (Z)

Grammaire : une phrase nominale, objet concret d'abord, puis « : » et ce qui fait la typologie (aucune action FDR, ce que le CODIR arbitre). Médiane vF : 62 caractères.

Verbatim (un par typologie) :
- Correctif mineur / pièce à produire [vF EB 1.2.1] : « Attestation de la direction financière sur la ventilation du CA. »
- Process à mettre en place [vF GEC 1.1] : « Registre déchets des sites propres : aucune action FDR. »
- Document structurant [vF DH 1.2] : « Politique droits humains publique : aucune action FDR dédiée. »
- Chantier majeur – arbitrage CODIR [vF AC 2.1] : « Plan climat public : trajectoire en intensité ou en absolu à arbitrer. »
- NA (libellé fixe, 60 lignes) : « Critère non applicable (option non retenue ou hors périmètre). »

À ne pas faire : reformuler le diagnostic ; justifier par l'importance (« enjeu clé pour la certification »).

## 3. Lexique et ponctuation

Formules bannies [P] : « j'espère que vous allez bien » et formules supplicantes ; « je me permets » ; « n'hésitez pas à me contacter » ; « game-changer », « best-in-class », « value proposition ». Pas de « OFFERT ». Pas de jargon américanisé (« async »).

Tics IA à éviter :
- Openers : « Voici ce que / pourquoi / comment », « Il s'avère que », « Force est de constater », « Il convient de noter que », « Dans ce contexte », « En ce qui concerne ».
- Emphase : « essentiel », « crucial », « clé » ; « vraiment », « clairement », « fondamentalement ».
- Jargon : « levier » ou « enjeu » sans les nommer, « approche holistique », « s'inscrire dans », « embarquer », « valeur ajoutée ».
- Formules de remplissage de la vF générée : « en fournissent le cadre », « Aucun élément dans les documents disponibles » suivi de quatre puces qui en apportent.

Ponctuation :
- Tirets cadratins et demi-cadratins en incise interdits partout. Seule exception : le libellé fixe « Chantier majeur – arbitrage CODIR ».
- Tirets « - » en début de puce (Preuves, Commentaire auditeur) ; « > » pour les faits du Diagnostic ; « --> » pour une conséquence (Diagnostic, Actions), jamais dans le Commentaire auditeur.
- « ATTENTION : » est la seule majuscule d'insistance admise.
- Pas de Markdown, de gras, d'emoji. Un espace avant « : ». Pas de « 3.. », de « 1.. », de double espace, de « ° » abréviatif. Les coquilles de Julie (« 1.Instituer », double espace, « s''engage ») sont citées en verbatim, pas imitées.
- Codes au format de la vF : sigle français + espace + numéro (« MGPP 3.1 », « JEDI 2.g.1 »).

## 4. Règles de fond

1. Ne jamais transformer une intention en preuve. Une action FDR, un objectif, un support de CODIR « à venir » restent des intentions ; le niveau de conformité ne monte pas.
2. Commentaire auditeur : jamais de manque. Une action engagée peut figurer en « en cours de déploiement », toujours avec son jalon (date ou échéance) et son porteur (fonction, jamais de prénom). Sans jalon ni porteur connus, la ligne ne figure pas. Dans la vF, aucune des six lignes « en cours » n'a les deux (MGPP 1.1.1, MGPP 2.1.3, EB 1.3.1, GEC 1.2.1, GEC 1.7.1, AC 2.1.2) : seule TE 3.2.1 nomme un porteur (« pilotée par la direction des ressources humaines »).
3. Ne jamais inventer un code B Corp, un numéro d'action FDR, un nom de document, une page, une date ou une URL. Un rattachement FDR se fait sur le texte de l'action, pas sur des mots-clés.
4. Option minimale : la forme de preuve la plus légère que le critère accepte (CR ou signature datée, déclaration courte, attestation d'une page, pièce existante comme le bulletin de paie).
5. Le NA se justifie et se prouve ; « Conclusion provisoire » tant que la plateforme n'a pas confirmé.
6. Rappeler les règles B Lab qui piègent, en une ligne : « Attention : B Lab écarte explicitement la charte fournisseur comme politique droits humains. » [vF DH 1.2] ; « Les critères de sélection fournisseurs ne suffisent pas : B Lab attend cinq décisions d'achat réelles documentées » [vF GEC 5.2.1].
7. Les colonnes F et G (critère, clarification) sont recopiées du référentiel, jamais réécrites.
8. Les personnes sont désignées par leur fonction (Présidente, direction financière, Qualité, réglementaire & claims, RH), dans toutes les colonnes.

## 5. Points encore ouverts (à demander à Julie)

1. Clôture « Les N critères a/b/c sont couverts. » ([Client B]) : à garder avec « Pièces jointes au dossier » dans [Client A], ou non ? Décision en attente ; la vF ne l'emploie dans aucune cellule.
2. L'aveu cadré [Client B] TE 4.1.3 (« n'indiquent pas explicitement que… mais… ») est-il compatible avec « jamais de manque » ?
3. Forme unique pour la dernière ligne : « Pièces jointes au dossier : » (2 cellules) ou « Pièces jointes : » (4 cellules).
4. La colonne W (Commentaires) est vide dans la vF : y a-t-il des annotations de Julie ailleurs (versions intermédiaires) qui serviraient de paires avant/après ?
5. Validation des longueurs cibles : Diagnostic 150-300 caractères, Actions 1-3 items, Preuves 1-3 tirets, Commentaire 250-500 caractères.
