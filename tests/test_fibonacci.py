from app.fibonacci import fibonacci

def test_fibonacci():
    assert fibonacci(6) == 8
    assert fibonacci(12) == 144
    assert fibonacci(15) == 610
    assert fibonacci(21) == 10946