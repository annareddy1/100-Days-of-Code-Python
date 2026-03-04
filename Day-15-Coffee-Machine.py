# Drinks the machine can make and what they need
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,  # price of espresso
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,  # price of latte
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,  # price of cappuccino
    }
}

profit = 0  # total money earned

# Ingredients currently inside the machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Check if we have enough ingredients."""
    for item in order_ingredients:
        # If ingredient is not enough
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True  # everything is available


def process_coins():
    """Ask user to insert coins and count total money."""
    print("Please insert coins.")

    # count quarters
    total = int(input("how many quarters?: ")) * 0.25

    # add dimes
    total += int(input("how many dimes?: ")) * 0.1

    # add nickels
    total += int(input("how many nickles?: ")) * 0.05

    # add pennies
    total += int(input("how many pennies?: ")) * 0.01

    return total  # return total money inserted


def is_transaction_successful(money_received, drink_cost):
    """Check if the user paid enough."""
    if money_received >= drink_cost:

        # calculate change
        change = round(money_received - drink_cost, 2)

        print(f"Here is ${change} in change.")

        # add money to machine profit
        global profit
        profit += drink_cost

        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Make the drink and use ingredients."""
    for item in order_ingredients:
        # remove used ingredients
        resources[item] -= order_ingredients[item]

    print(f"Here is your {drink_name} ☕️. Enjoy!")


# Machine power state
is_on = True

# Machine keeps running until turned off
while is_on:

    # Ask user what drink they want
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    # Turn off machine
    if choice == "off":
        is_on = False

    # Show current resources
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    # Make a drink
    else:
        drink = MENU[choice]

        # Check ingredients first
        if is_resource_sufficient(drink["ingredients"]):

            # Take coins
            payment = process_coins()

            # Check if payment works
            if is_transaction_successful(payment, drink["cost"]):

                # Make the coffee
                make_coffee(choice, drink["ingredients"])