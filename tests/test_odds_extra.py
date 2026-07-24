from odds_toolkit.odds import no_vig_two_way, parlay_decimal


def test_parlay_decimal():
    assert abs(parlay_decimal([2.0, 1.5, 2.0]) - 6.0) < 1e-9


def test_no_vig_two_way():
    a, b = no_vig_two_way(0.55, 0.55)
    assert abs(a + b - 1.0) < 1e-9
    assert abs(a - 0.5) < 1e-9
