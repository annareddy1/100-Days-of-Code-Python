import random      # used to generate random numbers
import maths       # our own file that has the add() function


# This function changes every number in the list
def mutate(a_list):
    b_list = []     # new list where we will store changed numbers
    new_item = 0    # variable to hold the updated value

    # Go through each number in the list one by one
    for item in a_list:

        # Step 1: double the number
        new_item = item * 2

        # Step 2: add a random number between 1 and 3
        new_item += random.randint(1, 3)

        # Step 3: add the original number again using maths.add()
        new_item = maths.add(new_item, item)

        # Save the final number in the new list
        b_list.append(new_item)

    # Show the new list after all numbers are changed
    print(b_list)


# Run the function with a sample list
mutate([1, 2, 3, 5, 8, 13])