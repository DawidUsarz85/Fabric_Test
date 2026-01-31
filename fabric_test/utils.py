"""Utility helpers for Fabric_Test repo.

Small, testable helpers extracted from notebooks.
"""

from typing import Iterable, List


def filter_even_numbers(numbers: Iterable[int]) -> List[int]:
    """Return even numbers from the given iterable, preserving order."""
    return [n for n in numbers if n % 2 == 0]
