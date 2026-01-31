import pytest

from fabric_test.utils import filter_even_numbers


def test_filter_even_numbers_basic():
    assert filter_even_numbers([1, 2, 3, 4, 5]) == [2, 4]


def test_filter_even_numbers_empty():
    assert filter_even_numbers([]) == []


def test_filter_even_numbers_iterable():
    assert filter_even_numbers(range(1, 6)) == [2, 4]
