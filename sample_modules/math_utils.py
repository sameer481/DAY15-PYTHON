"""
Math Utilities Module (sample_modules/math_utils.py)

Demonstrates custom module functions, class exports, private helper functions (_private_helper),
and execution control (__name__ == '__main__').
"""

from typing import List, Union

__all__ = ["add", "multiply", "FactorialCalculator"]

_SECRET_CONSTANT: float = 3.1415926535


def _private_validate_numbers(numbers: List[Union[int, float]]) -> None:
    """Private module-level function used internally for input validation."""
    for n in numbers:
        if not isinstance(n, (int, float)):
            raise TypeError(f"Expected number (int/float), got {type(n).__name__}")


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Return the sum of two numbers."""
    _private_validate_numbers([a, b])
    return a + b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Return the product of two numbers."""
    _private_validate_numbers([a, b])
    return a * b


class FactorialCalculator:
    """Class encapsulated within math_utils module."""

    @staticmethod
    def compute(n: int) -> int:
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


if __name__ == "__main__":
    print("[MODULE TEST] Running standalone tests for sample_modules.math_utils...")
    print(f"add(10, 20) = {add(10, 20)}")
    print(f"multiply(5, 4) = {multiply(5, 4)}")
    print(f"FactorialCalculator.compute(5) = {FactorialCalculator.compute(5)}")
