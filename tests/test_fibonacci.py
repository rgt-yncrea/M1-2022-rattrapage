# tests_fibonacci.py

from functools import lru_cache
import pytest

@lru_cache(maxsize=1000)
def fibonacci(n: int):
    return 1 if (n == 1 or n == 2) else fibonacci(n - 1) + fibonacci(n - 2)

def test_fibonacci():
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
    assert fibonacci(10) == 55

def test_fibonacci_with_negative_input():
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_fibonacci_with_invalid_type_input():
    with pytest.raises(TypeError):
        fibonacci('test')
        