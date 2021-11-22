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


def test_history():
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


def test_init_memory_exists():
    assert hasattr(Calculator(), 'memory')


def test_init_memory_is_list():
    assert isinstance(Calculator().memory, list)


def test_init_memory_is_empty():
    assert len(Calculator().memory) == 0


def test_memory_add_callable():
    assert callable(getattr(Calculator, 'memory_add'))


def test_memory_add_appends_memory():
    c = Calculator()
    c.memory_add(5)
    assert c.memory == [5]


def test_memory_add_makes_memory_non_empty():
    c = Calculator()
    c.memory_add(5)
    assert c.memory != []


def test_memory_add_returns_nothing():
    assert not Calculator().memory_add(5)


def test_memory_clear_callable():
    assert callable(getattr(Calculator, 'memory_clear'))


def test_memory_clear():
    c = Calculator()
    c.memory_add(5)
    c.memory_clear()
    assert c.memory == []


def test_memory_sub_callable():
    assert callable(getattr(Calculator, 'memory_sub'))


def test_memory_sub_raises_exception_on_subtracting_unknown_type():
    c = Calculator()
    with pytest.raises(TypeError):
        c.memory_sub(5)
