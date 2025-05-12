from src.math_operations import add, sub

def test_add():
    assert add(5, 2) == 7
    assert add(50, 2) == 52
    assert add(10, 12) == 22


def test_sub():
    assert sub(5, 2) == 3
    assert sub(50, 2) == 48
    assert sub(5, 7) == -2
    