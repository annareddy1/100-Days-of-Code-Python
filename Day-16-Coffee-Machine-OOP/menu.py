# OOP Lesson: A CLASS is a blueprint.
# MenuItem is the blueprint for one drink.
class MenuItem:

    """Models each Menu Item."""

    # OOP Lesson: __init__ is the CONSTRUCTOR.
    # It runs when we create a new drink object.
    def __init__(self, name, water, milk, coffee, cost):

        # OOP Lesson: ATTRIBUTES are things the object remembers
        self.name = name   # drink name
        self.cost = cost   # drink price

        # Ingredients needed to make this drink
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


# OOP Lesson: Another CLASS that manages many drinks.
# Menu is like a manager that holds all MenuItem objects.
class Menu:

    """Models the Menu with drinks."""

    # CONSTRUCTOR: runs when a Menu object is created
    def __init__(self):

        # OOP Lesson: OBJECTS created from MenuItem class
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    # OOP Lesson: METHODS are actions objects can do
    def get_items(self):
        """Returns the names of drinks on the menu"""

        options = ""

        # Look at each drink object in the menu
        for item in self.menu:
            options += f"{item.name}/"

        return options

    # This method searches for a drink by name
    def find_drink(self, order_name):

        """Find and return the drink object"""

        for item in self.menu:

            # If the drink name matches the order
            if item.name == order_name:
                return item

        # If the drink does not exist
        print("Sorry that item is not available.")