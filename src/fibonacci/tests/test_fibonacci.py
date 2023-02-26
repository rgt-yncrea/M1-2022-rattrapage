from functools import lru_cache



@lru_cache(maxsize=1000)
def fibonacci(n: int):
    return 1 if (n == 1 or n == 2) else fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    for i in range(1, 100):
        print(f"fibonacci({i}) = {fibonacci(i)}")

def test_fibonacci():
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
