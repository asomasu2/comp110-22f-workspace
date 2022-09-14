"""Structured Wordle"""
__author__ = "730509674"

def contains_char(word: str, letter: str) -> bool:
    assert len(letter) == 1
    word_index: int = 0
    letter_in_word: bool = False
    while word_index < len(word) and letter_in_word == False:
        if letter == word[word_index]:
            letter_in_word = True
        else:
            letter_in_word = False
        word_index += 1
    if letter_in_word == True:
        return True
    else:
        return False

def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    color_box: str = ""
    index_of_word: int = 0
    if guess == secret:
        while index_of_word < len(secret):
            color_box += GREEN_BOX
            index_of_word += 1
        print(color_box)
    else:
        while index_of_word < len(secret):
            if guess[index_of_word] == secret[index_of_word]:
                color_box += GREEN_BOX
            else:
                in_secret: bool = False
                index_of_secret: int = 0
                while not in_secret and index_of_secret < len(secret):
                    if secret[index_of_secret] == guess[index_of_word]:
                        in_secret = True
                    else:
                        index_of_secret += 1
                if in_secret:
                    color_box += YELLOW_BOX
                else:
                    color_box += WHITE_BOX
            index_of_word += 1
        print(color_box)

