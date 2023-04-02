"""one Shot Wordle."""
__author__ = "730605138"
secret_word = "python"
correct_format = True
first = True
while correct_format:
    if first:
        guess = input(f"What is your {len(secret_word)}-letter guess?")
        first = False
    else:
        guess = input(f"That was not {len(secret_word)} letters! Try again:")
    if len(guess) == len(secret_word):
        correct_format = False
        count = 0
        emoji = ""
        while count < len(secret_word):
            if secret_word[count] == guess[count]:
                emoji += "\U0001F7E9"
            else:
                count2 = 0
                other_occurance = False
                while count2 < len(secret_word):
                    if guess[count] == secret_word[count2]:
                        other_occurance = True
                        count2 = len(secret_word) + 1
                    else:
                        count2 += 1
                if other_occurance:
                    emoji += "\U0001F7E8"
                else:
                    emoji += "\U00002B1C"
            count += 1
        print(emoji)  
        if guess == secret_word:
            print("Woo! You got it!")
        else:
            print("Not Quite. Play again soon!")
