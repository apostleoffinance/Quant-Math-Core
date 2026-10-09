import pytest
from quant_math.compounding import compound_value

def test_three_years_at_10pct():
    assert compound_value(100, 0.10, 3) == pytest.approx(133.10, rel=1e-9)

def test_ten_years_at_5pct():
    assert compound_value(1000, 0.05, 10) == pytest.approx(1628.8946267, rel=1e-6)

def test_zero_periods_returns_principal():
    assert compound_value(100, 0.05, 0) == pytest.approx(100.0)

def test_negative_T_raises():
    with pytest.raises(ValueError):
        compound_value(100, 0.05, -1)