from ..src.fibonacci.fibonacci import fibonacci
import pytest

def tests_fibonacci():
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
    assert fibonacci(20) == 6765
    assert fibonacci(30) == 832040
    assert fibonacci(40) == 102334155
