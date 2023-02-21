import pytest
from src.fibonacci.fibonacci import fibonacci
#test des 4 premiers valeurs de la suite de fibonacci

def test_fibonacci():
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5


