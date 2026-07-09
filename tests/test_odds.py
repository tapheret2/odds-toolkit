from odds_toolkit import (
    american_to_decimal,
    decimal_to_american,
    expected_value,
    implied_prob,
    remove_overround,
)


def test_american_even():
    assert abs(american_to_decimal(100) - 2.0) < 1e-9
    assert abs(american_to_decimal(-100) - 2.0) < 1e-9


def test_roundtrip_american():
    for a in [150, -200, 110, -110]:
        d = american_to_decimal(a)
        back = decimal_to_american(d)
        assert abs(back - a) < 1e-6


def test_implied():
    assert abs(implied_prob(2.0) - 0.5) < 1e-9


def test_devig():
    raw = [1 / 1.91, 1 / 2.05]
    fair = remove_overround(raw)
    assert abs(sum(fair) - 1.0) < 1e-9


def test_ev_positive_edge():
    # true 55%, odds 2.0 -> EV = 0.1 per unit
    assert abs(expected_value(0.55, 2.0) - 0.1) < 1e-9
