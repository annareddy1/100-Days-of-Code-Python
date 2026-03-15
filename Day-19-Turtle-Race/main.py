from turtle import Turtle, Screen
import random

# Set up the race window and ask the user to place a bet on a turtle color
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Define turtle colors and their starting vertical positions
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create 6 turtles, give each a unique color, and line them up at the starting point
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Start the race only if the user entered a bet
if user_bet:
    is_race_on = True

# Keep moving all turtles forward by a random distance until one crosses the finish line
while is_race_on:
    for turtle in all_turtles:

        # Check if this turtle has won the race
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            # Compare the winner with the user's bet and print the result
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Move each turtle forward by a small random amount to simulate racing
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Keep the screen open until the user clicks
screen.exitonclick()