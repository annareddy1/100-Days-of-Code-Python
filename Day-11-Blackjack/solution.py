import random
from art import logo


def deal_card():
    """Gives you 1 random card (deck never runs out)"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # 11 = Ace, 10s = J/Q/K
    return random.choice(cards)  # pick 1 random card


def calculate_score(cards):
    """Turns a hand of cards into a score"""

    # If you have 2 cards that make 21, that's Blackjack
    # We return 0 to mean "Blackjack" (special score)
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # If we have an Ace (11) and we are too high, turn Ace into 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)  # remove one Ace that is 11
        cards.append(1)   # add Ace back as 1

    # Normal score is just the sum
    return sum(cards)


def compare(u_score, c_score):
    """Decides who wins using the scores"""

    # Same score = tie
    if u_score == c_score:
        return "Draw 🙃"

    # If computer has Blackjack
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"

    # If user has Blackjack
    elif u_score == 0:
        return "Win with a Blackjack 😎"

    # If user went above 21
    elif u_score > 21:
        return "You went over. You lose 😭"

    # If computer went above 21
    elif c_score > 21:
        return "Opponent went over. You win 😁"

    # Higher score wins
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    # Show the logo when the game starts
    print(logo)

    # These lists hold each player's cards
    user_cards = []
    computer_cards = []

    # Start scores (we will calculate soon)
    computer_score = -1
    user_score = -1

    # This tells us when to stop the game
    is_game_over = False

    # Give 2 cards to user and 2 cards to computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # User's turn (and early stop checks)
    while not is_game_over:
        # Update scores each loop
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Show user their cards and score
        print(f"Your cards: {user_cards}, current score: {user_score}")

        # Show only computer's first card (dealer hides the rest)
        print(f"Computer's first card: {computer_cards[0]}")

        # Stop if someone has Blackjack or user busts
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask user if they want another card
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())  # give user a new card
            else:
                is_game_over = True  # user is done

    # Computer's turn: keep drawing until 17 or more (dealer rule)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())              # give computer a new card
        computer_score = calculate_score(computer_cards)  # update computer score

    # Show final hands and final scores
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    # Print who won
    print(compare(user_score, computer_score))


# Keep asking to play again
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)  # clear screen by pushing old text away
    play_game()