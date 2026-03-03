# Get the pretty calculator logo
import art


# Adds two numbers
def add(n1, n2):
    return n1 + n2


# Subtracts second number from first
def subtract(n1, n2):
    return n1 - n2


# Multiplies two numbers
def multiply(n1, n2):
    return n1 * n2


# Divides first number by second
def divide(n1, n2):
    return n1 / n2


# This dictionary matches a symbol to the function that does the math
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Example: operations["*"](4, 8) would run multiply(4, 8)


def calculator():
    # Show the logo at the start
    print(art.logo)

    # This keeps one calculation session running
    should_accumulate = True

    # Ask for the first number
    num1 = float(input("What is the first number?: "))

    # Keep doing more math until user says stop
    while should_accumulate:

        # Show all possible symbols
        for symbol in operations:
            print(symbol)

        # Ask which math sign to use
        operation_symbol = input("Pick an operation: ")

        # Ask for the next number
        num2 = float(input("What is the next number?: "))

        # Pick the right function from the dictionary and run it
        answer = operations[operation_symbol](num1, num2)

        # Show the math and the result
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Ask if we keep going with the answer or start over
        choice = input(
            f"Type 'y' to continue calculating with {answer}, "
            "or type 'n' to start a new calculation: "
        )

        # If yes, the answer becomes the new first number
        if choice == "y":
            num1 = answer
        else:
            # If no, stop this loop and restart fresh
            should_accumulate = False
            print("\n" * 20)  # Clear screen by pushing old text away
            calculator()      # Start a brand new calculator session


# Start the program
calculator()