import pytest
from calculator import Calculator


def test_add():
    calculator = Calculator()
    assert calculator.add(2, 2) == 4
    assert calculator.add(6, 7) == 13
    assert calculator.add(-6, 7) == 1


def test_sub():
    calculator = Calculator()
    assert calculator.sub(2, 2) == 0
    assert calculator.sub(6, 7) == -1
    assert calculator.sub(-6, 7) == -13


def test_mul():
    calculator = Calculator()
    assert calculator.mul(2, 2) == 4
    assert calculator.mul(6, 0) == 0
    assert calculator.mul(-6, 7) == -42
