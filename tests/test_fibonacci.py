


import pytest
import os
import sys

# construire le chemin complet vers le dossier 'fibonacci'
fibonacci_dir = os.path.join(os.path.abspath('..'), 'M1-2022-rattrapage', 'src', 'fibonacci')
sys.path.append(fibonacci_dir)


# importer les fonctions depuis le fichier 'fibonacci.py'
from fibonacci import *


def test_fibonacci_returns_integer():
    result = fibonacci.fibonacci(10)
    assert isinstance(result, int)

def test_fibonacci_first_value_is_zero():
    result = fibonacci.fibonacci(1)
    assert result == 1

def test_fibonacci_second_value_is_one():
    result = fibonacci.fibonacci(2)
    assert result == 1

def test_fibonacci_values_are_correct():
    result = fibonacci.fibonacci(10)
    assert result == 1

def test_fibonacci_raises_error_if_argument_not_positive_integer():
    with pytest.raises(ValueError):
        fibonacci.fibonacci(-1)

pytest