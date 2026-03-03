from random import randint
from art import logo

# Easy mode gives more tries, hard mode gives less tries
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Checks if the guess is too high, too low, or correct
def check_answer(user_guess, actual_answer, turns):
    """Returns turns left after checking the guess."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1  # you used up 1 try
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1  # you used up 1 try
    else:
        print(f"You got it! The answer was {actual_answer}")
        # no return needed here because game ends when guess == answer


# Picks how many tries the user gets
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # Show the logo
    print(logo)

    # Say hello and explain the game
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Pick the secret number
    answer = randint(1, 100)

    # (Cheat line) shows the answer
    print(f"Pssst, the correct answer is {answer}")

    # Get number of tries based on difficulty
    turns = set_difficulty()

    # Start with a wrong guess so the loop begins
    guess = 0

    # Keep looping until the guess is correct
    while guess != answer:
        # Tell user how many tries are left
        print(f"You have {turns} attempts remaining to guess the number.")

        # Ask user for a guess
        guess = int(input("Make a guess: "))

        # Check guess and reduce tries if wrong
        turns = check_answer(guess, answer, turns)

        # If no tries left, game ends
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return

        # If still wrong, tell them to try again
        elif guess != answer:
            print("Guess again.")


# Start the game
game()