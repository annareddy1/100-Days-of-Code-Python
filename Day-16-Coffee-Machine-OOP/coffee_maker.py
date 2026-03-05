# This class represents a coffee machine.
# Think of it like a robot that knows how to make coffee.
class CoffeeMaker:

    # This runs when we first create the coffee machine.
    # It tells the machine how much water, milk, and coffee it has.
    def __init__(self):
        # The machine has some ingredients stored inside it.
        self.resources = {
            "water": 300,   # 300 ml of water
            "milk": 200,    # 200 ml of milk
            "coffee": 100,  # 100 grams of coffee powder
        }

    # This function shows us how much ingredients are left.
    def report(self):
        """Prints a report of all resources."""

        # Show how much water is left
        print(f"Water: {self.resources['water']}ml")

        # Show how much milk is left
        print(f"Milk: {self.resources['milk']}ml")

        # Show how much coffee powder is left
        print(f"Coffee: {self.resources['coffee']}g")

    # This function checks if the machine has enough ingredients
    # to make the drink someone asked for.
    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""

        # Assume we can make the drink
        can_make = True

        # Look at each ingredient the drink needs
        for item in drink.ingredients:

            # If the drink needs more than what we have
            if drink.ingredients[item] > self.resources[item]:

                # Tell the user we don't have enough
                print(f"Sorry there is not enough {item}.")

                # We cannot make the drink
                can_make = False

        # Return True or False depending on whether we can make it
        return can_make

    # This function actually makes the coffee.
    # It uses up the ingredients from the machine.
    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""

        # For each ingredient the drink needs
        for item in order.ingredients:

            # Subtract the amount used from the machine's storage
            self.resources[item] -= order.ingredients[item]

        # Tell the user their coffee is ready
        print(f"Here is your {order.name} ☕️. Enjoy!")