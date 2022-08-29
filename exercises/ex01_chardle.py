"""EX01 - Chardle - A cute step towards Wordle."""
__author__ = "730509674"

random_word: str = input("Enter a 5-character word: ")
if len(random_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
guessed_character: str = input("Enter a single character: ")
if len(guessed_character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + guessed_character + " in " + random_word)

matching_characters: int = 0

if random_word[0] == guessed_character:
    [print(guessed_character + " found at index 0")]
    matching_characters = matching_characters + 1
if random_word[1] == guessed_character:
    [print(guessed_character + " found at index 1")]
    matching_characters = matching_characters + 1
if random_word[2] == guessed_character:
    [print(guessed_character + " found at index 2")]
    matching_characters = matching_characters + 1
if random_word[3] == guessed_character:
    [print(guessed_character + " found at index 3")]
    matching_characters = matching_characters + 1
if random_word[4] == guessed_character:
    [print(guessed_character + " found at index 4")]
    matching_characters = matching_characters + 1

if matching_characters == 0:
    print("No instances of " + guessed_character + " found in " + random_word)
else:
    if matching_characters == 1:
        print(str(matching_characters) + " instance of " + guessed_character + " found in " + random_word) 
    else:
        print(str(matching_characters) + " instances of " + guessed_character + " found in " + random_word) 