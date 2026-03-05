# This class is like the money box inside the coffee machine.
# It knows how to take coins and check if the user paid enough.
class MoneyMachine:

    # This is the symbol used for money
    CURRENCY = "$"

    # These are the values of each coin
    COIN_VALUES = {
        "quarters": 0.25,  # one quarter = 25 cents
        "dimes": 0.10,     # one dime = 10 cents
        "nickles": 0.05,   # one nickel = 5 cents
        "pennies": 0.01    # one penny = 1 cent
    }

    # This runs when the money machine starts
    def __init__(self):

        # Total money the coffee machine has earned
        self.profit = 0

        # Money the user just inserted
        self.money_received = 0

    # This function shows how much money the machine has made
    def report(self):
        """Prints the current profit"""

        # Print the total money earned
        print(f"Money: {self.CURRENCY}{self.profit}")

    # This function asks the user to insert coins
    def process_coins(self):
        """Returns the total calculated from coins inserted."""

        # Tell the user to insert coins
        print("Please insert coins.")

        # Go through each type of coin
        for coin in self.COIN_VALUES:

            # Ask how many of that coin the user inserted
            # Multiply by the coin value to calculate the money
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]

        # Return the total money inserted
        return self.money_received

    # This function checks if the user paid enough for the drink
    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""

        # First ask the user to insert coins
        self.process_coins()

        # Check if the user gave enough money
        if self.money_received >= cost:

            # Calculate change to give back
            change = round(self.money_received - cost, 2)

            # Tell the user their change
            print(f"Here is {self.CURRENCY}{change} in change.")

            # Add the drink cost to the machine's profit
            self.profit += cost

            # Reset money received for the next user
            self.money_received = 0

            # Payment successful
            return True

        else:
            # If the money is not enough
            print("Sorry that's not enough money. Money refunded.")

            # Reset money received
            self.money_received = 0

            # Payment failed
            return False