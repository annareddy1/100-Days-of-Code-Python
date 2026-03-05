# Bring the menu, coffee machine, and money machine into this program
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create the machines we will use
money_machine = MoneyMachine()   # Handles coins and payments
coffee_maker = CoffeeMaker()     # Makes the coffee
menu = Menu()                    # Shows available drinks

# The machine starts turned ON
is_on = True

# Keep running the coffee machine until someone turns it off
while is_on:

    # Get the list of drinks (latte/espresso/cappuccino)
    options = menu.get_items()

    # Ask the user what drink they want
    choice = input(f"What would you like? ({options}): ")

    # If user types "off", turn the machine off
    if choice == "off":
        is_on = False

    # If user types "report", show ingredients and money
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    # Otherwise the user chose a drink
    else:
        # Find that drink in the menu
        drink = menu.find_drink(choice)

        # Check if we have enough ingredients AND the user paid enough
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):

            # If both are true, make the coffee
            coffee_maker.make_coffee(drink)