# Get the logo from art.py
from art import logo

# Show the logo when the program starts
print(logo)


# Function to find who bid the most money
def find_highest_bidder(bidding_record):
    highest_bid = 0      # Start with no money
    winner = ""          # No winner yet

    # Look at each person in the dictionary
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]  # Get their bid

        # If this bid is bigger, update winner
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    # Show who won the auction
    print(f"The winner is {winner} with a bid of ${highest_bid}")


# Dictionary to store names and bids
bids = {}

# This keeps the program running
continue_bidding = True

# Loop until no more bidders
while continue_bidding:

    # Ask the person's name
    name = input("What is your name?: ")

    # Ask how much they want to bid
    price = int(input("What is your bid?: $"))

    # Save the bid in the dictionary
    bids[name] = price

    # Ask if another person wants to bid
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")

    # If no more bidders, stop and find winner
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)

    # If more bidders, clear the screen
    elif should_continue == "yes":
        print("\n" * 20)  # Push old text up so next person can't see bids