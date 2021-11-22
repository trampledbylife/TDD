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

def test_memory_clear():
    calculator = Calculator()
    assert calculator.memory == 0
    calculator.memory = 1000
    calculator.memory_clear()
    assert (calculator.memory == 0)
    calculator.memory_clear()
    assert (calculator.memory == 0)
    calculator.memory = -34
    calculator.memory_clear()
    assert (calculator.memory == 0)

def test_memory_add():
    calculator = Calculator()
    assert calculator.memory == 0
    assert(calculator.memory_add(5) == 5)
    assert(calculator.memory == 5)
    calculator.memory = 5
    assert(calculator.memory_add(7) == 12)
    assert(calculator.memory == 12)
    calculator.memory = -33
    assert(calculator.memory_add(0) == -33)
    assert(calculator.memory == -33)
    calculator.memory = -33
    assert (calculator.memory_add(-7) == -40)
    assert(calculator.memory == -40)

def test_memory_sub():
    calculator = Calculator()
    assert calculator.memory == 0
    assert(calculator.memory_sub(5) == -5)
    assert(calculator.memory == -5)
    calculator.memory = -5
    assert(calculator.memory_sub(7) == -12)
    assert(calculator.memory == -12)
    calculator.memory = -33
    assert(calculator.memory_sub(0) == -33)
    assert(calculator.memory == -33)
    calculator.memory = -33
    assert (calculator.memory_sub(-7) == -26)
    assert(calculator.memory == -26)



