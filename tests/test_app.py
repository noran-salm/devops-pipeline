from app import calc_discount
import pytest

def test_ten_precent():
    result = calc_discount(100,10)
    assert result == 90

def test_zero_percent():
    result = calc_discount(100,0)
    assert result == 100

def test_invalid_discount():
    with pytest.raises(ValueError):
        calc_discount(100,150)

def test_negative_discount():
    with pytest.raises(ValueError):
        calc_discount(100,-10)

def test_negative_price():
    with pytest.raises(ValueError):
        calc_discount(-100,10)