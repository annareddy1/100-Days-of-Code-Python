# Import the random module to generate random characters
import random


# List of all possible letters (lowercase + uppercase)
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]

# List of possible numeric characters
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of possible special characters
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Intro message
print("Welcome to the PyPassword Generator!")


# Take user input and convert to integers
# These represent how many characters of each type are required
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


# -----------------------------
# EASY LEVEL (Sequential Order)
# -----------------------------
# In this version, characters are added in strict order:
# Letters first → then symbols → then numbers.
# The final password will always follow a predictable pattern.

"""
password = ""

# Add random letters
for char in range(0, nr_letters):
    password += random.choice(letters)

# Add random symbols
for char in range(0, nr_symbols):
    password += random.choice(symbols)

# Add random numbers
for char in range(0, nr_numbers):
    password += random.choice(numbers)

print(password)
"""


# -----------------------------
# HARD LEVEL (Randomized Order)
# -----------------------------
# In this version, we:
# 1. Store all characters in a list
# 2. Shuffle the list randomly
# 3. Join the list into a string


# Create an empty list to store password characters
password_list = []


# Add random letters to the list
# random.choice(list_name) picks a random element from the list
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))


# Add random symbols to the list
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))


# Add random numbers to the list
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))


# At this stage, the list might look like:
# ['a', 'K', 'd', '!', '%', '7', '2']
# But the order is still grouped (letters first, etc.)
print(password_list)


# Shuffle the list randomly (in-place)
# This modifies the list directly
random.shuffle(password_list)

# Now the list order is randomized
print(password_list)


# Convert the shuffled list into a single string
# We iterate through each character in the list
password = ""

for char in password_list:
    password += char


# Final output
print(f"Your password is: {password}")