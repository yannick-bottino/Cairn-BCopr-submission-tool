# 06 — Seuils de taille d'entreprise, B Lab Standards V2.x (certification "new standards")

Date de la recherche : 2026-10-04. Périmètre : B Lab Standards V2.1 / V2.2 (V2.2 publiée le 20/02/2026), catégories Company without workers → XX Large.

## 0. Limite de méthode (à lire avant d'utiliser les chiffres)

Le proxy réseau de cette session a bloqué la lecture directe de toutes les pages utiles : kb.bimpactassessment.net, bcorporation.net, bcorporation.eu, web.archive.org, ainsi que les blogs tiers (seedling.earth, theterrace.nl, greensmallbusiness.com, 3rsustainability.com, b-boosters.com). WebFetch et curl renvoient `EGRESS_BLOCKED` / `CONNECT 403`. Je n'ai donc pas pu ouvrir l'image du tableau dans la KB.

Les chiffres ci-dessous viennent des extraits que le moteur WebSearch indexe pour ces pages. Ce sont des extraits, pas des lectures intégrales vérifiées à l'œil. Le tableau a pourtant été renvoyé à l'identique par trois requêtes différentes, dont une limitée aux domaines officiels B Lab (kb.bimpactassessment.net, bcorporation.net, bcorporation.eu). Deux seuils (Large et X Large) sont en plus recoupés par la presse d'avril 2025. **À faire avant mise en production : un humain ouvre la page KB 43000747439 (ou la page Pricing V2 de B Lab Europe) et confirme le tableau en 2 minutes.**

## 1. Tableau final des seuils (V2.1/V2.2, règle en vigueur depuis novembre 2025)

| Catégorie | Effectif (workers, en ETP) | CA annuel (USD) | Confiance effectif | Confiance CA |
|---|---|---|---|---|
| Company without workers | 0 | (vide dans le tableau B Lab) | Moyenne-haute | n/a, voir §3 |
| Micro | 1-9 | < 2 M | Haute | Moyenne-haute |
| Small | 10-49 | 2 M à < 10 M | Haute | Moyenne-haute |
| Medium | 50-249 | 10 M à < 75 M | Haute | Moyenne-haute |
| Large | 250-999 | 75 M à < 350 M | Haute | Haute (recoupé presse) |
| X Large | 1 000-9 999 | 350 M à < 1,5 Md | Haute (recoupé presse) | Haute (recoupé presse) |
| XX Large | > 10 000 | > 1,5 Md | Moyenne-haute | Moyenne-haute |

Texte du tableau tel que restitué par l'index (requête limitée aux domaines B Lab, pages KB 43000772932 / 43000747439 et Pricing V2 B Lab Europe) :

> | Size | Number of workers | Annual revenue in $ |
> | Companies without workers | 0 | |
> | Micro companies | 1-9 | < 2 million |
> | Small companies | 10-49 | 2 - <10 million |
> | Medium companies | 50-249 | 10 - <75 million |
> | Large companies | 250-999 | 75 - <350 million |
> | X Large companies | 1,000-9,999 | 350 - <1.5 billion |
> | XX Large companies | > 10,000 | >1.5 billion |

### Bornes inclusives / exclusives
- Effectif : bornes inclusives (1-9, 10-49…). Exactement 10 000 : le tableau dit "1,000-9,999" puis "> 10,000", donc la valeur 10 000 tombe dans un trou. Interprétation raisonnable : 10 000 et plus = XX Large. À confirmer sur l'image.
- CA : borne basse incluse, borne haute exclue ("2 - <10 million"). Exactement 1,5 Md : "<1.5 billion" puis ">1.5 billion", même trou. Interprétation raisonnable : ≥ 1,5 Md = XX Large.

## 2. Règle de combinaison : "Lesser of Two" (la plus petite des deux)

- **En vigueur depuis novembre 2025** (officiel B Lab, KB 43000772932 "FAQs: Change to Determining Company Size in the B Lab Standards V2.1") :
  > "Companies are assigned to the size category corresponding to their number of workers or revenue — whichever is lower. This change is effective November 2025."
- **Avant** (V2 d'avril 2025 et consultation draft 2 de 2024) : "Greater of Two". Extrait de la même FAQ :
  > B Lab previously used the "Greater of Two" rule, classifying company size based on the higher of annual revenue or number of workers. They are moving to the "Lesser of Two" rule.
  
  Motif donné : les entreprises du Sud global, avec beaucoup de salariés pour un CA modeste, étaient "bumped up" dans des tailles supérieures. Le changement a été fait avant les premiers audits V2.1 de février 2026.
- Draft 2024 : la consultation "shifting from solely worker count to either worker count or revenue, depending on which is higher" (extrait indexé, bcorporation.net, consultation janvier-mars 2024).
- B Lab Europe (Pricing V2) dit la même chose, avec la devise :
  > "B Lab determines company size based on both the number of workers and the company's revenue in U.S. dollars, with whichever value is lower determining the size designation." (extrait indexé de https://bcorporation.eu/b-corp-costs/pricing-2/)

V2.2 (20/02/2026) : d'après les sources trouvées, cette version modifie surtout FR1.2 (listes fermées d'industries). Je n'ai trouvé aucune mention d'un changement des seuils de taille en V2.2.

## 3. Définitions

- **Workers / effectif** : mesuré en ETP.
  > "Worker size is determined by Full-Time Equivalency (FTE), a measure of the work done by the company's entire workforce as if they were all full-time employees." (KB 43000772932 et 43000747439)
- **Qui compte comme worker** (KB 43000574690 "A reference for the calculation of Full-time Equivalency (FTE) Workers", extrait indexé ; l'article date de l'époque BIA, je n'ai pas pu vérifier s'il a été mis à jour pour la V2) : salariés de tous types (permanents, temporaires, temps plein, temps partiel, saisonniers, occasionnels), plus les indépendants et intérimaires qui travaillent plus de 20 h/semaine, sans limite de durée ou pendant plus de 6 mois. Les "working owners" sont des workers mais **ne sont pas comptés dans l'ETP**. Barème d'estimation : 35 h et plus = 1 ; 20-35 h = 0,5 ; moins de 20 h = 0,25 (si plus de 6 mois) ; 0,5 / 0,25 / 0 si moins de 6 mois.
- **Devise** : USD (B Lab Europe et KB 43000747439).
- **Période du CA** : **non trouvée.** Aucune source consultable ne précise "dernier exercice clos". Ne pas l'affirmer dans le plugin. Garder "CA annuel" et le marquer à vérifier.
- **Company without workers** : 0 dans la colonne effectif, case CA vide. Pas de définition textuelle trouvée. Lecture probable, non confirmée : 0 ETP, par exemple une société où seuls les associés travaillent, puisque les working owners ne comptent pas dans l'ETP. Avec la règle "lesser of two", une entreprise à 0 ETP tombe dans cette catégorie quel que soit son CA. C'est cohérent avec la case CA vide, mais il s'agit d'une inférence. Ces entreprises sont exemptées de FR3.1 (avec Micro) et du sujet Fair Work.

## 4. Sources

| # | Source | Statut | URL | Ce qu'elle établit |
|---|---|---|---|---|
| S1 | KB B Lab, "FAQs: Change to Determining Company Size in the B Lab Standards V2.1" | Officielle B Lab, finale (V2.1) | https://kb.bimpactassessment.net/en/support/solutions/articles/43000772932-faqs-change-to-determining-company-size-in-the-b-lab-standards-v2-1 | Lesser of two depuis nov. 2025 ; avant, greater of two ; ETP ; tableau (restitué par l'index) |
| S2 | KB B Lab, "How are the new B Lab Standards requirements tailored to each company's context?" | Officielle B Lab, finale | https://kb.bimpactassessment.net/en/support/solutions/articles/43000747439-how-the-new-b-lab-standards-requirements-are-tailored-to-each-company-s-context- | Tableau complet, USD, "whichever is lower", ETP |
| S3 | B Lab Europe, Pricing V2 | Officielle B Lab régionale, finale | https://bcorporation.eu/b-corp-costs/pricing-2/ | Même tableau, USD, "whichever value is lower" ; Company without workers = 0 |
| S4 | KB B Lab, EB3.1 / FR3.1 "Managing Negative Impact(s) through the Foundation Requirement" | Officielle B Lab (rédigée sous greater of two) | https://kb.bimpactassessment.net/en/support/solutions/articles/43000761433 | "small or above if it has at least 10 workers or $2 million in annual revenue". Cohérent avec les seuils Small (10 / 2 M$), formulé selon l'ancienne règle "greater of two" |
| S5 | KB B Lab, calcul ETP | Officielle B Lab (époque BIA, mise à jour V2 non vérifiée) | https://kb.bimpactassessment.net/en/support/solutions/articles/43000574690-a-reference-for-the-calculation-of-full-time-equivalency-fte-workers | Définition des workers et barème ETP |
| S6 | just-food, "B Lab sets out new B Corp standards" (avril 2025) | Tierce (presse) | https://www.just-food.com/news/new-b-corp-standards/ | "larger companies – defined as having between 250 and 999 employees or $75m to $350m … 1,000 to 9,999 employees, or $350m to $1.5bn" |
| S7 | Trellis, "B Lab overhauls B Corp certification" (avril 2025) | Tierce (presse) | https://trellis.net/article/b-corp-certification-update-mandates-minimum-performance/ | Exigences renforcées "more than 1,000 employees or $350 million in sales" |
| S8 | Recherches indexées sur theterrace.nl, greensmallbusiness.com | Tierce | https://theterrace.nl/news/new-b-corp-standards-2025-for-large-enterprise/ | X Large = 1 000-9 999 / 350 M-<1,5 Md$ |

## 5. Divergences

| Source | Ce qu'elle dit | Diagnostic |
|---|---|---|
| **Excel de la consultante** (source inconnue) | Micro < 1 M$ ; Small 1-10 M$ ; Medium 10-50 M$ ; Large 50-250 M$ ; X Large 1 000-4 999 / 250 M-1 Md$ ; XX Large 5 000+ / > 1 Md$ | **À rejeter.** Seules les bandes d'effectif Micro à Large (1-9, 10-49, 50-249, 250-999) et la règle "lesser of two" sont justes. Toutes les bandes de CA sont fausses (officiel : 2 / 10 / 75 / 350 M$ / 1,5 Md$). Les bandes X/XX Large aussi (officiel : 1 000-9 999 et plus de 10 000). Aucune source trouvée ne reprend ces chiffres. |
| **Blog Seedling** | Small < 50 / < 10 M$ ; Medium 50-249 / 10-50 M$ ; Large ≥ 250 / ≥ 50 M$ | Le seuil Medium/Large à 50 M$ contredit l'officiel (75 M$). Il vient probablement d'un draft ou d'une approximation. Page non lisible, je n'ai pas pu dater sa source. |
| **Résumé KB "Small = au moins 10 employés ou CA > 2 M$"** (S4) | 10 workers **ou** 2 M$ | Pas de contradiction sur les seuils. Le "ou" correspond à l'ancienne règle "greater of two", remplacée en novembre 2025 par "lesser of two" (il faut alors 10 workers **et** 2 M$ pour être Small). |
| **Ancien BIA V6** | 0, 1-9, 10-49, 50-249, 250-999, 1000+ (effectif seul) | Mêmes bandes d'effectif jusqu'à 999. La V2 ajoute le CA, scinde 1000+ en X Large (1 000-9 999) et XX Large (plus de 10 000), et change la règle de combinaison. |
| **Draft 2 (2024)** | Effectif ou CA, "whichever is higher" | Règle remplacée. Je n'ai pas trouvé les montants exacts du draft. |

## 6. Recommandation pour le plugin

1. Encoder le tableau du §1 comme référence V2.1/V2.2, en USD, effectif en ETP.
2. Calculer la taille = `min(taille_par_ETP, taille_par_CA)` ("lesser of two"). Cas 0 ETP → "Company without workers".
3. Bornes à coder : ETP 1-9 / 10-49 / 50-249 / 250-999 / 1 000-9 999 / ≥ 10 000. CA < 2 M / [2 ; 10[ / [10 ; 75[ / [75 ; 350[ / [350 M ; 1,5 Md[ / ≥ 1,5 Md. Signaler les deux trous (10 000 ETP pile, 1,5 Md pile) comme cas à confirmer.
4. Conversion EUR → USD : demander le taux au consultant, ne pas en fixer un en dur. Afficher un avertissement quand le CA tombe à moins de 10 % d'un seuil.
5. Marquer "à vérifier" : période de référence du CA, définition textuelle de "Company without workers", version V2 de l'article ETP.
6. Supprimer les valeurs de l'Excel de la consultante (bandes de CA et bandes X/XX Large).
7. Avant publication : faire confirmer le tableau sur l'image de la KB 43000747439 par une personne connectée.
