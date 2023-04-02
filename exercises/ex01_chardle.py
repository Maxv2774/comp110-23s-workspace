"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730605138"
count = 0
word = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
letter = input("Enter a single character: ")
if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + letter + " in " + word)
if word[0] == letter:
    count += 1
    print(letter + " found at index 0")
if word[1] == letter:
    count += 1
    print(letter + " found at index 1")
if word[2] == letter:
    count += 1
    print(letter + " found at index 2")
if word[3] == letter:
    count += 1
    print(letter + " found at index 3")
if word[4] == letter:
    count += 1
    print(letter + " found at index 4")
if count == 0:
    print("No instances of " + letter + " found in " + word)
elif count == 1:
    print(str(count) + " instance of " + letter + " found in " + word)
else:
    print(str(count) + " instances of " + letter + " found in " + word)
