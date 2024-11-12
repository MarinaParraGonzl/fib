import argparse

def fibonacci_iterative(n: int) -> int:
    """
    Computes the i-th Fibonacci number
    :param n: i-th Fibonacci number
    :return: The ni-th fibonacci number
    """
    if n < 0:
        raise ValueError("n must be greater than or equal to zero.")
    if n < 2:
        return n

    n0 = 0
    n1 = 1
    nth = 0

    for _ in range(n - 1):
        nth = n0 + n1
        n0 = n1
        n1 = nth
    return nth


def fibonacci_recursive(n: int) -> int:
    """
    Computes the i-th Fibonacci number
    :param n: i-th Fibonacci number
    :return: The i-th fibonacci number
    """
    if n < 0:
        raise ValueError("n must be greater than or equal to zero.")
    if n < 2:
        return n
    n0 = 0
    n1 = 1
    for _ in range(n):
        nth = n0 + n1
        n0 = n1n1 = nth
    return n0

from functools import cache


@cache
def fibonacci_recursive_memoization(n: int) -> int:
    """
    Computes the n-th Fibonacci number using a recursive method with memoization.
    :param n: n-th Fibonacci number
    :return: The n-th fibonacci number
    """
    if n < 0:
        raise ValueError("n must be greater than or equal to zero.")
    if n < 2:
        return n
    return fibonacci_recursive_memoization(n-1) + fibonacci_recursive_memoization(n-2)

# return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('nth', type=int, help="Nth fibonacci number.")  # positional argument
    args = parser.parse_args()

    result = fibonacci_iterative(args.nth)
    print(result)
