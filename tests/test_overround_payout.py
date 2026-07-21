from odds_toolkit import overround, payout

def test_overround_positive():
    assert abs(overround([0.55, 0.55]) - 0.10) < 1e-12

def test_payout_even():
    assert abs(payout(10, 2.0) - 20.0) < 1e-12
