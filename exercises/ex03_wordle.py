"""Wordle!"""
__author__ = "350605138"


def contains_char(string_1: str, string_2: str) -> bool:
    """This takes in a string a nd a character and sees if the character is a substring of the character."""
    assert len(string_2) == 1
    counter = 0
    while (len(string_1) > counter):
        if string_1[counter] == string_2:
            return True
        else:
            counter += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Takes a guess and secret word turn it into its repective emoji."""
    assert len(guess) == len(secret)
    counter = 0
    out = ""
    y_b = "\U0001F7E8"
    g_b = "\U0001F7E9"
    w_b = "\U00002B1C"
    while (len(secret) > counter):
        if secret[counter] == guess[counter]:
            out += g_b
        elif contains_char(secret, guess[counter]):
            out += y_b
        else:
            out += w_b
        counter += 1
    return out


def input_guess(length: int) -> str:
    """Makes sure guess is right length."""
    guess = input(f"Enter a {length} character word:")
    while True:
        if len(guess) == length:
            return guess
        else:
            guess = input(f"That wasn't {length} chars! Try again:") 


def main() -> None:
    """Main function initilizes the game."""
    n = 1
    secret = "codes"
    while (n < 7):
        print(f"=== Turn {n}/6 ===")
        guess = input_guess(len(secret))
        emoji = emojified(guess, secret)
        print(emoji)        
        if guess == secret:
            print(f"You won in {n}/6 turns!")
            return None
        n += 1
    print("X/6 - sorry, try again tomorrow!")
    return None


if __name__ == "__main__":
    main()
