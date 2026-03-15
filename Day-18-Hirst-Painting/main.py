import turtle as turtle_module
import random

# Enable RGB color mode (0–255 instead of default 0–1)
turtle_module.colormode(255)

# Create turtle object
tim = turtle_module.Turtle()

# Configure turtle for fast drawing and hide cursor
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# Color palette extracted from a Hirst-style painting
color_list = [
    (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135),
    (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185),
    (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
    (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77),
    (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90),
    (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
    (107, 127, 153), (174, 94, 97), (176, 192, 209)
]

# Move turtle to starting position (bottom-left of grid)
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

# Total number of dots to draw
number_of_dots = 100

# Draw dots in a 10x10 grid
for dot_count in range(1, number_of_dots + 1):

    # Draw a colored dot at the current position
    tim.dot(20, random.choice(color_list))

    # Move forward to the next position in the row
    tim.forward(50)

    # After every 10 dots, move to the next row
    if dot_count % 10 == 0:
        tim.setheading(90)   # Move up
        tim.forward(50)
        tim.setheading(180)  # Move back to row start
        tim.forward(500)
        tim.setheading(0)    # Face forward again

# Keep window open until user clicks
screen = turtle_module.Screen()
screen.exitonclick()