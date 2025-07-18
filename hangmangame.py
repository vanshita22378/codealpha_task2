
import random

# Predefined list of words
word_list = ["book", "toy", "dance", "apple", "plant"]

# Randomly choose a word from the list
word = random.choice(word_list)
guessed_letters = []
tries = 6

# Create the hidden word with underscores
hidden_word = ["_" for _ in word]

print(" Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

# Main game loop
while tries > 0 and "_" in hidden_word:
    print("Word: ", " ".join(hidden_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print(" Please enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!\n")
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        tries -= 1
        print(f" Wrong guess. You have {tries} tries left.\n")
