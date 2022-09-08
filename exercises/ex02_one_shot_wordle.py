"""EX02 : One Shot Wordle"""
__author__ = "730509674"


secret: str = "python"
guessed_word: str = input("What is your 6-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

color_box: str = ""
index_of_word: int = 0


while len(guessed_word) != len(secret):
    guessed_word = input(f"That was not {len(secret)} letters! Try again: ")
if guessed_word == secret:
    while index_of_word < len(secret):
        color_box += GREEN_BOX
        index_of_word += 1
    print(color_box)
    print("Woo! You got it!")
else:
    while index_of_word < len(secret):
        if guessed_word[index_of_word] == secret[index_of_word]:
            color_box += GREEN_BOX
        else:
            in_secret: bool = False
            index_of_secret: int = 0
            while not in_secret and index_of_secret < len(secret):
                if secret[index_of_secret] == guessed_word[index_of_word]:
                    in_secret = True
                else:
                    index_of_secret += 1
            if in_secret:
                color_box += YELLOW_BOX
            else:
                color_box += WHITE_BOX
        index_of_word += 1
    print (color_box)
    print("Not quite. Play again soon!")

