# OOP Lesson: We IMPORT classes so we can create objects from them
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# OOP Lesson: OBJECTS are real things created from classes
money_machine = MoneyMachine()   # object that handles money
coffee_maker = CoffeeMaker()     # object that makes coffee
menu = Menu()                    # object that stores drinks

# Program control variable
is_on = True

# Main program loop (keeps the coffee shop running)
while is_on:

    # OOP Lesson: calling a METHOD of the menu object
    options = menu.get_items()

    # Ask the user what drink they want
    choice = input(f"What would you like? ({options}): ")

    # Turn the machine off
    if choice == "off":
        is_on = False

    # Show machine report
    elif choice == "report":

        # OOP Lesson: objects perform their own actions (METHODS)
        coffee_maker.report()
        money_machine.report()

    else:
        # OOP Lesson: objects can return other objects
        drink = menu.find_drink(choice)

        # OOP Lesson: objects work together (COMPOSITION)
        # coffee_maker checks ingredients
        # money_machine checks payment
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):

            # CoffeeMaker object performs the action
            coffee_maker.make_coffee(drink)