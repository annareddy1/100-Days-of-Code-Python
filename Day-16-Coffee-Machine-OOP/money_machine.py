# OOP Lesson: A CLASS is a blueprint (like a toy design).
# This class designs a "Money Machine" that can take coins.
class MoneyMachine:

    # OOP Lesson: CLASS VARIABLES belong to the whole class (shared by all objects)
    CURRENCY = "$"

    # This dictionary tells how much each coin is worth
    COIN_VALUES = {
        "quarters": 0.25,  # 25 cents
        "dimes": 0.10,     # 10 cents
        "nickles": 0.05,   # 5 cents
        "pennies": 0.01    # 1 cent
    }

    # OOP Lesson: __init__ is the CONSTRUCTOR.
    # It runs when we create a new MoneyMachine object.
    def __init__(self):

        # OOP Lesson: ATTRIBUTES are variables that belong to the object
        self.profit = 0          # total money earned
        self.money_received = 0  # money user inserted

    # OOP Lesson: METHODS are actions the object can do
    def report(self):
        """Shows how much money the machine has made"""

        # The machine tells us its profit
        print(f"Money: {self.CURRENCY}{self.profit}")

    # This method asks the user to insert coins
    def process_coins(self):
        """Calculates total money inserted"""

        print("Please insert coins.")

        # Look at each coin type and count the money
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]

        # Return the total money the user inserted
        return self.money_received

    # This method checks if the user paid enough
    def make_payment(self, cost):
        """Returns True if payment works, False if not"""

        # Ask for coins first
        self.process_coins()

        # If the user gave enough money
        if self.money_received >= cost:

            # Calculate change
            change = round(self.money_received - cost, 2)

            # Give change back
            print(f"Here is {self.CURRENCY}{change} in change.")

            # Add money to the machine's profit
            self.profit += cost

            # Reset money for next customer
            self.money_received = 0

            return True

        else:
            # Not enough money → refund
            print("Sorry that's not enough money. Money refunded.")

            # Reset inserted money
            self.money_received = 0

            return False