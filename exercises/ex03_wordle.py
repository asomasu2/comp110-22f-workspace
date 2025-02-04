"""Structured Wordle!"""
__author__ = "730509674"


def contains_char(word: str, letter: str) -> bool:
    """Searches for a certain letter in a certain word."""
    assert len(letter) == 1
    word_index: int = 0
    letter_not_in_word: bool = True
    while word_index < len(word) and letter_not_in_word: 
        if letter == word[word_index]:
            letter_not_in_word = False
            return True
        else:
            letter_not_in_word = True
        word_index += 1
    if letter_not_in_word:
        return False


def emojified(guess: str, secret: str) -> str:
    """Adds the color to the boxes so we know if certain letters are in the right place, in the word but wrong space, or not in the word."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    color_box: str = ""
    index_of_word: int = 0 
    while index_of_word < len(secret):
        if guess[index_of_word] == secret[index_of_word]:
            color_box += GREEN_BOX
        elif contains_char(secret, guess[index_of_word]):
            color_box += YELLOW_BOX
        else:
            color_box += WHITE_BOX
        index_of_word += 1
    return color_box


def input_guess(characters_in_guess: int) -> str:
    """Tells the user how many characters should be in their guess."""
    guess: str = input(f"Enter a {characters_in_guess} character word: ")
    while len(guess) != characters_in_guess:
        guess = input(f"That wasn't {characters_in_guess} chars! Try again: ")
    return guess


def main() -> None:
    """Running the actual wordle."""
    turn: int = 1
    game_not_over: bool = True
    secret: str = "codes"
    while turn < 7 and game_not_over:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret)) 
        print(emojified(guess, secret))
        if guess == secret:
            game_not_over = False
            print(f"You won in {turn}/6 turns!")
        else:
            turn += 1
    if turn == 7 and game_not_over:
        print(" X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()