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


def test_div():
    calculator = Calculator()
    assert calculator.div(2, 2) == 1
    assert calculator.div(6, 3) == 2
    assert calculator.div(-6, 2) == -3
    with pytest.raises(ZeroDivisionError):
        calculator.div(2, 0)


def test_sqrt():
    calculator = Calculator()
    assert calculator.sqrt(16) == 4
    assert calculator.sqrt(0) == 0
    assert calculator.sqrt(36) == 6
    with pytest.raises(ValueError):
        calculator.sqrt(-69)


def test_hisotory():
    calculator = Calculator()
    assert calculator.history == []
    calculator.add(2, 3)
    assert calculator.history == [5]
    calculator.sub(2, 3)
    assert calculator.history == [5, -1]
    calculator.mul(2, 3)
    assert calculator.history == [5, -1, 6]
    calculator.div(2, 2)
    assert calculator.history == [5, -1, 6, 1]
    calculator.sqrt(16)
    assert calculator.history == [5, -1, 6, 1, 4]

def test_memory_add():
    c = Calculator()
    assert c.memory == 0
    c.memory_add(12)
    assert  c.memory == 12
    c.memory_add(20)
    assert  c.memory == 32

def test_memory_sub():
    c = Calculator()
    assert c.memory == 0
    c.memory_sub(12)
    assert  c.memory == -12
    c.memory_sub(20)
    assert  c.memory == -32

def test_memory_clear():
    c = Calculator()
    assert c.memory == 0
    c.memory_add(420)
    c.memory_add(42)
    c.memory_sub(69)
    assert c.memory == 393
    c.memory_clear()
    assert c.memory == 0