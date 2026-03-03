# Import the random module to allow the computer to make random choices
import random


# ASCII art for Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# ASCII art for Paper
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

# ASCII art for Scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Store all three options inside a list.
# Index positions:
# 0 → Rock
# 1 → Paper
# 2 → Scissors
game_images = [rock, paper, scissors]


# Ask the user to choose between Rock (0), Paper (1), or Scissors (2)
# Convert input from string to integer so we can compare numbers
user_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
))


# Validate user input BEFORE accessing the list.
# If the number is within valid range (0 to 2), print their chosen ASCII art.
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])


# Generate a random number between 0 and 2 for the computer
# random.randint(0, 2) includes both 0 and 2
computer_choice = random.randint(0, 2)

print("Computer chose:")
print(game_images[computer_choice])


# If user typed an invalid number (less than 0 or greater than 2)
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")


# Special win case:
# Rock (0) beats Scissors (2)
elif user_choice == 0 and computer_choice == 2:
    print("You win!")


# Special lose case:
# Scissors (2) loses to Rock (0)
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")


# If computer's number is greater, user loses
# (Except the special case above which we already handled)
elif computer_choice > user_choice:
    print("You lose!")


# If user's number is greater, user wins
elif user_choice > computer_choice:
    print("You win!")


# If both choices are equal → draw
elif computer_choice == user_choice:
    print("It's a draw!")