import pytest
from quant_math.compounding import (
    compound_value,
    cagr,
    periods_to_target,
)

def test_three_years_at_10pct():
    assert compound_value(100, 0.10, 3) == pytest.approx(133.10, rel=1e-9)

def test_ten_years_at_5pct():
    assert compound_value(1000, 0.05, 10) == pytest.approx(1628.8946267, rel=1e-6)

def test_zero_periods_returns_principal():
    assert compound_value(100, 0.05, 0) == pytest.approx(100.0)

def test_negative_T_raises():
    with pytest.raises(ValueError):
        compound_value(100, 0.05, -1)



def test_cagr_doubling_in_10_years():
    assert cagr(100, 200, 10) == pytest.approx(0.0718, rel=1e-2)

def test_cagr_zero_return():
    assert cagr(100, 100, 5) == pytest.approx(0.0)

def test_cagr_zero_periods_raises():
    with pytest.raises(ValueError):
        cagr(100, 200, 0)

def test_periods_to_target_double_at_7pct():
    assert periods_to_target(100, 200, 0.07) == pytest.approx(10.24, rel=1e-2)

def test_periods_to_target_zero_rate_raises():
    with pytest.raises(ValueError):
        periods_to_target(100, 200, 0)