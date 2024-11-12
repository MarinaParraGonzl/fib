from fib import fibonacci_iterative
from fib import fibonacci_recursive_memoization
import pytest


def test_fib_9_is_34():
    assert fibonacci_iterative(9)==34


def test_fib_negative_raise_error():
    with pytest.raises(ValueError):
        fibonacci_iterative(-1)


def test_fibonacci_recursive_memoization():
    assert fibonacci_recursive_memoization(9)==34