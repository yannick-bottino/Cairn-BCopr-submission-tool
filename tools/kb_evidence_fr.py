#!/usr/bin/env python3
"""
Construit kb_evidence_fr.json : intitulés FR + exemples de preuves par sous-exigence,
issus des articles "Exemples de preuves" de la base de connaissance B Lab (FR), consultés
le 2026-10-03 via WebFetch (contenu restitué sous forme RÉSUMÉE par l'outil de lecture,
donc à re-vérifier mot à mot avant usage client).

Sources :
  MGPP  https://kb.bimpactassessment.net/fr/support/solutions/articles/43000771162
  APAC  https://kb.bimpactassessment.net/fr/support/solutions/articles/43000771161
  GEC   https://kb.bimpactassessment.net/fr/support/solutions/articles/43000771167
  AC    https://kb.bimpactassessment.net/fr/support/solutions/articles/43000771164
  DH    https://kb.bimpactassessment.net/fr/support/solutions/articles/43000771172
  TE    https://kb.bimpactassessment.net/fr/support/solutions/articles/43000771170
  JEDI  https://kb.bimpactassessment.net/fr/support/solutions/articles/43000771171
Pas d'article "Exemples de preuves" pour les Exigences de Base (EB = FR).

Exclusions volontaires : APAC2.2, APAC2.3, APAC2.4 — le résumé KB leur associe des
contenus climat (SBTi, plan de transition, transition juste) qui ne correspondent pas
aux sous-exigences GACA2.2/2.3/2.4 du PDF V2.2 (actions collectives par taille).
Incohérence probable du résumé ; non intégrées.
"""
import json, sys

MAP = {"MGPP": "PSG", "TE": "FW", "JEDI": "JEDI", "DH": "HR", "AC": "CA", "GEC": "ESC", "APAC": "GACA"}

DATA = [
 # code_fr, titre_fr, preuves (condensé)
 ("MGPP1.1", "L'entreprise établit une raison d'être publique visant à générer un impact positif significatif", "Déclaration de raison d'être publique sur le site internet ; déclaration complémentaire si le lien au modèle d'affaires / à la stratégie n'est pas explicite"),
 ("MGPP2.1", "L'entreprise dispose d'un mécanisme permettant de prendre en compte ou d'impliquer ses parties prenantes", "Documentation du mécanisme d'engagement : CR de réunions, résultats d'enquêtes, charte de comité consultatif ; preuve de représentation de chaque catégorie de parties prenantes"),
 ("MGPP2.2", "L'entreprise dispose d'une politique de gouvernance des parties prenantes", "Politique de gouvernance des parties prenantes formalisée ; PV d'approbation par l'instance dirigeante ; communication interne indiquant où trouver la politique"),
 ("MGPP2.3", "L'entreprise procède régulièrement à une analyse de matérialité", "Rapport / méthodologie d'analyse de matérialité (double matérialité ou matérialité d'impact, incluant droits humains et environnement) de moins de 36 mois ; PV de supervision ; publication (matrice + résumé méthodo)"),
 ("MGPP2.4", "L'entreprise identifie les enjeux matériels non couverts par les standards de B Lab", "Liste des enjeux matériels non couverts ; au moins un objectif SMART par enjeu, public, approuvé ; responsables désignés ; suivi annuel publié"),
 ("MGPP2.5", "L'entreprise tient compte de ses parties prenantes dans la prise de décision concernant les dividendes et les rachats d'actions", "PV du conseil montrant la prise en compte des parties prenantes ; analyses d'impact ; reporting public de l'allocation des fonds"),
 ("MGPP3.1", "L'entreprise dispose d'une procédure de réclamation accessible au public", "Lien vers le formulaire public ; procédure (éligibilité, étapes, délais, résolution) ; protection contre les représailles ; traces de communication avec le plaignant"),
 ("MGPP3.2", "L'entreprise recense les réclamations et attribue la responsabilité de leur résolution", "Registre des réclamations (tableur/logiciel) ; synthèse annuelle ; organigramme / fiche de poste du responsable ; dossiers clos (ou procédure si aucune réclamation)"),
 ("MGPP3.3", "L'entreprise dispose d'une procédure de réclamation accessible au public", "Page web de la procédure dans les langues des plaignants ; procédure documentée ; protection contre les représailles ; prévention des conflits d'intérêts"),
 ("MGPP3.4", "L'entreprise recense les réclamations et rend compte auprès de la plus haute instance de direction et des parties prenantes", "Rapport interne annuel sur les réclamations ; PV de présentation à l'instance dirigeante ; informations publiques (nombre, rejets, issues) selon les critères d'efficacité UNGP"),
 ("MGPP4.1", "L'entreprise s'est dotée de principes en matière de marketing et de communication responsables", "Principes documentés (politique interne ou code de conduite) ; preuve de diffusion aux salariés (intranet, formation, e-mail)"),
 ("MGPP4.2", "L'entreprise dispose d'une politique de marketing et de communication responsables supervisée par l'équipe de direction", "Politique formalisée approuvée ; organigramme ou RACI ; preuves de communication interne"),
 ("MGPP5.1", "La plus haute instance de direction supervise le déploiement de la raison d'être et la gestion de l'impact", "PV de l'instance dirigeante des 12 derniers mois (ordre du jour et échanges sur raison d'être, performance sociale/environnementale, gouvernance des parties prenantes)"),
 ("MGPP5.2", "Les exigences de supervision sont définies dans le cadre de référence de la plus haute instance de direction", "Documents de gouvernance / règlement intérieur du conseil formalisant la responsabilité de supervision"),
 ("MGPP5.3", "Tous les membres de l'équipe de direction ont au moins un objectif annuel lié aux performances sociales ou environnementales", "Objectifs individuels de la direction ; évaluations annuelles ; objectifs SMART alignés sur la stratégie"),
 ("MGPP5.4", "Si l'entreprise dispose d'un système de rémunération incitative pour l'équipe de direction, celui-ci intègre des objectifs de performance sociale et environnementale", "Documents liant la part variable à des objectifs d'impact ; rapports RH/rémunération (% de la rémunération) ; critères SMART"),
 ("MGPP5.5", "L'entreprise inclut des objectifs de performance sociale ou environnementale dans les évaluations de performance des managers", "Supports d'entretiens / fixation d'objectifs des managers ; extraits SIRH ; objectifs SMART revus"),
 ("MGPP6.1", "Chaque année, l'entreprise rend compte publiquement de ses performances sociales et environnementales", "Rapport annuel d'impact approuvé par l'instance dirigeante et publié en ligne (ou rapport complet tous les deux ans + mise à jour annuelle)"),
 ("MGPP6.2", "Chaque année, l'entreprise rend compte publiquement en s'appuyant sur un standard externe", "Rapport public référencé à un cadre externe (ex. GRI, ESRS), approuvé par l'instance dirigeante"),
 ("MGPP6.3", "L'entreprise évalue la capacité des collaborateurs et collaboratrices à mettre en œuvre sa stratégie sociale et environnementale", "Enquête / évaluation des salariés au moins tous les 24 mois (connaissances, préparation), participation volontaire, synthèse des résultats et suites"),
 ("APAC1.1", "L'entreprise dispose d'une politique publiquement accessible en matière de lobbying responsable", "Politique de lobbying publiée sur le site ; PV d'approbation"),
 ("APAC1.2", "L'entreprise rend publique ses positions en matière de lobbying ainsi que ses contributions politiques", "Rapport public (contributions politiques, principales positions) ; PV ; rapport annuel"),
 ("APAC1.3", "L'entreprise rend publiques ses positions en matière de lobbying et ses contributions politiques", "Rapport public (contributions politiques, principales positions) ; PV de supervision"),
 ("APAC2.1", "L'entreprise prend part à des actions collectives visant à promouvoir des impacts sociaux ou environnementaux positifs", "Confirmation écrite de l'option retenue (a-e) ; traces : mentorat, recherche externe, collaboration multipartite, plaidoyer, leadership d'opinion"),
 ("APAC2.5", "L'entreprise participe à une action collective visant à faire progresser les impacts sociaux ou environnementaux", "Confirmation écrite des options retenues (a-e)"),
 ("APAC2.6", "L'entreprise inclut les initiatives multipartites ou le plaidoyer en faveur de politiques publiques", "Document démontrant une collaboration multipartite ou un plaidoyer de politique publique parmi les actions collectives retenues"),
 ("APAC3.1", "L'entreprise dispose d'une politique en matière de fiscalité responsable et la rend publique", "Politique fiscale (autonome ou intégrée) ; approbation ; publication"),
 ("APAC3.2", "L'entreprise publie son reporting pays par pays pour chaque année fiscale", "Rapport fiscal pays par pays ; supervision par l'instance dirigeante ; publication annuelle"),
 ("GEC1.1", "L'entreprise surveille la production de déchets issus de ses activités et leur destination finale", "Politique/processus déchets ; rapports internes par filière ; bordereaux de suivi des déchets dangereux ; certificats d'élimination/recyclage"),
 ("GEC1.2", "L'entreprise surveille sa consommation énergétique", "Processus de suivi ; factures / preuves d'installations renouvelables ; rapports de répartition énergétique ; liste des sites"),
 ("GEC1.3", "L'entreprise surveille sa consommation ou son prélèvement d'eau", "Processus de suivi ; justification de la méthode de mesure ; évaluation du risque eau ; rapports de consommation"),
 ("GEC1.4", "L'entreprise identifie ses infrastructures dans les zones à risque hydrique et surveille leur consommation ou leur prélèvement d'eau", "Liste géolocalisée des sites ; recherche de risque hydrique ; consommation par zone"),
 ("GEC1.5", "L'entreprise identifie ses infrastructures situées en zone écologiquement sensible ou à proximité, et détermine si elles ont une incidence négative", "Recherche des zones sensibles ; évaluation d'impact biodiversité (< 36 mois) ; liste géolocalisée des sites"),
 ("GEC1.6", "L'entreprise surveille les conditions de bien-être animal dans ses activités", "Cartographie des opérations impliquant des animaux ; indicateurs de bien-être ; synthèse annuelle ; conformité réglementaire"),
 ("GEC1.7", "L'entreprise procède à une évaluation afin d'identifier les impacts environnementaux réels et potentiels liés à ses activités internes et à sa chaîne de valeur", "Rapport d'évaluation priorisant les enjeux environnementaux avec méthodologie (< 36 mois) ; données de performance ; engagement des parties prenantes"),
 ("GEC1.8", "L'entreprise partage publiquement ses enjeux environnementaux matériels", "Lien site / rapport annuel avec matrice de matérialité et méthodologie"),
 ("GEC2.1", "L'entreprise a mis en place une stratégie pour remédier à ses impacts négatifs réels et potentiels sur l'environnement", "Stratégie environnementale + plan de mise en œuvre ; approbation de la direction ; date d'adoption/révision (< 12 mois) ; PV de revue"),
 ("GEC2.2", "L'entreprise dispose d'un plan de transition pour la biodiversité visant à arrêter et à inverser la perte de biodiversité", "Plan de transition biodiversité ; plans d'action ; approbation ; date (< 12 mois)"),
 ("GEC2.3", "L'entreprise a mis en place une stratégie de gestion de l'eau qui limite la consommation d'eau à des seuils soutenables", "Stratégie eau ; approbation ; date (< 12 mois) ; données de contexte (autorités locales, analyses de risque)"),
 ("GEC2.4", "Les politiques et procédures de l'entreprise traitent les enjeux d'impacts environnementaux matériels", "Politique/procédure pour chaque enjeu matériel"),
 ("GEC2.5", "Les collaborateurs exerçant des fonctions pertinentes reçoivent les conseils dont ils ont besoin pour mettre en œuvre les politiques et procédures environnementales", "Supports de formation / outils ; feuilles de présence ; fiches de poste ; entretiens salariés"),
 ("GEC2.6", "L'entreprise évalue les impacts environnementaux négatifs potentiels liés à ses prospects organisationnels et aux projets envisagés, et prend les mesures d'atténuation nécessaires", "Processus d'évaluation documenté ; politique de sélection clients ; outil de filtrage ; résultats"),
 ("GEC2.7", "L'entreprise évalue les impacts environnementaux négatifs potentiels des investissements, et prend les mesures d'atténuation nécessaires", "Processus d'évaluation des investissements ; politique de sélection ; documentation de trois investissements significatifs"),
 ("GEC3.1", "L'entreprise surveille ses approvisionnements en matériaux", "Vue annuelle des flux de matières (produits / emballages) ; certifications des matières renouvelables"),
 ("GEC3.2", "L'entreprise réduit son utilisation de matériaux vierges non renouvelables", "Vue annuelle des flux de matières démontrant la réduction"),
 ("GEC3.3", "Le développement des produits de l'entreprise intègre les principes de circularité", "Confirmation écrite des options de circularité ; fiches techniques ; documentation d'écoconception ; réduction de l'usage unique"),
 ("GEC3.4", "L'entreprise comprend les infrastructures de revalorisation disponibles là où elle vend ses produits", "Analyse des infrastructures de collecte/valorisation (< 36 mois) ; note méthodologique"),
 ("GEC3.5", "L'entreprise prend des mesures pour augmenter la revalorisation de ses produits et emballages après leur fin de vie", "Programmes / partenariats ; contrats REP ; mise en œuvre dans deux pays de vente majeurs"),
 ("GEC4.1", "L'entreprise met en place des actions pour prévenir ou atténuer ses impacts environnementaux négatifs réels et potentiels", "Documentation des actions et résultats ; engagements publics ; indicateurs d'impact"),
 ("GEC4.2", "L'entreprise progresse dans sa stratégie environnementale et en évalue l'efficacité", "Stratégie ; actions/résultats ; rapport d'évaluation d'efficacité ; mises à jour ; PV de partage à la direction"),
 ("GEC4.3", "L'entreprise progresse dans son plan de transition pour la biodiversité et évalue son efficacité", "Plan biodiversité ; actions/résultats ; évaluation d'efficacité ; objectifs chaîne de valeur"),
 ("GEC4.4", "L'entreprise progresse dans sa stratégie de gestion de l'eau et évalue son efficacité", "Stratégie eau ; actions/résultats ; évaluation d'efficacité ; objectifs chaîne de valeur"),
 ("GEC4.5", "L'entreprise partage publiquement l'efficacité de sa stratégie environnementale", "Lien vers la publication (< 36 mois)"),
 ("GEC5.1", "L'entreprise travaille avec ses prestataires de biens et de services pour atteindre ses objectifs environnementaux", "Processus annuel d'identification des cinq achats significatifs ; dépenses, factures, bons de commande, évaluations d'impact"),
 ("GEC5.2", "L'entreprise prend en compte les impacts environnementaux réels et potentiels dans ses décisions d'achat", "Processus annuel d'identification des cinq achats significatifs ; dépenses, factures, bons de commande, évaluations d'impact"),
 ("GEC5.3", "L'entreprise collabore avec ses fournisseurs pour prévenir ou atténuer leurs impacts environnementaux les plus matériels", "Liste des fournisseurs prioritaires et critères ; objectifs convenus ; suivi annuel"),
 ("GEC5.4", "L'entreprise dispose d'un plan, défini dans le temps, pour assurer la traçabilité de l'origine de ses matières premières à haut risque ainsi que leurs impacts environnementaux potentiels", "Liste des matières à haut risque ; plan de traçabilité ; certifications / rapports ; % traçable par origine"),
 ("GEC5.5", "L'entreprise s'approvisionne en matières premières non issues de la déforestation", "Certifications, rapports de traçabilité, données géospatiales ; politique zéro déforestation"),
 ("GEC5.6", "L'entreprise trace une part croissante de ses matières premières à haut risque", "Évolution du % de matières traçables ; certifications / rapports"),
 ("GEC5.7", "L'entreprise collabore avec ses fournisseurs pour remédier aux impacts environnementaux liés aux matières premières à haut risque", "Objectifs convenus avec les fournisseurs ; suivi annuel"),
 ("AC1.1", "L'entreprise dispose d'un processus documenté pour mesurer chaque année ses émissions de GES sur les scope 1, 2 et 3", "Lien vers l'inventaire GES annuel public ; inventaire avec sections méthodologiques"),
 ("AC1.2", "L'entreprise fait appel à un organisme tiers indépendant pour vérifier l'inventaire annuel de ses émissions de GES", "Attestation de vérification par un organisme tiers accrédité ; certificat d'accréditation"),
 ("AC2.1", "L'entreprise dispose d'un plan d'action climatique accessible publiquement", "Lien vers le plan public ; ressources allouées ; approbation ; mise à jour < 36 mois"),
 ("AC2.2", "L'entreprise a des objectifs alignés sur les connaissances scientifiques, validés par la SBTi ou vérifiés par un organisme tiers indépendant", "Lettre de validation SBTi ou vérification tierce"),
 ("AC2.3", "L'entreprise a un plan de transition climatique pour contribuer à la neutralité carbone 2050", "Plan de transition ; ressources ; approbation ; rapport de séquestration vérifié le cas échéant"),
 ("AC2.4", "L'entreprise consulte collaborateurs et parties prenantes pour garantir transition juste", "Traces de consultation (réunions, enquêtes, focus groups) ; parties prenantes vulnérables identifiées ; intégration au plan"),
 ("AC3.1", "Si l'entreprise dispose d'un système de rémunération incitative pour l'équipe de direction, celui-ci intègre des objectifs climatiques", "Politique de rémunération ; évaluations ; données sur la part variable climat"),
 ("AC3.2", "L'entreprise utilise le plaidoyer pour soutenir l'objectif mondial de zéro émission nette 2050", "Travaux avec associations professionnelles ; engagements de politique publique ; ressources allouées"),
 ("AC3.3", "L'entreprise fait progresser son plan d'action climatique et évalue son efficacité", "Compte rendu d'avancement ; actions réalisées ; révision des objectifs ; évaluation d'efficacité"),
 ("AC3.4", "L'entreprise réalise des progrès sur son plan de transition climatique et évalue son efficacité", "Progrès vers objectifs court terme (tCO2e) ; actions ; nouveaux objectifs ; évaluation d'efficacité"),
 ("AC3.5", "L'entreprise met en place des actions pour une transition juste", "Consultations ; actions consécutives documentées"),
 ("AC3.6", "L'entreprise rend publics les progrès réalisés dans le cadre de son plan d'action climatique", "Lien vers page web / rapport public"),
 ("AC3.7", "L'entreprise publie chaque année l'état d'avancement de son plan de transition climatique", "Lien vers page web / rapport public (progrès, actions, ressources, nouveaux objectifs)"),
 ("DH1.1", "L'entreprise s'engage publiquement à respecter les droits humains", "Lien vers la page / document public d'engagement"),
 ("DH1.2", "L'entreprise dispose d'une politique publique en matière de droits humains", "Politique publique approuvée par la direction, couvrant toutes les personnes et communautés affectées"),
 ("DH2.1", "L'entreprise identifie ses enjeux majeurs en matière de droits humains", "Liste hiérarchisée des enjeux saillants, évaluations d'impact, données sociales (< 36 mois)"),
 ("DH2.2", "L'entreprise partage publiquement ses enjeux majeurs en matière de droits humains", "Lien vers la publication (enjeux + méthodologie)"),
 ("DH2.3", "L'entreprise dispose d'une stratégie pour traiter ses enjeux majeurs en matière de droits humains", "Stratégie (< 12 mois) ; approbation ; plan de mise en œuvre"),
 ("DH2.4", "L'entreprise met en œuvre sa stratégie en matière de droits humains et évalue son efficacité", "Comptes rendus d'avancement ; rapports d'efficacité ; consultations externes ; mises à jour"),
 ("DH2.5", "L'entreprise partage publiquement l'efficacité de sa stratégie en matière de droits humains", "Rapport public (< 36 mois)"),
 ("DH2.6", "Les politiques et procédures de l'entreprise couvrent ses enjeux majeurs en matière de droits humains", "Politique ou procédure pour chaque enjeu saillant"),
 ("DH2.7", "Les collaborateurs occupant des postes concernés reçoivent les orientations nécessaires pour mettre en œuvre les politiques et procédures", "Supports de formation ; présence ; fiches de poste ; entretiens"),
 ("DH3.1", "L'entreprise dispose d'un processus pour collecter, hiérarchiser et faire remonter les impacts négatifs", "Procédure de collecte/priorisation/escalade ; rôles définis"),
 ("DH3.2", "L'entreprise prévient, atténue et répare les impacts négatifs réels et potentiels", "Comptes rendus d'actions ; engagements ; rapports d'impact"),
 ("DH3.3", "L'entreprise évalue les impacts négatifs potentiels liés aux clients organisationnels et projets", "Processus d'évaluation ; politique de sélection clients ; trois clients/projets significatifs par an"),
 ("DH3.4", "L'entreprise évalue les impacts négatifs potentiels liés aux investissements", "Processus d'évaluation ; politique d'investissement ; trois investissements significatifs par an"),
 ("DH3.5", "L'entreprise réalise une évaluation d'impact sur les droits humains", "Rapport d'EIDH ; résumé public en ligne"),
 ("DH3.6", "L'entreprise met en œuvre une diligence raisonnable renforcée pour activités en zones de conflit", "Rapport sur activités en zones de conflit ; engagement des parties prenantes ; déclencheurs d'action"),
 ("DH4.1", "L'entreprise identifie les limites de sa capacité à engager et suivre ses fournisseurs", "Analyses par pays / matières premières ; évaluations de risque ; liste des limites et mesures"),
 ("DH4.2", "L'entreprise prend en compte les impacts réels et potentiels sur les droits humains dans ses décisions d'achat", "Identification annuelle de trois décisions d'achat significatives ; impacts considérés"),
 ("DH4.3", "L'entreprise prend en compte les impacts réels et potentiels sur les droits humains dans ses décisions d'achat", "Identification annuelle de cinq décisions d'achat significatives ; impacts considérés"),
 ("DH4.4", "L'entreprise collabore avec ses fournisseurs pour prévenir ou atténuer les enjeux majeurs", "Fournisseurs prioritaires ; objectifs convenus ; suivi annuel"),
 ("DH4.5", "L'entreprise renforce ses engagements au sein de ses documents d'approvisionnement", "Retours fournisseurs ; documents d'achat modifiés"),
 ("DH4.6", "L'entreprise dispose d'un plan assorti d'un calendrier pour retracer origine et impacts de matières premières à haut risque", "Liste des matières à haut risque ; plan de traçabilité ; % traçable"),
 ("DH4.7", "L'entreprise trace un nombre croissant de matières premières à haut risque jusqu'à leur origine", "Calcul du % de matières à haut risque traçables"),
 ("DH4.8", "L'entreprise collabore avec ses fournisseurs pour traiter les impacts liés aux matières premières à haut risque", "Collaboration fournisseurs ; suivi annuel"),
 ("DH4.9", "L'entreprise identifie les écarts par rapport au salaire de subsistance dans ses contrats de services", "Évaluation des contrats de services ; calcul des écarts au salaire de subsistance"),
 ("DH4.10", "L'entreprise fait référence au salaire de subsistance dans ses processus d'achat de services", "Mention du salaire de subsistance dans appels d'offres / contrats"),
 ("DH4.11", "L'entreprise dispose d'un plan pour aborder le salaire de subsistance, revenu de subsistance ou négociation collective", "Plan interne (< 12 mois) ; approbation ; mise à jour publique"),
 ("TE1.1", "L'entreprise fournit à tous les salariés un contrat de travail ou une lettre d'engagement signés", "Contrats / lettres signés ; registre du personnel ; entretiens salariés"),
 ("TE1.2", "L'entreprise applique un délai de prévenance équitable pour les salarié·es ayant des emplois du temps variables", "Politique interne ; entretiens ; communications"),
 ("TE2.1", "L'entreprise a pour politique de ne pas demander les antécédents salariaux des candidats et candidates", "Politique / procédure ; entretiens"),
 ("TE2.2", "L'entreprise informe les collaborateurs et collaboratrices de la manière dont leur salaire est déterminé et des avantages auxquels ils et elles ont droit", "Communications ; politique accessible ; bulletins de paie"),
 ("TE2.3", "L'entreprise dispose d'une grille salariale", "Grille salariale ; accès intranet ; entretiens"),
 ("TE2.4", "L'entreprise calcule son écart de salaire entre les femmes et les hommes", "Calculs détaillés ; note méthodologique"),
 ("TE2.5", "L'entreprise publie son ou ses écarts de salaires entre les hommes et les femmes", "Page web / rapport public avec méthodologie"),
 ("TE2.6", "L'entreprise élimine l'écart de salaires entre les hommes et les femmes, le réduit ou justifie les raisons", "Calculs ; justification écrite ; plan d'action"),
 ("TE2.7", "L'entreprise évalue le salaire égal pour un poste à valeur égale", "Évaluation des emplois ; méthodologie ; date ; plan correctif"),
 ("TE2.8", "L'entreprise met en œuvre des pratiques salariales équitables pour ses salarié·es les moins bien rémunéré·es", "Option retenue par site ; données de paie ; estimation du salaire de subsistance ; accords collectifs"),
 ("TE3.1", "L'entreprise possède un dispositif de représentation des salarié·es", "Documents de gouvernance ; liste des représentants ; CR de réunions"),
 ("TE3.2", "L'entreprise prend en compte les retours des collaborateurs et collaboratrices sur les décisions qui les concernent", "Communications ; ateliers / enquêtes ; entretiens"),
 ("TE4.1", "L'entreprise évalue régulièrement la culture d'entreprise", "Rapports d'enquête / ateliers (satisfaction, bien-être, appartenance, engagement, sécurité psychologique)"),
 ("TE4.2", "L'entreprise a un plan d'amélioration continue de sa culture d'entreprise", "Plan d'amélioration ; approbation ; calendrier"),
 ("TE4.3", "Les résultats des enquêtes sur la culture d'entreprise sont ventilés par identité de genre ou selon le sexe à la naissance", "Données ventilées ; mesures de protection de l'anonymat"),
 ("TE4.4", "Les résultats des enquêtes sur la culture d'entreprise sont ventilés selon un autre aspect de l'identité sociale", "Données ventilées ; justification du choix ; mesures de protection"),
 ("JEDI1.1", "L'entreprise collecte des données afin d'orienter ses actions en matière de JEDI.", "CR de discussions ou résultats d'enquête ; données ventilées (genre, niveaux, rétention, recrutement, promotion, salaires...)"),
 ("JEDI1.2", "L'entreprise collecte des données sur une identité sociale supplémentaire pour les indicateurs liés aux collaborateurs et collaboratrices.", "Questionnaires ; garanties d'anonymat ; tableaux ventilés"),
 ("JEDI2.1", "L'entreprise choisit et met en œuvre une action JEDI.", "Confirmation écrite de l'option retenue (JEDI2.a-s)"),
 ("JEDI2.2", "L'entreprise choisit ses actions JEDI et les met en œuvre.", "Confirmation écrite des options retenues et de leur catégorie"),
 ("JEDI2.3", "L'entreprise choisit ses actions JEDI sur la base des données et des retours des parties prenantes, les consigne dans un plan et les met en œuvre.", "Options retenues ; données / retours parties prenantes ; plan formalisé ; communication ; entretiens"),
 ("JEDI2.4", "L'entreprise choisit ses actions JEDI sur la base des données et des retours des parties prenantes, les consigne dans un plan et les met en œuvre.", "Idem JEDI2.3"),
 ("JEDI2.5", "L'entreprise choisit ses actions JEDI sur la base des données et des retours des parties prenantes, les consigne dans un plan et les met en œuvre.", "Idem JEDI2.3 + vue annuelle par pays/site"),
 ("JEDI2.6", "L'entreprise choisit ses actions JEDI sur la base des données et des retours des parties prenantes, les consigne dans un plan et les met en œuvre.", "Idem JEDI2.5"),
]

out = {}
for code_fr, titre, preuves in DATA:
    pre = next(p for p in sorted(MAP, key=len, reverse=True) if code_fr.startswith(p))
    out[MAP[pre] + code_fr[len(pre):]] = {"code_fr": code_fr, "titre_fr": titre, "preuves": preuves}
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "kb_evidence_fr.json", "w"), ensure_ascii=False, indent=1)
print(len(out), "entrées")
