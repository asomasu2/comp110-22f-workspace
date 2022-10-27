"""Dictionary related utility functions."""

__author__ = "730509674"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(input: list[dict[str, str]], name: str) -> list[str]:
    """Produces a list of of values of the name given."""
    result: list[str] = []
    for dict in input:
        for key in dict:
            if key == name:
                result.append(dict[key])
    return result


def columnar(first_list: list[dict[str, str]]) -> dict[str, list[str]]:
    """Makes a table a list of rows into a dictionary of columns."""
    new_dict: dict[str, list[str]] = {}
    for dictionary in first_list:
        for key in dictionary:
            new_dict[key] = column_values(first_list, key)
    return new_dict


def head(old_dict: dict[str, list[str]], number: int) -> dict[str, list[str]]:
    """Makes a table with only the first N rows of data for each of the columns."""
    new_dict: dict[str, list[str]] = {}
    for key in old_dict:
        i: int = 0
        new_list: list[str] = []            
        while i < number and i < len(old_dict[key]):
            new_list.append(old_dict[key][i])
            i += 1
        new_dict[key] = new_list
    return new_dict
                
            
def select(old_dict: dict[str, list[str]], old_list: list[str]) -> dict[str, list[str]]:
    """Makes a table with only a certain set of the original columns."""
    new_dict: dict[str, list[str]] = {}
    for item in old_list:
        if item in old_dict:
            new_dict[item] = old_dict[item]
    return new_dict


def concat(dict_1: dict[str, list[str]], dict_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Makes a new dict with combination of the dictionaries given."""
    new_dict: dict[str, list[str]] = {}
    for key in dict_1:
        new_dict[key] = dict_1[key]
    for key in dict_2:
        if key not in new_dict:
            new_dict[key] = dict_2[key]
        else:
            new_list: list[str] = new_dict[key]
            for item in dict_2[key]:
                new_list.append(item)
            new_dict[key] = new_list
    return new_dict


def count(old_list: list[str]) -> dict[str, int]:
    """Counts the items in the given dictionary."""
    new_dict: dict[str, int] = {}
    for item in old_list:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    return new_dict