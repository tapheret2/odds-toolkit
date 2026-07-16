from odds_toolkit import prob_to_american

def test_even_money():
    assert abs(prob_to_american(0.5) - 100.0) < 1e-6 or abs(prob_to_american(0.5) + 100.0) < 1e-6
