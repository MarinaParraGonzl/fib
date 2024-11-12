import argparse
from functools import cache


def fibonacci_iterative(n: int) -> int:
    """
    Computes the n-th Fibonacci number
    :param n: i-th Fibonacci number
    :return: The n-th fibonacci number
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


@cache
def fibonacci_recursive(n: int) -> int:
    """
    Computes the n-th Fibonacci number
    :param n: i-th Fibonacci number
    :return: The n-th fibonacci number
    """
    if n < 0:
        raise ValueError("n must be greater than or equal to zero.")
    if n < 2:
        return n

    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)




# return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('nth', type=int, help="Nth fibonacci number.")  # positional argument
    args = parser.parse_args()

    result = fibonacci_recursive(args.nth)
    print(result)
