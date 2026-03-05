# OOP Lesson: A CLASS is a blueprint for a machine.
# CoffeeMaker is the blueprint for a coffee-making robot.
class CoffeeMaker:

    # OOP Lesson: __init__ is the CONSTRUCTOR.
    # It runs when we create a CoffeeMaker object.
    def __init__(self):

        # OOP Lesson: ATTRIBUTES are things the object remembers.
        # This machine remembers how many ingredients it has.
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    # OOP Lesson: METHODS are actions the object can do.
    # This method shows what ingredients are left.
    def report(self):
        """Print remaining resources"""

        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    # This method checks if we have enough ingredients for a drink
    def is_resource_sufficient(self, drink):
        """Return True if ingredients are enough"""

        can_make = True

        # Look at each ingredient the drink needs
        for item in drink.ingredients:

            # If the machine has less than needed
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False

        return can_make

    # This method uses ingredients to make the coffee
    def make_coffee(self, order):
        """Use ingredients and make the drink"""

        # Reduce ingredients used for the drink
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]

        # Tell the user the coffee is ready
        print(f"Here is your {order.name} ☕️. Enjoy!")