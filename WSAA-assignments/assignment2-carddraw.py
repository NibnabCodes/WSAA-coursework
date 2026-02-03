# Author: Niamh Hogan

# This program carries out the following tasks:
# - Shuffles a deck using the API
# - Gets the deck_id from the shuffle response
# - Draws 5 cards from that deck
# - Prints each card’s value and suit
# = Checks the hand to see if it contains: a pair, triple, straight, or same suit
# = Congratulates the user if any of those happen

# I decided to use functions to organise my program into clear sections, 
# to improve readability and reusability of code.

# import to interact with the API
import requests

# Create function to shuffle new deck and get deck_id
def get_new_deck_id():
    url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    return requests.get(url).json()["deck_id"] # https://www.w3schools.com/PYTHON/ref_requests_get.asp 
# Note: .json() converts the JSON text from the API into a Python dictionary 
# to allow for accessing ot items e.g) ["deck_id"]

# Create function to draw 5 cards from deck using deck_id
def draw_cards(deck_id, count=5):
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={count}"
    return requests.get(url).json()["cards"]

# Create function to print each card's value and suit
def print_cards(cards):
    print("Your cards:")
    for card in cards:
        print(f"{card['value']} of {card['suit']}")
    print()
    
# Count how many times each item appears in a list
def count_items(items):
    counts = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

# Check the hand for a pair, triple, straight, or same suit
def check_hand(cards):
    values = [card["value"] for card in cards]
    suits = [card["suit"] for card in cards]

    value_counts = count_items(values)
    suit_counts = count_items(suits)

    # Pair
    if 2 in value_counts.values():
        print("Congratulations! You have a pair!")

    # Triple
    if 3 in value_counts.values():
        print("Congratulations! You have a triple!")

    # All same suit
    if len(suit_counts) == 1:
        print("Congratulations! All cards are the same suit!")

    # Straight
    # Create dictionary to map card values to numbers 
    # so the program can check for a straight
    order = {
        "ACE": 1, "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "JACK": 11, "QUEEN": 12, "KING": 13
    }

    numbers = [] # Create empty list to store numeric values of the cards
    for value in values:
        numbers.append(order[value]) # Convert card values to numbers

    numbers.sort() # Sort numbers in ascending order

    is_straight = True  # Assume the hand is a straight until proven otherwise
    for i in range(len(numbers) - 1):
        if numbers[i + 1] != numbers[i] + 1: # Check if each number is exactly 1 higher than the previous
            is_straight = False # If not consecutive, it’s not a straight
            break # Stop checking further once a non-consecutive pair is found

    if is_straight:
        print("Congratulations! You have a straight!")

# Control the program flow and runs all main steps
def main():
    deck_id = get_new_deck_id()
    cards = draw_cards(deck_id)
    print_cards(cards)
    check_hand(cards)

# Start program
main()


