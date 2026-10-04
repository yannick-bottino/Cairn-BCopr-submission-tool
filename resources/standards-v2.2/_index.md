# Standard B Corp V2.2 : base documentaire

Source : B Lab Standards V2.2, 20/02/2026 (PDF dans `_source/`). 184 blocs, généré par tools/build_standard_md.py.

## Mode d'emploi (LLM)

1. Chercher un bloc par son code plateforme (ex. `PSG1.1`, `JEDI2.a`, `FR3.1.a`) : fichier `<code>.md` dans le dossier de son Impact Area.
2. Un code FR (ex. `MGPP 1.1`) se convertit via la colonne Code FR ci-dessous.
3. Chaque fichier contient le texte EN verbatim : exigence, critères de conformité (`### <id>`), intent, clarifications, applicabilité.
4. Les intitulés FR et exemples de preuves viennent de la KB B Lab (traduction / résumé automatique, à relire).
5. Pour filtrer (taille, secteur, échéance), utiliser le CSV `shared/referentiel/bcorp_v2.2_requirements.csv`, qui reste la source machine ; `criteres_en.csv` donne un critère par ligne.

## [FR : Exigences de base](0-FR-exigences-de-base/_index.md)

| Code | Code FR | Intitulé | Type | Year | Lien |
|---|---|---|---|---|---|
| FR1.1 | EB 1.1 | The company meets the entity qualifications to become a B Corp. | sous_exigence | 0 | [FR1.1.md](0-FR-exigences-de-base/FR1.1.md) |
| FR1.2 | EB 1.2 | The company is not significantly involved in industries that undermine the B Lab Theory of Change. | sous_exigence | 0 | [FR1.2.md](0-FR-exigences-de-base/FR1.2.md) |
| FR1.3 | EB 1.3 | The company complies with local and national laws and regulations. | sous_exigence | 0 | [FR1.3.md](0-FR-exigences-de-base/FR1.3.md) |
| FR1.4 | EB 1.4 | The company shares accurate and complete information with B Lab. | sous_exigence | 0 | [FR1.4.md](0-FR-exigences-de-base/FR1.4.md) |
| FR1.5 | EB 1.5 | The company is transparent about its performance against the B Lab Standard. | sous_exigence | 0 | [FR1.5.md](0-FR-exigences-de-base/FR1.5.md) |
| FR2.1 | EB 2.1 | The company adopts the B Corp legal requirement in its corporate structure or governing documents. | sous_exigence | 0 | [FR2.1.md](0-FR-exigences-de-base/FR2.1.md) |
| FR2.2 | EB 2.2 | The company signs the Declaration of Interdependence and commits to the shared collective purpose of the B Corp community. | sous_exigence | 0 | [FR2.2.md](0-FR-exigences-de-base/FR2.2.md) |
| FR3.1 | EB 3.1 | The company creates a risk profile and meets any additional sub-requirements. | sous_exigence | 0 | [FR3.1.md](0-FR-exigences-de-base/FR3.1.md) |
| FR3.1.a | EB 3.1.a | [Your employees] In the past fiscal year, did the company contract more independent contractors than it has employees? | question_risk_tool | 0 | [FR3.1.a.md](0-FR-exigences-de-base/FR3.1.a.md) |
| FR3.1.b | EB 3.1.b | [Your products] In the past fiscal year, did the company generate at least 10% of its revenue from a consumer product that causes negative health impacts acknowledged by a national government or intergovernmental body? | question_risk_tool | 0 | [FR3.1.b.md](0-FR-exigences-de-base/FR3.1.b.md) |
| FR3.1.c | EB 3.1.c | [Your products] In the past fiscal year, did the company distribute a digital product that uses artificial intelligence? | question_risk_tool | 0 | [FR3.1.c.md](0-FR-exigences-de-base/FR3.1.c.md) |
| FR3.1.d | EB 3.1.d | [Your products] In the past fiscal year, did the company generate at least 10% of its revenue from selling hazardous chemicals? | question_risk_tool | 0 | [FR3.1.d.md](0-FR-exigences-de-base/FR3.1.d.md) |
| FR3.1.e | EB 3.1.e | [Your products] In the past fiscal year, did the company generate at least 10% of its revenue from any of these activities? (i) Selling single-use plastic products from virgin, non-renewable materials, manufactured either by the company or for the company. (ii) Selling single-use plastic packaging from virgin, non-renewable materials, manufactured either by the company or for the company. (iii) Selling products manufactured either by the company or for the company that were packaged in single-use plastic packaging from virgin, non-renewable materials. | question_risk_tool | 0 | [FR3.1.e.md](0-FR-exigences-de-base/FR3.1.e.md) |
| FR3.1.f | EB 3.1.f | [Your products] In the past fiscal year, did the company generate at least 10% of its revenue from selling agricultural chemicals, excluding naturally derived pesticides and fertilizers? | question_risk_tool | 0 | [FR3.1.f.md](0-FR-exigences-de-base/FR3.1.f.md) |
| FR3.1.g | EB 3.1.g | [Your operations] In the past fiscal year, did the company's own operations have potential negative impacts on the rights or lands of Indigenous Peoples? | question_risk_tool | 0 | [FR3.1.g.md](0-FR-exigences-de-base/FR3.1.g.md) |
| FR3.1.h | EB 3.1.h | [Your operations] In the past three years, has the company experienced any fatality or health and safety penalty? | question_risk_tool | 0 | [FR3.1.h.md](0-FR-exigences-de-base/FR3.1.h.md) |
| FR3.1.i | EB 3.1.i | [Your operations] In the past fiscal year, did the company manufacture or outsource the manufacturing of products made primarily from materials from extractive industries? | question_risk_tool | 0 | [FR3.1.i.md](0-FR-exigences-de-base/FR3.1.i.md) |
| FR3.1.j | EB 3.1.j | [Your operations] In the past three years, did the company’s own operations directly involve ecosystem conversion that could contribute to habitat loss, soil erosion, or loss of biodiversity? | question_risk_tool | 0 | [FR3.1.j.md](0-FR-exigences-de-base/FR3.1.j.md) |
| FR3.1.k | EB 3.1.k | [Your operations] In the past fiscal year, did the company use hazardous chemicals in its core production processes? | question_risk_tool | 0 | [FR3.1.k.md](0-FR-exigences-de-base/FR3.1.k.md) |
| FR3.1.l | EB 3.1.l | [Your operations] In the past fiscal year, did the company operate a water-intensive production in an area with water risk? | question_risk_tool | 0 | [FR3.1.l.md](0-FR-exigences-de-base/FR3.1.l.md) |
| FR3.1.m | EB 3.1.m | [Your reputation] In the past three years, has the company experienced litigations, penalties, or public allegations of forced labor in its supply chain? | question_risk_tool | 0 | [FR3.1.m.md](0-FR-exigences-de-base/FR3.1.m.md) |
| FR3.1.n | EB 3.1.n | [Your reputation] In the past three years, has the company experienced litigations, penalties, or public allegations of misleading marketing or greenwashing? | question_risk_tool | 0 | [FR3.1.n.md](0-FR-exigences-de-base/FR3.1.n.md) |

## [PSG : Mission et gouvernance des parties prenantes](1-PSG-mission-et-gouvernance-des-parties-prenantes/_index.md)

| Code | Code FR | Intitulé | Type | Year | Lien |
|---|---|---|---|---|---|
| PSG1.1 | MGPP 1.1 | L'entreprise établit une raison d'être publique visant à générer un impact positif significatif | sous_exigence | 0 | [PSG1.1.md](1-PSG-mission-et-gouvernance-des-parties-prenantes/PSG1.1.md) |
| PSG2.1 | MGPP 2.1 | L'entreprise dispose d'un mécanisme permettant de prendre en compte ou d'impliquer ses parties prenantes | sous_exigence | 0 | [PSG2.1.md](1-PSG-mission-et-gouvernance-des-parties-prenantes/PSG2.1.md) |
| PSG2.2 | MGPP 2.2 | L'entreprise dispose d'une politique de gouvernance des parties prenantes | sous_exigence | 0 | [PSG2.2.md](1-PSG-mission-et-gouvernance-des-parties-prenantes/PSG2.2.md) |
| PSG2.3 | MGPP 2.3 | L'entreprise procède régulièrement à une analyse de matérialité | sous_exigence | 0 | [PSG2.3.md](1-PSG-mission-et-gouvernance-des-parties-prenantes/PSG2.3.md) |
| PSG2.4 | MGPP 2.4 | L'entreprise identifie les enjeux matériels non couverts par les standards de B Lab | sous_exigence | 0 | [PSG2.4.md](1-PSG-mission-et-gouvernance-des-parties-prenantes/PSG2.4.md) |
| PSG2.5 | MGPP 2.5 | L'entreprise tient compte de ses parties prenantes dans la prise de décision concernant les dividendes et les rachats d'actions | sous_exigence | 3 | [PSG2.5.md](1-PSG-mission-et-gouvernance-des-parties-prenantes/PSG2.5.md) |
| PSG3.1 | MGPP 3.1 | L'entreprise dispose d'une procédure de réclamation accessible au public | sous_exigence | 0 | [PSG3.1.md](1-PSG-mission-et-gouvernance-des-parties-prenantes/PSG3.1.md) |
| PSG3.2 | MGPP 3.2 | L'entreprise recense les réclamations et attribue la responsabilité de leur résolution | sous_exigence | 0 | [PSG3.2.md](1-PSG-mission-et-gouvernance-des-parties-prenantes/PSG3.2.md) |
| PSG3.3 | MGPP 3.3 | L'entreprise dispose d'une procédure de réclamation accessible au public | sous_exigence | 0 | [PSG3.3.md](1-PSG-mission-et-gouvernance-des-parties-prenantes/PSG3.3.md) |
| PSG3.4 | MGPP 3.4 | L'entreprise recense les réclamations et rend compte auprès de la plus haute instance de direction et des parties prenantes | sous_exigence | 0 | [PSG3.4.md](1-PSG-mission-et-gouvernance-des-parties-prenantes/PSG3.4.md) |
| PSG4.1 | MGPP 4.1 | L'entreprise s'est dotée de principes en matière de marketing et de communication responsables | sous_exigence | 0 | [PSG4.1.md](1-PSG-mission-et-gouvernance-des-parties-prenantes/PSG4.1.md) |
| PSG4.2 | MGPP 4.2 | L'entreprise dispose d'une politique de marketing et de communication responsables supervisée par l'équipe de direction | sous_exigence | 0 | [PSG4.2.md](1-PSG-mission-et-gouvernance-des-parties-prenantes/PSG4.2.md) |
| PSG5.1 | MGPP 5.1 | La plus haute instance de direction supervise le déploiement de la raison d'être et la gestion de l'impact | sous_exigence | 0 | [PSG5.1.md](1-PSG-mission-et-gouvernance-des-parties-prenantes/PSG5.1.md) |
| PSG5.2 | MGPP 5.2 | Les exigences de supervision sont définies dans le cadre de référence de la plus haute instance de direction | sous_exigence | 0 | [PSG5.2.md](1-PSG-mission-et-gouvernance-des-parties-prenantes/PSG5.2.md) |
| PSG5.3 | MGPP 5.3 | Tous les membres de l'équipe de direction ont au moins un objectif annuel lié aux performances sociales ou environnementales | sous_exigence | 3 | [PSG5.3.md](1-PSG-mission-et-gouvernance-des-parties-prenantes/PSG5.3.md) |
| PSG5.4 | MGPP 5.4 | Si l'entreprise dispose d'un système de rémunération incitative pour l'équipe de direction, celui-ci intègre des objectifs de performance sociale et environnementale | sous_exigence | 3 | [PSG5.4.md](1-PSG-mission-et-gouvernance-des-parties-prenantes/PSG5.4.md) |
| PSG5.5 | MGPP 5.5 | L'entreprise inclut des objectifs de performance sociale ou environnementale dans les évaluations de performance des managers | sous_exigence | 3 | [PSG5.5.md](1-PSG-mission-et-gouvernance-des-parties-prenantes/PSG5.5.md) |
| PSG6.1 | MGPP 6.1 | Chaque année, l'entreprise rend compte publiquement de ses performances sociales et environnementales | sous_exigence | 3 | [PSG6.1.md](1-PSG-mission-et-gouvernance-des-parties-prenantes/PSG6.1.md) |
| PSG6.2 | MGPP 6.2 | Chaque année, l'entreprise rend compte publiquement en s'appuyant sur un standard externe | sous_exigence | 3 | [PSG6.2.md](1-PSG-mission-et-gouvernance-des-parties-prenantes/PSG6.2.md) |
| PSG6.3 | MGPP 6.3 | L'entreprise évalue la capacité des collaborateurs et collaboratrices à mettre en œuvre sa stratégie sociale et environnementale | sous_exigence | 3 | [PSG6.3.md](1-PSG-mission-et-gouvernance-des-parties-prenantes/PSG6.3.md) |

## [FW : Travail équitable](2-FW-travail-equitable/_index.md)

| Code | Code FR | Intitulé | Type | Year | Lien |
|---|---|---|---|---|---|
| FW1.1 | TE 1.1 | L'entreprise fournit à tous les salariés un contrat de travail ou une lettre d'engagement signés | sous_exigence | 0 | [FW1.1.md](2-FW-travail-equitable/FW1.1.md) |
| FW1.2 | TE 1.2 | L'entreprise applique un délai de prévenance équitable pour les salarié·es ayant des emplois du temps variables | sous_exigence | 0 | [FW1.2.md](2-FW-travail-equitable/FW1.2.md) |
| FW2.1 | TE 2.1 | L'entreprise a pour politique de ne pas demander les antécédents salariaux des candidats et candidates | sous_exigence | 0 | [FW2.1.md](2-FW-travail-equitable/FW2.1.md) |
| FW2.2 | TE 2.2 | L'entreprise informe les collaborateurs et collaboratrices de la manière dont leur salaire est déterminé et des avantages auxquels ils et elles ont droit | sous_exigence | 0 | [FW2.2.md](2-FW-travail-equitable/FW2.2.md) |
| FW2.3 | TE 2.3 | L'entreprise dispose d'une grille salariale | sous_exigence | 3 | [FW2.3.md](2-FW-travail-equitable/FW2.3.md) |
| FW2.4 | TE 2.4 | L'entreprise calcule son écart de salaire entre les femmes et les hommes | sous_exigence | 0 | [FW2.4.md](2-FW-travail-equitable/FW2.4.md) |
| FW2.5 | TE 2.5 | L'entreprise publie son ou ses écarts de salaires entre les hommes et les femmes | sous_exigence | 0 | [FW2.5.md](2-FW-travail-equitable/FW2.5.md) |
| FW2.6 | TE 2.6 | L'entreprise élimine l'écart de salaires entre les hommes et les femmes, le réduit ou justifie les raisons | sous_exigence | 3 | [FW2.6.md](2-FW-travail-equitable/FW2.6.md) |
| FW2.7 | TE 2.7 | L'entreprise évalue le salaire égal pour un poste à valeur égale | sous_exigence | 5 | [FW2.7.md](2-FW-travail-equitable/FW2.7.md) |
| FW2.8 | TE 2.8 | L'entreprise met en œuvre des pratiques salariales équitables pour ses salarié·es les moins bien rémunéré·es | sous_exigence | 3 | [FW2.8.md](2-FW-travail-equitable/FW2.8.md) |
| FW2.8.a | TE 2.8.a | The company pays employees a living wage. | option | 3 | [FW2.8.a.md](2-FW-travail-equitable/FW2.8.a.md) |
| FW2.8.b | TE 2.8.b | The company pays employees a collectively-bargained wage. | option | 3 | [FW2.8.b.md](2-FW-travail-equitable/FW2.8.b.md) |
| FW2.8.c | TE 2.8.c | The company calculates its living wage gap, creates a closure plan, and meets two additional criteria. | option | 3 | [FW2.8.c.md](2-FW-travail-equitable/FW2.8.c.md) |
| FW3.1 | TE 3.1 | L'entreprise possède un dispositif de représentation des salarié·es | sous_exigence | 3 | [FW3.1.md](2-FW-travail-equitable/FW3.1.md) |
| FW3.2 | TE 3.2 | L'entreprise prend en compte les retours des collaborateurs et collaboratrices sur les décisions qui les concernent | sous_exigence | 0 | [FW3.2.md](2-FW-travail-equitable/FW3.2.md) |
| FW4.1 | TE 4.1 | L'entreprise évalue régulièrement la culture d'entreprise | sous_exigence | 0 | [FW4.1.md](2-FW-travail-equitable/FW4.1.md) |
| FW4.2 | TE 4.2 | L'entreprise a un plan d'amélioration continue de sa culture d'entreprise | sous_exigence | 3 | [FW4.2.md](2-FW-travail-equitable/FW4.2.md) |
| FW4.3 | TE 4.3 | Les résultats des enquêtes sur la culture d'entreprise sont ventilés par identité de genre ou selon le sexe à la naissance | sous_exigence | 3 | [FW4.3.md](2-FW-travail-equitable/FW4.3.md) |
| FW4.4 | TE 4.4 | Les résultats des enquêtes sur la culture d'entreprise sont ventilés selon un autre aspect de l'identité sociale | sous_exigence | 3 | [FW4.4.md](2-FW-travail-equitable/FW4.4.md) |

## [JEDI : Justice, équité, diversité & inclusion](3-JEDI-justice-equite-diversite-inclusion/_index.md)

| Code | Code FR | Intitulé | Type | Year | Lien |
|---|---|---|---|---|---|
| JEDI1.1 | JEDI 1.1 | L'entreprise collecte des données afin d'orienter ses actions en matière de JEDI. | sous_exigence | 0 | [JEDI1.1.md](3-JEDI-justice-equite-diversite-inclusion/JEDI1.1.md) |
| JEDI1.2 | JEDI 1.2 | L'entreprise collecte des données sur une identité sociale supplémentaire pour les indicateurs liés aux collaborateurs et collaboratrices. | sous_exigence | 3 | [JEDI1.2.md](3-JEDI-justice-equite-diversite-inclusion/JEDI1.2.md) |
| JEDI2.1 | JEDI 2.1 | L'entreprise choisit et met en œuvre une action JEDI. | sous_exigence | 0 | [JEDI2.1.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.1.md) |
| JEDI2.2 | JEDI 2.2 | L'entreprise choisit ses actions JEDI et les met en œuvre. | sous_exigence | 0 | [JEDI2.2.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.2.md) |
| JEDI2.3 | JEDI 2.3 | L'entreprise choisit ses actions JEDI sur la base des données et des retours des parties prenantes, les consigne dans un plan et les met en œuvre. | sous_exigence | 0 | [JEDI2.3.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.3.md) |
| JEDI2.4 | JEDI 2.4 | L'entreprise choisit ses actions JEDI sur la base des données et des retours des parties prenantes, les consigne dans un plan et les met en œuvre. | sous_exigence | 0 | [JEDI2.4.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.4.md) |
| JEDI2.5 | JEDI 2.5 | L'entreprise choisit ses actions JEDI sur la base des données et des retours des parties prenantes, les consigne dans un plan et les met en œuvre. | sous_exigence | 0 | [JEDI2.5.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.5.md) |
| JEDI2.6 | JEDI 2.6 | L'entreprise choisit ses actions JEDI sur la base des données et des retours des parties prenantes, les consigne dans un plan et les met en œuvre. | sous_exigence | 0 | [JEDI2.6.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.6.md) |
| JEDI2.a | JEDI 2.a | The company commits publicly to JEDI principles. [Foundation] | option | 0 | [JEDI2.a.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.a.md) |
| JEDI2.b | JEDI 2.b | The company improves JEDI knowledge and capacity among leaders. [Foundation] | option | 0 | [JEDI2.b.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.b.md) |
| JEDI2.c | JEDI 2.c | The company reviews and updates existing policies using JEDI principles. [Foundation] | option | 0 | [JEDI2.c.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.c.md) |
| JEDI2.d | JEDI 2.d | The company’s highest governing body and executive team reflect the diversity of its community. [Foundation] | option | 0 | [JEDI2.d.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.d.md) |
| JEDI2.e | JEDI 2.e | The company carries out an equity audit. [Foundation] | option | 0 | [JEDI2.e.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.e.md) |
| JEDI2.f | JEDI 2.f | The company supports at least two employee resource or affinity groups. [Within the Workplace] | option | 0 | [JEDI2.f.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.f.md) |
| JEDI2.g | JEDI 2.g | The company implements inclusive hiring practices. [Within the Workplace] | option | 0 | [JEDI2.g.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.g.md) |
| JEDI2.h | JEDI 2.h | The company provides sponsorship and mentorship opportunities to employees. [Within the Workplace] | option | 0 | [JEDI2.h.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.h.md) |
| JEDI2.i | JEDI 2.i | The company develops and implements an inclusive language guide for internal communications. [Within the Workplace] | option | 0 | [JEDI2.i.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.i.md) |
| JEDI2.j | JEDI 2.j | The company increases its proportion of workers from underrepresented groups to reflect the diversity of its community. [Within the Workplace] | option | 0 | [JEDI2.j.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.j.md) |
| JEDI2.k | JEDI 2.k | The company provides additional types of paid leave beyond legal minimums. [Within the Workplace] | option | 0 | [JEDI2.k.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.k.md) |
| JEDI2.l | JEDI 2.l | The company’s internal communication tools meet accessibility standards. [Within the Workplace] | option | 0 | [JEDI2.l.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.l.md) |
| JEDI2.m | JEDI 2.m | The company’s website meets accessibility standards. [Beyond the Workplace] | option | 0 | [JEDI2.m.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.m.md) |
| JEDI2.n | JEDI 2.n | The company communicates its JEDI action plan and progress publicly. [Beyond the Workplace] | option | 0 | [JEDI2.n.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.n.md) |
| JEDI2.o | JEDI 2.o | The company promotes diversity among its local suppliers. [Beyond the Workplace] | option | 0 | [JEDI2.o.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.o.md) |
| JEDI2.p | JEDI 2.p | The company develops and implements an inclusive communications and ethical content guide for external communications. [Beyond the Workplace] | option | 0 | [JEDI2.p.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.p.md) |
| JEDI2.q | JEDI 2.q | The company assesses how inclusive a product or service is. [Beyond the Workplace] | option | 0 | [JEDI2.q.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.q.md) |
| JEDI2.r | JEDI 2.r | The company redesigns a product or service to be more inclusive. [Beyond the Workplace] | option | 0 | [JEDI2.r.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.r.md) |
| JEDI2.s | JEDI 2.s | The company takes part in at least one collective action to advance JEDI principles. [Beyond the Workplace] | option | 0 | [JEDI2.s.md](3-JEDI-justice-equite-diversite-inclusion/JEDI2.s.md) |

## [HR : Droits humains](4-HR-droits-humains/_index.md)

| Code | Code FR | Intitulé | Type | Year | Lien |
|---|---|---|---|---|---|
| HR1.1 | DH 1.1 | L'entreprise s'engage publiquement à respecter les droits humains | sous_exigence | 0 | [HR1.1.md](4-HR-droits-humains/HR1.1.md) |
| HR1.2 | DH 1.2 | L'entreprise dispose d'une politique publique en matière de droits humains | sous_exigence | 0 | [HR1.2.md](4-HR-droits-humains/HR1.2.md) |
| HR2.1 | DH 2.1 | L'entreprise identifie ses enjeux majeurs en matière de droits humains | sous_exigence | 0 | [HR2.1.md](4-HR-droits-humains/HR2.1.md) |
| HR2.2 | DH 2.2 | L'entreprise partage publiquement ses enjeux majeurs en matière de droits humains | sous_exigence | 3 | [HR2.2.md](4-HR-droits-humains/HR2.2.md) |
| HR2.3 | DH 2.3 | L'entreprise dispose d'une stratégie pour traiter ses enjeux majeurs en matière de droits humains | sous_exigence | 3 | [HR2.3.md](4-HR-droits-humains/HR2.3.md) |
| HR2.4 | DH 2.4 | L'entreprise met en œuvre sa stratégie en matière de droits humains et évalue son efficacité | sous_exigence | 5 | [HR2.4.md](4-HR-droits-humains/HR2.4.md) |
| HR2.5 | DH 2.5 | L'entreprise partage publiquement l'efficacité de sa stratégie en matière de droits humains | sous_exigence | 5 | [HR2.5.md](4-HR-droits-humains/HR2.5.md) |
| HR2.6 | DH 2.6 | Les politiques et procédures de l'entreprise couvrent ses enjeux majeurs en matière de droits humains | sous_exigence | 3 | [HR2.6.md](4-HR-droits-humains/HR2.6.md) |
| HR2.7 | DH 2.7 | Les collaborateurs occupant des postes concernés reçoivent les orientations nécessaires pour mettre en œuvre les politiques et procédures | sous_exigence | 3 | [HR2.7.md](4-HR-droits-humains/HR2.7.md) |
| HR3.1 | DH 3.1 | L'entreprise dispose d'un processus pour collecter, hiérarchiser et faire remonter les impacts négatifs | sous_exigence | 0 | [HR3.1.md](4-HR-droits-humains/HR3.1.md) |
| HR3.2 | DH 3.2 | L'entreprise prévient, atténue et répare les impacts négatifs réels et potentiels | sous_exigence | 3 | [HR3.2.md](4-HR-droits-humains/HR3.2.md) |
| HR3.3 | DH 3.3 | L'entreprise évalue les impacts négatifs potentiels liés aux clients organisationnels et projets | sous_exigence | 0 | [HR3.3.md](4-HR-droits-humains/HR3.3.md) |
| HR3.4 | DH 3.4 | L'entreprise évalue les impacts négatifs potentiels liés aux investissements | sous_exigence | 0 | [HR3.4.md](4-HR-droits-humains/HR3.4.md) |
| HR3.5 | DH 3.5 | L'entreprise réalise une évaluation d'impact sur les droits humains | sous_exigence | 5 | [HR3.5.md](4-HR-droits-humains/HR3.5.md) |
| HR3.6 | DH 3.6 | L'entreprise met en œuvre une diligence raisonnable renforcée pour activités en zones de conflit | sous_exigence | 3 | [HR3.6.md](4-HR-droits-humains/HR3.6.md) |
| HR4.1 | DH 4.1 | L'entreprise identifie les limites de sa capacité à engager et suivre ses fournisseurs | sous_exigence | 3 | [HR4.1.md](4-HR-droits-humains/HR4.1.md) |
| HR4.2 | DH 4.2 | L'entreprise prend en compte les impacts réels et potentiels sur les droits humains dans ses décisions d'achat | sous_exigence | 0 | [HR4.2.md](4-HR-droits-humains/HR4.2.md) |
| HR4.3 | DH 4.3 | L'entreprise prend en compte les impacts réels et potentiels sur les droits humains dans ses décisions d'achat | sous_exigence | 0 | [HR4.3.md](4-HR-droits-humains/HR4.3.md) |
| HR4.4 | DH 4.4 | L'entreprise collabore avec ses fournisseurs pour prévenir ou atténuer les enjeux majeurs | sous_exigence | 0 | [HR4.4.md](4-HR-droits-humains/HR4.4.md) |
| HR4.5 | DH 4.5 | L'entreprise renforce ses engagements au sein de ses documents d'approvisionnement | sous_exigence | 5 | [HR4.5.md](4-HR-droits-humains/HR4.5.md) |
| HR4.6 | DH 4.6 | L'entreprise dispose d'un plan assorti d'un calendrier pour retracer origine et impacts de matières premières à haut risque | sous_exigence | 3 | [HR4.6.md](4-HR-droits-humains/HR4.6.md) |
| HR4.7 | DH 4.7 | L'entreprise trace un nombre croissant de matières premières à haut risque jusqu'à leur origine | sous_exigence | 5 | [HR4.7.md](4-HR-droits-humains/HR4.7.md) |
| HR4.8 | DH 4.8 | L'entreprise collabore avec ses fournisseurs pour traiter les impacts liés aux matières premières à haut risque | sous_exigence | 5 | [HR4.8.md](4-HR-droits-humains/HR4.8.md) |
| HR4.9 | DH 4.9 | L'entreprise identifie les écarts par rapport au salaire de subsistance dans ses contrats de services | sous_exigence | 0 | [HR4.9.md](4-HR-droits-humains/HR4.9.md) |
| HR4.10 | DH 4.10 | L'entreprise fait référence au salaire de subsistance dans ses processus d'achat de services | sous_exigence | 3 | [HR4.10.md](4-HR-droits-humains/HR4.10.md) |
| HR4.11 | DH 4.11 | L'entreprise dispose d'un plan pour aborder le salaire de subsistance, revenu de subsistance ou négociation collective | sous_exigence | 3 | [HR4.11.md](4-HR-droits-humains/HR4.11.md) |

## [CA : Action climatique](5-CA-action-climatique/_index.md)

| Code | Code FR | Intitulé | Type | Year | Lien |
|---|---|---|---|---|---|
| CA1.1 | AC 1.1 | L'entreprise dispose d'un processus documenté pour mesurer chaque année ses émissions de GES sur les scope 1, 2 et 3 | sous_exigence | 0 | [CA1.1.md](5-CA-action-climatique/CA1.1.md) |
| CA1.2 | AC 1.2 | L'entreprise fait appel à un organisme tiers indépendant pour vérifier l'inventaire annuel de ses émissions de GES | sous_exigence | 0 | [CA1.2.md](5-CA-action-climatique/CA1.2.md) |
| CA2.1 | AC 2.1 | L'entreprise dispose d'un plan d'action climatique accessible publiquement | sous_exigence | 0 | [CA2.1.md](5-CA-action-climatique/CA2.1.md) |
| CA2.2 | AC 2.2 | L'entreprise a des objectifs alignés sur les connaissances scientifiques, validés par la SBTi ou vérifiés par un organisme tiers indépendant | sous_exigence | 3 | [CA2.2.md](5-CA-action-climatique/CA2.2.md) |
| CA2.3 | AC 2.3 | L'entreprise a un plan de transition climatique pour contribuer à la neutralité carbone 2050 | sous_exigence | 3 | [CA2.3.md](5-CA-action-climatique/CA2.3.md) |
| CA2.4 | AC 2.4 | L'entreprise consulte collaborateurs et parties prenantes pour garantir transition juste | sous_exigence | 3 | [CA2.4.md](5-CA-action-climatique/CA2.4.md) |
| CA3.1 | AC 3.1 | Si l'entreprise dispose d'un système de rémunération incitative pour l'équipe de direction, celui-ci intègre des objectifs climatiques | sous_exigence | 3 | [CA3.1.md](5-CA-action-climatique/CA3.1.md) |
| CA3.2 | AC 3.2 | L'entreprise utilise le plaidoyer pour soutenir l'objectif mondial de zéro émission nette 2050 | sous_exigence | 3 | [CA3.2.md](5-CA-action-climatique/CA3.2.md) |
| CA3.3 | AC 3.3 | L'entreprise fait progresser son plan d'action climatique et évalue son efficacité | sous_exigence | 3 | [CA3.3.md](5-CA-action-climatique/CA3.3.md) |
| CA3.4 | AC 3.4 | L'entreprise réalise des progrès sur son plan de transition climatique et évalue son efficacité | sous_exigence | 5 | [CA3.4.md](5-CA-action-climatique/CA3.4.md) |
| CA3.5 | AC 3.5 | L'entreprise met en place des actions pour une transition juste | sous_exigence | 5 | [CA3.5.md](5-CA-action-climatique/CA3.5.md) |
| CA3.6 | AC 3.6 | L'entreprise rend publics les progrès réalisés dans le cadre de son plan d'action climatique | sous_exigence | 3 | [CA3.6.md](5-CA-action-climatique/CA3.6.md) |
| CA3.7 | AC 3.7 | L'entreprise publie chaque année l'état d'avancement de son plan de transition climatique | sous_exigence | 5 | [CA3.7.md](5-CA-action-climatique/CA3.7.md) |

## [ESC : Gestion environnementale et circularité](6-ESC-gestion-environnementale-et-circularite/_index.md)

| Code | Code FR | Intitulé | Type | Year | Lien |
|---|---|---|---|---|---|
| ESC1.1 | GEC 1.1 | L'entreprise surveille la production de déchets issus de ses activités et leur destination finale | sous_exigence | 0 | [ESC1.1.md](6-ESC-gestion-environnementale-et-circularite/ESC1.1.md) |
| ESC1.2 | GEC 1.2 | L'entreprise surveille sa consommation énergétique | sous_exigence | 0 | [ESC1.2.md](6-ESC-gestion-environnementale-et-circularite/ESC1.2.md) |
| ESC1.3 | GEC 1.3 | L'entreprise surveille sa consommation ou son prélèvement d'eau | sous_exigence | 0 | [ESC1.3.md](6-ESC-gestion-environnementale-et-circularite/ESC1.3.md) |
| ESC1.4 | GEC 1.4 | L'entreprise identifie ses infrastructures dans les zones à risque hydrique et surveille leur consommation ou leur prélèvement d'eau | sous_exigence | 0 | [ESC1.4.md](6-ESC-gestion-environnementale-et-circularite/ESC1.4.md) |
| ESC1.5 | GEC 1.5 | L'entreprise identifie ses infrastructures situées en zone écologiquement sensible ou à proximité, et détermine si elles ont une incidence négative | sous_exigence | 0 | [ESC1.5.md](6-ESC-gestion-environnementale-et-circularite/ESC1.5.md) |
| ESC1.6 | GEC 1.6 | L'entreprise surveille les conditions de bien-être animal dans ses activités | sous_exigence | 0 | [ESC1.6.md](6-ESC-gestion-environnementale-et-circularite/ESC1.6.md) |
| ESC1.7 | GEC 1.7 | L'entreprise procède à une évaluation afin d'identifier les impacts environnementaux réels et potentiels liés à ses activités internes et à sa chaîne de valeur | sous_exigence | 0 | [ESC1.7.md](6-ESC-gestion-environnementale-et-circularite/ESC1.7.md) |
| ESC1.8 | GEC 1.8 | L'entreprise partage publiquement ses enjeux environnementaux matériels | sous_exigence | 3 | [ESC1.8.md](6-ESC-gestion-environnementale-et-circularite/ESC1.8.md) |
| ESC2.1 | GEC 2.1 | L'entreprise a mis en place une stratégie pour remédier à ses impacts négatifs réels et potentiels sur l'environnement | sous_exigence | 3 | [ESC2.1.md](6-ESC-gestion-environnementale-et-circularite/ESC2.1.md) |
| ESC2.2 | GEC 2.2 | L'entreprise dispose d'un plan de transition pour la biodiversité visant à arrêter et à inverser la perte de biodiversité | sous_exigence | 3 | [ESC2.2.md](6-ESC-gestion-environnementale-et-circularite/ESC2.2.md) |
| ESC2.3 | GEC 2.3 | L'entreprise a mis en place une stratégie de gestion de l'eau qui limite la consommation d'eau à des seuils soutenables | sous_exigence | 3 | [ESC2.3.md](6-ESC-gestion-environnementale-et-circularite/ESC2.3.md) |
| ESC2.4 | GEC 2.4 | Les politiques et procédures de l'entreprise traitent les enjeux d'impacts environnementaux matériels | sous_exigence | 3 | [ESC2.4.md](6-ESC-gestion-environnementale-et-circularite/ESC2.4.md) |
| ESC2.5 | GEC 2.5 | Les collaborateurs exerçant des fonctions pertinentes reçoivent les conseils dont ils ont besoin pour mettre en œuvre les politiques et procédures environnementales | sous_exigence | 3 | [ESC2.5.md](6-ESC-gestion-environnementale-et-circularite/ESC2.5.md) |
| ESC2.6 | GEC 2.6 | L'entreprise évalue les impacts environnementaux négatifs potentiels liés à ses prospects organisationnels et aux projets envisagés, et prend les mesures d'atténuation nécessaires | sous_exigence | 0 | [ESC2.6.md](6-ESC-gestion-environnementale-et-circularite/ESC2.6.md) |
| ESC2.7 | GEC 2.7 | L'entreprise évalue les impacts environnementaux négatifs potentiels des investissements, et prend les mesures d'atténuation nécessaires | sous_exigence | 0 | [ESC2.7.md](6-ESC-gestion-environnementale-et-circularite/ESC2.7.md) |
| ESC3.1 | GEC 3.1 | L'entreprise surveille ses approvisionnements en matériaux | sous_exigence | 0 | [ESC3.1.md](6-ESC-gestion-environnementale-et-circularite/ESC3.1.md) |
| ESC3.2 | GEC 3.2 | L'entreprise réduit son utilisation de matériaux vierges non renouvelables | sous_exigence | 3 | [ESC3.2.md](6-ESC-gestion-environnementale-et-circularite/ESC3.2.md) |
| ESC3.3 | GEC 3.3 | Le développement des produits de l'entreprise intègre les principes de circularité | sous_exigence | 3 | [ESC3.3.md](6-ESC-gestion-environnementale-et-circularite/ESC3.3.md) |
| ESC3.3a | GEC 3.3a | The company avoids and reduces single-use products and packaging in its portfolio. | option | 3 | [ESC3.3a.md](6-ESC-gestion-environnementale-et-circularite/ESC3.3a.md) |
| ESC3.3b | GEC 3.3b | The company designs its products for long-term use. | option | 3 | [ESC3.3b.md](6-ESC-gestion-environnementale-et-circularite/ESC3.3b.md) |
| ESC3.3c | GEC 3.3c | The company’s products are able to recirculate after use. | option | 3 | [ESC3.3c.md](6-ESC-gestion-environnementale-et-circularite/ESC3.3c.md) |
| ESC3.3d | GEC 3.3d | The company’s products are able to recirculate at their end-of-life | option | 3 | [ESC3.3d.md](6-ESC-gestion-environnementale-et-circularite/ESC3.3d.md) |
| ESC3.4 | GEC 3.4 | L'entreprise comprend les infrastructures de revalorisation disponibles là où elle vend ses produits | sous_exigence | 0 | [ESC3.4.md](6-ESC-gestion-environnementale-et-circularite/ESC3.4.md) |
| ESC3.5 | GEC 3.5 | L'entreprise prend des mesures pour augmenter la revalorisation de ses produits et emballages après leur fin de vie | sous_exigence | 3 | [ESC3.5.md](6-ESC-gestion-environnementale-et-circularite/ESC3.5.md) |
| ESC4.1 | GEC 4.1 | L'entreprise met en place des actions pour prévenir ou atténuer ses impacts environnementaux négatifs réels et potentiels | sous_exigence | 3 | [ESC4.1.md](6-ESC-gestion-environnementale-et-circularite/ESC4.1.md) |
| ESC4.2 | GEC 4.2 | L'entreprise progresse dans sa stratégie environnementale et en évalue l'efficacité | sous_exigence | 5 | [ESC4.2.md](6-ESC-gestion-environnementale-et-circularite/ESC4.2.md) |
| ESC4.3 | GEC 4.3 | L'entreprise progresse dans son plan de transition pour la biodiversité et évalue son efficacité | sous_exigence | 5 | [ESC4.3.md](6-ESC-gestion-environnementale-et-circularite/ESC4.3.md) |
| ESC4.4 | GEC 4.4 | L'entreprise progresse dans sa stratégie de gestion de l'eau et évalue son efficacité | sous_exigence | 5 | [ESC4.4.md](6-ESC-gestion-environnementale-et-circularite/ESC4.4.md) |
| ESC4.5 | GEC 4.5 | L'entreprise partage publiquement l'efficacité de sa stratégie environnementale | sous_exigence | 5 | [ESC4.5.md](6-ESC-gestion-environnementale-et-circularite/ESC4.5.md) |
| ESC5.1 | GEC 5.1 | L'entreprise travaille avec ses prestataires de biens et de services pour atteindre ses objectifs environnementaux | sous_exigence | 0 | [ESC5.1.md](6-ESC-gestion-environnementale-et-circularite/ESC5.1.md) |
| ESC5.2 | GEC 5.2 | L'entreprise prend en compte les impacts environnementaux réels et potentiels dans ses décisions d'achat | sous_exigence | 0 | [ESC5.2.md](6-ESC-gestion-environnementale-et-circularite/ESC5.2.md) |
| ESC5.3 | GEC 5.3 | L'entreprise collabore avec ses fournisseurs pour prévenir ou atténuer leurs impacts environnementaux les plus matériels | sous_exigence | 0 | [ESC5.3.md](6-ESC-gestion-environnementale-et-circularite/ESC5.3.md) |
| ESC5.4 | GEC 5.4 | L'entreprise dispose d'un plan, défini dans le temps, pour assurer la traçabilité de l'origine de ses matières premières à haut risque ainsi que leurs impacts environnementaux potentiels | sous_exigence | 3 | [ESC5.4.md](6-ESC-gestion-environnementale-et-circularite/ESC5.4.md) |
| ESC5.5 | GEC 5.5 | L'entreprise s'approvisionne en matières premières non issues de la déforestation | sous_exigence | 3 | [ESC5.5.md](6-ESC-gestion-environnementale-et-circularite/ESC5.5.md) |
| ESC5.6 | GEC 5.6 | L'entreprise trace une part croissante de ses matières premières à haut risque | sous_exigence | 5 | [ESC5.6.md](6-ESC-gestion-environnementale-et-circularite/ESC5.6.md) |
| ESC5.7 | GEC 5.7 | L'entreprise collabore avec ses fournisseurs pour remédier aux impacts environnementaux liés aux matières premières à haut risque | sous_exigence | 5 | [ESC5.7.md](6-ESC-gestion-environnementale-et-circularite/ESC5.7.md) |

## [GACA : Affaires publiques & action collective](7-GACA-affaires-publiques-action-collective/_index.md)

| Code | Code FR | Intitulé | Type | Year | Lien |
|---|---|---|---|---|---|
| GACA1.1 | APAC 1.1 | L'entreprise dispose d'une politique publiquement accessible en matière de lobbying responsable | sous_exigence | 0 | [GACA1.1.md](7-GACA-affaires-publiques-action-collective/GACA1.1.md) |
| GACA1.2 | APAC 1.2 | L'entreprise rend publique ses positions en matière de lobbying ainsi que ses contributions politiques | sous_exigence | 0 | [GACA1.2.md](7-GACA-affaires-publiques-action-collective/GACA1.2.md) |
| GACA1.3 | APAC 1.3 | L'entreprise rend publiques ses positions en matière de lobbying et ses contributions politiques | sous_exigence | 3 | [GACA1.3.md](7-GACA-affaires-publiques-action-collective/GACA1.3.md) |
| GACA2.1 | APAC 2.1 | L'entreprise prend part à des actions collectives visant à promouvoir des impacts sociaux ou environnementaux positifs | sous_exigence | 0 | [GACA2.1.md](7-GACA-affaires-publiques-action-collective/GACA2.1.md) |
| GACA2.2 | APAC 2.2 | The company takes part in collective action to advance social or environmental impacts. | sous_exigence | 0 | [GACA2.2.md](7-GACA-affaires-publiques-action-collective/GACA2.2.md) |
| GACA2.1a | APAC 2.1a | The company mentors others in its industry, profession, or value chain to advance their social or environmental impacts. | option | 0 | [GACA2.1a.md](7-GACA-affaires-publiques-action-collective/GACA2.1a.md) |
| GACA2.1b | APAC 2.1b | The company contributes to external research to advance social or environmental impacts. | option | 0 | [GACA2.1b.md](7-GACA-affaires-publiques-action-collective/GACA2.1b.md) |
| GACA2.1c | APAC 2.1c | The company collaborates with multiple stakeholders to advance social or environmental impacts. | option | 0 | [GACA2.1c.md](7-GACA-affaires-publiques-action-collective/GACA2.1c.md) |
| GACA2.1d | APAC 2.1d | The company promotes public policy to advance social or environmental impacts. | option | 0 | [GACA2.1d.md](7-GACA-affaires-publiques-action-collective/GACA2.1d.md) |
| GACA2.1e | APAC 2.1e | The company uses thought leadership to drive systemic change towards an equitable, inclusive, and regenerative economy. | option | 0 | [GACA2.1e.md](7-GACA-affaires-publiques-action-collective/GACA2.1e.md) |
| GACA2.3 | APAC 2.3 | The company takes part in collective action to advance social or environmental impacts. | sous_exigence | 0 | [GACA2.3.md](7-GACA-affaires-publiques-action-collective/GACA2.3.md) |
| GACA2.4 | APAC 2.4 | The company takes part in collective action to advance social or environmental impacts. | sous_exigence | 0 | [GACA2.4.md](7-GACA-affaires-publiques-action-collective/GACA2.4.md) |
| GACA2.5 | APAC 2.5 | L'entreprise participe à une action collective visant à faire progresser les impacts sociaux ou environnementaux | sous_exigence | 0 | [GACA2.5.md](7-GACA-affaires-publiques-action-collective/GACA2.5.md) |
| GACA2.3a | APAC 2.3a | The company mentors others in its industry, profession, or value chain to advance their social or environmental impacts. | option | 0 | [GACA2.3a.md](7-GACA-affaires-publiques-action-collective/GACA2.3a.md) |
| GACA2.3b | APAC 2.3b | The company contributes to external research to advance social or environmental impacts. | option | 0 | [GACA2.3b.md](7-GACA-affaires-publiques-action-collective/GACA2.3b.md) |
| GACA2.3c | APAC 2.3c | The company collaborates with multiple stakeholders to advance social or environmental impacts with clear contribution. | option | 0 | [GACA2.3c.md](7-GACA-affaires-publiques-action-collective/GACA2.3c.md) |
| GACA2.3d | APAC 2.3d | The company promotes public policy to advance social or environmental impacts with clear contribution. | option | 0 | [GACA2.3d.md](7-GACA-affaires-publiques-action-collective/GACA2.3d.md) |
| GACA2.3e | APAC 2.3e | The company uses thought leadership to drive systemic change towards an equitable, inclusive, and regenerative economy, and has a clear outcome. | option | 0 | [GACA2.3e.md](7-GACA-affaires-publiques-action-collective/GACA2.3e.md) |
| GACA2.6 | APAC 2.6 | L'entreprise inclut les initiatives multipartites ou le plaidoyer en faveur de politiques publiques | sous_exigence | 3 | [GACA2.6.md](7-GACA-affaires-publiques-action-collective/GACA2.6.md) |
| GACA3.1 | APAC 3.1 | L'entreprise dispose d'une politique en matière de fiscalité responsable et la rend publique | sous_exigence | 0 | [GACA3.1.md](7-GACA-affaires-publiques-action-collective/GACA3.1.md) |
| GACA3.2 | APAC 3.2 | L'entreprise publie son reporting pays par pays pour chaque année fiscale | sous_exigence | 3 | [GACA3.2.md](7-GACA-affaires-publiques-action-collective/GACA3.2.md) |
