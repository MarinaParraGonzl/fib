from fib import fibonacci_iterative
import pytest


def test_fib_9_is_34():
    assert fibonacci_iterative(9)==34
    pass


def test_fib_negative_raise_error():
    with pytest.raises(ValueError):
        fibonacci_iterative(-1)

