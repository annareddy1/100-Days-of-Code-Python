import random

# TODO-1: Update the word list to use the word_list from hangman_words.py
# We import word_list from hangman_words so we can randomly choose a word from that list.
from hangman_words import word_list

# TODO-2: Update the code to use the stages from the file hangman_art.py
# TODO-3: Import the logo from hangman_art.py and print it at the start of the game.
# We import stages (hangman pictures) and logo (game banner) from hangman_art.
from hangman_art import stages, logo

# Total lives (matches the length of stages - 1 in the course setup)
lives = 6

# TODO-3: Print the logo at the start of the game.
print(logo)

# Choose a random word from the imported word list (TODO-1)
chosen_word = random.choice(word_list)

# NOTE: This print is usually for debugging; remove it in final version so the answer isn't shown.
print(chosen_word)

# Create the starting placeholder using underscores, one for each letter in chosen_word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print("Word to guess: " + placeholder)

# Track if the game has ended
game_over = False

# Store letters that have been correctly guessed so far
correct_letters = []

while not game_over:

    # TODO-6: Show how many lives the user has left.
    # We use f-string to insert current lives into the display.
    print(f"****************************{lives}/6 LIVES LEFT****************************")

    # Ask the user for a guess, and normalize to lowercase
    guess = input("Guess a letter: ").lower()

    # TODO-4: If the user already guessed this letter, tell them.
    # IMPORTANT: We do NOT deduct a life here.
    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    # Build the display string based on the guess and previously correct letters
    display = ""

    for letter in chosen_word:
        # If the current letter matches the new guess, reveal it
        if letter == guess:
            display += letter
            # Add to correct_letters so we remember it for future rounds
            correct_letters.append(guess)
        # If this letter was guessed previously, show it
        elif letter in correct_letters:
            display += letter
        # Otherwise keep it hidden
        else:
            display += "_"

    print("Word to guess: " + display)

    # TODO-5: If guess is not in the chosen word, deduct a life and print the message.
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        # If lives reach 0, user loses and game ends
        if lives == 0:
            game_over = True

            # TODO-7: Show the correct word when the user loses.
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    # If there are no underscores left, user has guessed the whole word
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: Use the stages art from hangman_art.py
    # stages[lives] shows the correct hangman stage for remaining lives.
    print(stages[lives])