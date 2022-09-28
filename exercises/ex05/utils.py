"""Writing code to be unit tested."""
__author__ = "730509674"


def only_evens(input: list[int]) -> list[int]:
    """This function looks through a given list, and returns a new list with only the even numbers from that list."""
    evens_list: list[int] = []
    for number in input:
        if number % 2 == 0:
            evens_list.append(number)
    return evens_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """This function takes two given lists annd combines them to make one list."""
    final_list: list[int] = []
    for number in first_list:
        final_list.append(number)
    for number in second_list:
        final_list.append(number)
    return final_list


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """This function takes a given list and returns a list based on the start and end indices given."""
    end_list: list[int] = []
    if a_list == [] or start > len(a_list) or end < 1:
        return end_list
    if start < 0:
        start = 0
    if end > len(a_list):
        end = len(a_list)
    i = start
    while i < end:
        end_list.append(a_list[i])
        i += 1
    return end_list
