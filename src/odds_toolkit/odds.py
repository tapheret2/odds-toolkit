from __future__ import annotations

from fractions import Fraction
from math import gcd


def american_to_decimal(american: float) -> float:
    if american == 0:
        raise ValueError("American odds cannot be 0")
    if american > 0:
        return 1.0 + american / 100.0
    return 1.0 + 100.0 / abs(american)


def decimal_to_american(decimal: float) -> float:
    if decimal <= 1.0:
        raise ValueError("Decimal odds must be > 1")
    if decimal >= 2.0:
        return (decimal - 1.0) * 100.0
    return -100.0 / (decimal - 1.0)


def fractional_to_decimal(num: int, den: int) -> float:
    if den <= 0 or num < 0:
        raise ValueError("Invalid fractional odds")
    return 1.0 + num / den


def decimal_to_fractional(decimal: float) -> tuple[int, int]:
    if decimal <= 1.0:
        raise ValueError("Decimal odds must be > 1")
    frac = Fraction(decimal - 1.0).limit_denominator(1000)
    return frac.numerator, frac.denominator


def implied_prob(decimal: float) -> float:
    if decimal <= 1.0:
        raise ValueError("Decimal odds must be > 1")
    return 1.0 / decimal


def remove_overround(probs: list[float], method: str = "proportional") -> list[float]:
    """Normalize raw implied probs so they sum to 1 (simple proportional)."""
    if not probs:
        raise ValueError("empty probs")
    if any(p <= 0 for p in probs):
        raise ValueError("probs must be > 0")
    s = sum(probs)
    if method != "proportional":
        raise ValueError("only proportional method supported")
    return [p / s for p in probs]


def expected_value(true_p: float, decimal: float, stake: float = 1.0) -> float:
    """EV of a unit stake at decimal odds given true win probability."""
    if not 0.0 <= true_p <= 1.0:
        raise ValueError("true_p must be in [0, 1]")
    if decimal <= 1.0:
        raise ValueError("Decimal odds must be > 1")
    win = stake * (decimal - 1.0)
    lose = -stake
    return true_p * win + (1.0 - true_p) * lose
