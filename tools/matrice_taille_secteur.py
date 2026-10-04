#!/usr/bin/env python3
"""Matrice nb de sous-exigences applicables par défaut (hors options et questions Risk Tool)
par taille x secteur x échéance, à partir de 04-referentiel-exigences.csv (colonne track_factors_brut).
Une ligne restreinte à une industrie précise est comptée à part (conditionnelle)."""
import csv, sys, collections
SIZES = ["Company without workers","Micro","Small","Medium","Large","X Large","XX Large"]
SECT = ["Service with Minor Environmental Footprint","Service with Significant Environmental Footprint",
        "Wholesale/Retail","Manufacturing","Agriculture/Growers"]
rows = [r for r in csv.DictReader(open(sys.argv[1], encoding="utf-8-sig")) if r["type_ligne"]=="sous_exigence"]
print("taille;secteur;Year0;Year3;Year5;total;dont_conditionnel_industrie")
for sz in SIZES:
    for se in SECT:
        c = collections.Counter(); cond = 0
        for r in rows:
            hit = None
            for t in r["track_factors_brut"].split(" || "):
                tsz, tse, tind = t.split(" | ")
                if tsz == sz and tse in ("All", se):
                    hit = tind
                    if tind == "All":
                        break
            if hit is not None:
                c[r["echeance"]] += 1
                if hit != "All": cond += 1
        print(f"{sz};{se};{c['Year0']};{c['Year3']};{c['Year5']};{sum(c.values())};{cond}")
