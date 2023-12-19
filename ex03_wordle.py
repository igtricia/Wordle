"""EX03 - Structured Wordle."""

__author__ = "730608965"


def contains_char(word: str, letter: str) -> bool:
    """Checks if the character is found at any index in the word and returns true if it is."""
    assert len(letter) == 1
    
    count: int = 0
    while count < len(word):
        if letter == word[count]:
            count = len(word) + 1
        else:
            count = count + 1

    if count == len(word):
        return False
    else:
        return True


def emojified(guess_word: str, secret_word: str) -> str: 
    """Returns coloured emoji boxes based off of how well the guess word matches the secret word."""
    assert len(guess_word) == len(secret_word)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    resulting_emoji: str = ""

    index: int = 0
    while index < len(guess_word):
        if guess_word[index] == secret_word[index]:
            resulting_emoji = resulting_emoji + GREEN_BOX
        else:
            result: bool = contains_char(secret_word, guess_word[index])
            if result is True: 
                resulting_emoji = resulting_emoji + YELLOW_BOX
            else:
                resulting_emoji = resulting_emoji + WHITE_BOX
        index = index + 1
    return resulting_emoji


def input_guess(expected_length: int) -> str:
    """Prompts the user for input of a certain length and returns the guess."""
    user_input: str = input(f"Enter a {expected_length} character word: ")

    while len(user_input) != expected_length:
        user_input1 = input(f"That wasn't {expected_length} chars! Try again: ")
        user_input = user_input1

    return user_input


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    number_of_turns: int = 1
    while number_of_turns < 7:
        print(f"=== Turn {number_of_turns}/6 ===")
        guess_word = input_guess(5)
        print(emojified(guess_word, secret_word))
        
        if guess_word == secret_word:
            print(f"You won in {number_of_turns}/6 turns! ")
            number_of_turns = 8
        else:
            number_of_turns = number_of_turns + 1

    if number_of_turns == 7:
        print("X/6 - Sorry, try again tomorrow! ")


if __name__ == "__main__":
    main()