import pytest
from quant_math.returns import simple_return
from quant_math.returns import log_return

def test_gain():
    assert simple_return(110, 100) == pytest.approx(0.10)

def test_loss():
    assert simple_return(90, 100) == pytest.approx(-0.10)

def test_flat():
    assert simple_return(100, 100) == pytest.approx(0.0)

def test_zero_prev_raises():
    with pytest.raises(ValueError):
        simple_return(110, 0)


def test_log_return_gain():
    assert log_return(110, 100) == pytest.approx(0.0953, rel=1e-3)

def test_log_return_loss():
    assert log_return(90, 100) == pytest.approx(-0.1054, rel=1e-3)

def test_log_return_flat():
    assert log_return(100, 100) == pytest.approx(0.0)

def test_log_return_zero_price_raises():
    with pytest.raises(ValueError):
        log_return(110, 0)

def test_log_return_negative_price_raises():
    with pytest.raises(ValueError):
        log_return(-110, 100)

