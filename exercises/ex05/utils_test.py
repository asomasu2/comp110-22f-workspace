"""Tests for the utils functions."""
__author__ = "730509674"


from exercises.ex05.utils import only_evens, sub, concat

def test_only_evens_empty() -> None:
    assert only_evens([]) == []


def test_only_evens_normal_list() -> None:
    assert only_evens([1, 2, 3, 4, 5, 6, 7, 8 , 9 ,10]) == [2, 4, 6, 8, 10]


def test_only_evens_odd_list() -> None:
    assert only_evens([1, 3, 5, 7, 9]) == []


def test_concat_two_empty_lists() -> None:
    assert concat([], []) == []


def test_concat_normal_lists() -> None:
    assert concat([1, 2, 30, 115], [3, 80, 25]) == [1, 2, 30, 115, 3, 80, 25]


def test_concat_more_normal_lists() -> None:
    assert concat([34, 50],[3, 90]) == [34, 50, 3, 90]



def test_sub_small_end() -> None:
    assert sub([1, 4, 7], -40, 0) == []

def test_sub_normal_list() -> None:
    assert sub([5, 8, 9, 10, 356], 1, 5) == [8, 9, 10, 356]

def test_sub_another_normal_list() -> None:
    assert sub([1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6], 4, 9) == [5, 6, 7, 8, 1]

