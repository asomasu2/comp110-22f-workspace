"""Tests for the utils functions."""
__author__ = "730509674"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Testing the function with an empty list."""
    assert only_evens([]) == []


def test_only_evens_normal_list() -> None:
    """Testing the function with a normal list with even and odd integers."""
    assert only_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 4, 6, 8, 10]


def test_only_evens_odd_list() -> None:
    """Testing the function with a list of only odd integers."""
    assert only_evens([1, 3, 5, 7, 9]) == []


def test_concat_two_empty_lists() -> None:
    """Testing if the function returns an empty list with two empty lists at the beginning."""
    assert concat([], []) == []


def test_concat_normal_lists() -> None:
    """Testing if the function returns a combined list with the integers from both of the lists."""
    assert concat([1, 2, 30, 115], [3, 80, 25]) == [1, 2, 30, 115, 3, 80, 25]


def test_concat_more_normal_lists() -> None:
    """Testing if the function returns a combined list with the integers from both of the lists."""
    assert concat([], [3, 90]) == [3, 90]


def test_sub_large_end() -> None:
    """Testing to see if the function reassigns the end value when it is larger than the length of the list, so that the end value is the last value in the list."""
    assert sub([1, 4, 7], -40, 4) == [1, 4, 7]


def test_sub_normal_list() -> None:
    """Testing to see if the function returns a new list with values from the start value up to the end value."""
    assert sub([5, 8, 9, 10, 356], 1, 5) == [8, 9, 10, 356]


def test_sub_another_normal_list() -> None:
    """Testing to see if the function returns a new list with values from the start value up to the end value."""
    assert sub([1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6], 4, 9) == [5, 6, 7, 8, 1]
