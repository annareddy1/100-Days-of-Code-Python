print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

def ask_choice(prompt, valid_options):
    """
    Repeatedly asks the user a question until they type one of the valid options.

    prompt: the question to show the user
    valid_options: a list like ["left", "right"]

    Returns the user's choice (already cleaned).
    """
    while True:
        # input() returns a string.
        # .strip() removes extra spaces at both ends (e.g., " left " -> "left")
        # .lower() normalizes capitalization (e.g., "LEFT" -> "left")
        answer = input(prompt).strip().lower()

        # If the cleaned answer is valid, return it.
        if answer in valid_options:
            return answer

        # Otherwise, show a helpful message and ask again.
        print(f'Please type one of: {", ".join(valid_options)}')


choice1 = ask_choice(
    'You\'re at a crossroad, where do you want to go? Type "left" or "right".\n',
    ["left", "right"]
)

if choice1 == "left":
    choice2 = ask_choice(
        'You\'ve come to a lake. There is an island in the middle of the lake. '
        'Type "wait" to wait for a boat. Type "swim" to swim across.\n',
        ["wait", "swim"]
    )

    if choice2 == "wait":
        choice3 = ask_choice(
            "You arrive at the island unharmed. There is a house with 3 doors: "
            "red, yellow, and blue. Which colour do you choose?\n",
            ["red", "yellow", "blue"]
        )

        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        else:  # blue
            print("You enter a room of beasts. Game Over.")

    else:  # swim
        print("You got attacked by an angry trout. Game Over.")

else:  # right
    print("You fell into a hole. Game Over.")