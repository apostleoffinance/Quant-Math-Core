import pytest
from quant_math.returns import simple_return

def test_gain():
    assert simple_return(110, 100) == pytest.approx(0.10)

def test_loss():
    assert simple_return(90, 100) == pytest.approx(-0.10)

def test_flat():
    assert simple_return(100, 100) == pytest.approx(0.0)

def test_zero_prev_raises():
    with pytest.raises(ValueError):
        simple_return(110, 0)