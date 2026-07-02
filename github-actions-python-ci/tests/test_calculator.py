import pytest
from app.calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(-1, -1) == -2

def test_subtract():
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(-1, 1) == -2
    assert calc.subtract(-1, -1) == 0

def test_multiply():
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-1, 1) == -1
    assert calc.multiply(-1, -1) == 1

def test_divide():
    assert calc.divide(6, 3) == 2
    assert calc.divide(-6, 3) == -2
    assert calc.divide(-6, -3) == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(1, 0)