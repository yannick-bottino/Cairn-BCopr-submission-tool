import pytest

import bcorp_ref as ref


@pytest.fixture(scope="module")
def r():
    return ref.Referentiel.load()


# --- Codes FR <-> EN -------------------------------------------------------

@pytest.mark.parametrize("raw, site", [
    ("MGPP 1.1", "PSG1.1"),
    ("MGPP1.1", "PSG1.1"),
    ("PSG1.1", "PSG1.1"),
    ("psg 1.1", "PSG1.1"),
    ("APAC 1.1", "GACA1.1"),
    ("EB 1.2", "FR1.2"),
    ("TE 4.4", "FW4.4"),
    ("DH 4.3", "HR4.3"),
    ("GEC 5.2", "ESC5.2"),
    ("AC 2.1", "CA2.1"),
    ("JEDI 2.a", "JEDI2.a"),
])
def test_to_site_code(r, raw, site):
    assert r.to_site(raw) == site


@pytest.mark.parametrize("site, excel", [
    ("PSG1.1", "MGPP 1.1"),
    ("GACA1.1", "APAC 1.1"),
    ("FR1.2", "EB 1.2"),
    ("JEDI2.a", "JEDI 2.a"),
])
def test_to_excel_code(r, site, excel):
    assert r.to_excel(site) == excel


@pytest.mark.parametrize("bad", ["CA4.4", "ESC4.7", "PSG9.9", "XYZ1.1", ""])
def test_unknown_code_is_refused(r, bad):
    # CA4.4 et ESC4.7 sont cités dans le PDF mais ne sont pas des exigences
    with pytest.raises(ref.UnknownCode):
        r.to_site(bad)


# --- Référentiel ------------------------------------------------------------

def test_counts(r):
    kinds = [x.type_ligne for x in r.rows]
    assert len(kinds) == 184
    assert kinds.count("sous_exigence") == 134
    assert kinds.count("option") == 36
    assert kinds.count("question_risk_tool") == 14


def test_impact_areas_have_fr_and_en_names(r):
    ia = r.impact_area("PSG")
    assert ia.prefix_excel == "MGPP"
    assert ia.name_fr == "Mission et gouvernance des parties prenantes"
    assert r.impact_area("FR").prefix_excel == "EB"


# --- Applicabilité (non-régression vs matrice_taille_secteur.csv) ------------

@pytest.mark.parametrize("size, sector, y0, y3, y5", [
    ("Medium", "Wholesale/Retail", 36, 18, 2),
    ("Medium", "Manufacturing", 37, 20, 4),
    ("Small", "Wholesale/Retail", 32, 8, 0),
    ("Micro", "Manufacturing", 26, 4, 0),
    ("Company without workers", "Agriculture/Growers", 16, 3, 0),
])
def test_applicable_sub_requirements_match_matrix(r, size, sector, y0, y3, y5):
    subs = [x for x in r.applicable(size, sector, horizon=5) if x.type_ligne == "sous_exigence"]
    years = [x.year for x in subs]
    assert (years.count(0), years.count(3), years.count(5)) == (y0, y3, y5)


def test_horizon_filters_years(r):
    y0 = r.applicable("Medium", "Wholesale/Retail", horizon=0)
    assert {x.year for x in y0} == {0}
    y3 = r.applicable("Medium", "Wholesale/Retail", horizon=3)
    assert {x.year for x in y3} == {0, 3}


def test_manufacturing_only_rows(r):
    wr = {x.code for x in r.applicable("Medium", "Wholesale/Retail", horizon=5)}
    mf = {x.code for x in r.applicable("Medium", "Manufacturing", horizon=5)}
    assert "ESC1.5" in mf and "ESC1.5" not in wr


def test_risk_tool_not_for_micro(r):
    micro = {x.code for x in r.applicable("Micro", "Wholesale/Retail", horizon=5)}
    assert "FR3.1.a" not in micro
    small = {x.code for x in r.applicable("Small", "Wholesale/Retail", horizon=5)}
    assert "FR3.1.a" in small


def test_criteria_expansion(r):
    row = r.get("ESC1.5")
    assert row.criteria_ids == ["1.5.1", "1.5.2", "1.5.3"]
    assert row.req_ids == ["ESC1.5-1.5.1", "ESC1.5-1.5.2", "ESC1.5-1.5.3"]


def test_invalid_size_or_sector(r):
    with pytest.raises(ValueError):
        r.applicable("Moyenne", "Wholesale/Retail", horizon=0)
    with pytest.raises(ValueError):
        r.applicable("Medium", "Retail", horizon=0)
