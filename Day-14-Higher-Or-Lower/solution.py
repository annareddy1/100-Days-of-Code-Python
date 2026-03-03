# Show the game title and the VS symbol
from art import logo, vs

# Get the list of famous people with follower counts
from game_data import data

# Used to pick random people
import random


# This function turns account data into a nice sentence
def format_data(account):
    """Make the account info easy to read."""

    # Get name, job/description, and country
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]

    # Return a clean sentence
    return f"{account_name}, a {account_descr}, from {account_country}"


# This function checks if the user's guess is correct
def check_answer(user_guess, a_followers, b_followers):
    """Return True if the guess is correct."""

    # If A has more followers
    if a_followers > b_followers:
        return user_guess == "a"  # user must guess A

    # Otherwise B has more followers
    else:
        return user_guess == "b"


# Show the game logo
print(logo)

# Start score at 0
score = 0

# This controls if the game keeps going
game_should_continue = True

# Pick a random account to start as B
account_b = random.choice(data)

# Game loop (keeps running until player loses)
while game_should_continue:

    # Move previous B to become the new A
    account_a = account_b

    # Pick a new random account for B
    account_b = random.choice(data)

    # Make sure A and B are not the same person
    if account_a == account_b:
        account_b = random.choice(data)

    # Show player the first account
    print(f"Compare A: {format_data(account_a)}.")

    # Show VS art
    print(vs)

    # Show player the second account
    print(f"Against B: {format_data(account_b)}.")

    # Ask player who they think has more followers
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen so it looks cleaner
    print("\n" * 20)

    # Show logo again for the next round
    print(logo)

    # Get follower numbers for both accounts
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Check if the player's guess was correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # If player guessed right
    if is_correct:
        score += 1  # increase score
        print(f"You're right! Current score {score}")

    # If player guessed wrong
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False  # stop the game