import pytest

import bcorp_ref as ref


@pytest.mark.parametrize("etp, ca_usd, expected", [
    (0, 0, "Company without workers"),
    (5, 1_000_000, "Micro"),
    (30, 5_000_000, "Small"),
    (65, 36_000_000, "Medium"),      # cas Medium typique
    (300, 20_000_000, "Medium"),     # la plus petite des deux tailles
    (60, 1_500_000, "Micro"),
    (500, 100_000_000, "Large"),
    (2_000, 400_000_000, "X Large"),
    (20_000, 2_000_000_000, "XX Large"),
])
def test_size_lesser_of_two(etp, ca_usd, expected):
    assert ref.size_category(etp, ca_usd).category == expected


def test_size_is_never_confirmed_until_thresholds_verified():
    s = ref.size_category(65, 36_000_000)
    assert s.confirmed is False
    assert "à confirmer" in s.note


def test_boundary_gap_is_flagged():
    # Le tableau B Lab laisse un trou à 10 000 ETP / 1,5 Md USD
    assert ref.size_category(10_000, 2_000_000_000).boundary_issue is True
