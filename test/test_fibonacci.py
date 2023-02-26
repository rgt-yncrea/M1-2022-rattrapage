import pytest
from src.fibonacci.fibonacci import fibonacci

#on creer une fonction qui nous permettra de  tester les 4 premiere valeur de la fonction de fibonacci
def test_fibonacci():
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3