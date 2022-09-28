"""Practice with lists."""
__author__ = "730509674"


def all(input: list[int], number: int) -> bool:
    """Returns as true if every integer in the list matches the number entered with the function, and if not returns as false."""
    i: int = 0
    in_list: bool = True
    if len(input) == 0:
        in_list = False
        return in_list
    while i < len(input) and in_list: 
        if input[i] != number:
            in_list = False
        else:
            i += 1
    return in_list


def max(input: list[int]) -> int:
    """Returns the highest integer in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    largest_in_list: int = input[i]
    while i < len(input):
        if input[i] > largest_in_list:
            largest_in_list = input[i]
        i += 1
    return largest_in_list


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Checks to see if two lists are equal at every index or not."""
    i: int = 0
    lists_are_equal: bool = True
    if len(first_list) != len(second_list):
        lists_are_equal = False
        return lists_are_equal
    while i < len(first_list) and lists_are_equal:
        if first_list[i] != second_list[i]:
            lists_are_equal = False
            return lists_are_equal
        i += 1
    return lists_are_equal