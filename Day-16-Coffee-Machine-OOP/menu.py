# This class represents ONE drink on the menu.
# Like one card on a restaurant menu that says what the drink needs.
class MenuItem:

    """Models each Menu Item."""

    # This runs when we create a new drink.
    # It stores the drink's name, ingredients, and price.
    def __init__(self, name, water, milk, coffee, cost):

        # The name of the drink (latte, espresso, etc.)
        self.name = name

        # How much the drink costs
        self.cost = cost

        # A list of ingredients needed to make the drink
        self.ingredients = {
            "water": water,    # How much water the drink needs
            "milk": milk,      # How much milk the drink needs
            "coffee": coffee   # How much coffee powder it needs
        }


# This class represents the whole menu of the coffee shop.
# Think of it like the big menu board in a café.
class Menu:

    """Models the Menu with drinks."""

    # This runs when the menu is created.
    def __init__(self):

        # We create a list of drinks the shop can make.
        self.menu = [

            # Latte drink
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),

            # Espresso drink
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),

            # Cappuccino drink
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    # This function shows all the drinks available on the menu.
    def get_items(self):
        """Returns all the names of the available menu items"""

        # Start with an empty string
        options = ""

        # Go through every drink in the menu
        for item in self.menu:

            # Add the drink name to the options list
            options += f"{item.name}/"

        # Return something like "latte/espresso/cappuccino/"
        return options

    # This function looks for the drink the user asked for.
    def find_drink(self, order_name):

        """Searches the menu for a particular drink by name"""

        # Look at each drink in the menu
        for item in self.menu:

            # If the name matches what the user asked for
            if item.name == order_name:

                # Give back that drink object
                return item

        # If the drink does not exist in the menu
        print("Sorry that item is not available.")