from odds_toolkit.odds import clv, vig_free_two_way

def test_clv_positive_when_open_better():
    assert clv(2.10, 2.00) > 0

def test_clv_zero_equal():
    assert abs(clv(2.0, 2.0)) < 1e-12

def test_vig_free_sums_to_one():
    a, b = vig_free_two_way(1.91, 1.91)
    assert abs(a + b - 1.0) < 1e-12
