"""Testing different use cases for dictionary.py."""
__author__ = "730509674"

import pytest
from dictionary import invert, favorite_color, count


with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_invert_empty_list() -> None:
    """Making sure that an empty list is returned when the function is given an empty list."""
    assert invert({}) == {}


def test_invert_normal_list() -> None:
    """Making sure a normal list is inverted."""
    assert invert({'JJ': 'Redick', 'Matt': 'Thomas', 'Jordan': 'Nwora'}) == {'Redick': 'JJ', 'Thomas': 'Matt', 'Nwora': 'Jordan'}


def test_favorite_color_normal_dict() -> None:
    """Testing the function with a normal dictionary."""
    assert favorite_color({'arun': 'blue', 'rishi': 'blue', 'nathan': 'yellow'}) == 'blue'


def test_favorite_color_tied_highest_color() -> None:
    """Testing the function with a dictionary with the colors in the dictionary that show up all being tied for their quantity."""
    assert favorite_color({'arun': 'blue', 'rishi': 'red', 'nathan': 'yellow'}) == 'blue'


def test_favorite_color_one_key() -> None:
    """Testing the dictionary with only one key-value pair."""
    assert favorite_color({'arun': 'blue'}) == 'blue'
    
    
def test_count_normal_list() -> None:
    """Testing the function with a normal list of items."""
    assert count(['pancakes', 'eggs', 'waffles']) == {'pancakes': 1, 'eggs': 1, 'waffles': 1}


def test_count_list_with_items_iterated() -> None:
    """Testing the function with a list of items that showw up multiple times."""
    assert count(['eggs', 'eggs', 'eggs', 'milk']) == {'milk': 1, 'eggs': 3}


def test_count_empty_list() -> None:
    """Testing the funciton with an empty list."""
    assert count([]) == {}