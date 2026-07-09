from odds_toolkit import fair_odds

def test_fair_odds_even_money():
    assert abs(fair_odds(0.5) - 2.0) < 1e-9
