""""""
__author__ = "730509674"


def invert(old_dict: dict[str, str]) -> dict[str,str]:
    """Function takes a dictionary and returns a new one with the values and keys from the first dictionary input switched."""
    new_dict: dict[str, str] = {}
    for key in old_dict:
        checking: str = old_dict[key]
        times: int = 0
        for value in old_dict:
            if old_dict[value] == checking:
                times += 1
            if times == 2:
                raise KeyError("You have two of the same key values for the new dictionary!")
    for key in old_dict:
        new_dict[old_dict[key]] = key
    return new_dict
    

def favorite_colors(color: dict[str, str]) -> str:
    """Function returns the color that shows up in the dictionary the most amount of times."""
    color_list = []
    color_dict: dict[str, int] = {}
    for key in color:
        color_list.append(color[key])
    for specific_color in color_list:
        times: int = 0 
        for color in color_list:
            if color == specific_color:
                times += 1
        color_dict[specific_color] = times
    highest_value: int = 0 
    highest_key: str = ""
    for key in color_dict:
        if color_dict[key] > highest_value:
            highest_key = key
            highest_value = color_dict[key]
    return highest_key


def count(input_list: list[str]) -> dict[str, int]:
    """Function takes a list input and returns a dictionary with the keys being items in the list, and the values being how many times those keys appeared in the list."""
    final_dict: dict[str, int] = {}
    for specific_item in input_list:
        times: int = 0
        for item in input_list:
            if item == specific_item:
                times += 1
        if specific_item not in final_dict:
            final_dict[specific_item] = times
    return final_dict
    
    


            







            
