from odds_toolkit.odds import american_to_decimal

def test_american_plus():
    assert abs(american_to_decimal(100) - 2.0) < 1e-9

def test_american_minus():
    assert abs(american_to_decimal(-200) - 1.5) < 1e-9
