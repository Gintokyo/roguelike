# Contains most of the functions

# Importing the player_deck
from cards import player_deck, enemy_deck
from classes import enemy_list
# This is needed to randomly select what enemy the player's gonna face at a time
import random
# This allows to copy a class without actually modufying the original
import copy

# Function to print cards in the deck (will become Cards in Hand)
def my_deck():
    n = 1
    for card in player_deck:
        print(f"{n}. {card}")
        n += 1

# Select a card
def choose_card():
    while True:
        try:
            choice = int(input("Select a card to play: "))
            if 1 <= choice <= len(player_deck):
                return player_deck[choice-1]
            else:
                print("Choose a valid card number!")
        except ValueError:
            print("Please, type a card number!")

# Select a random enemy
def enemy_select():
    # deepcopy prevents from keeping old HP/Status
    current_enemy = copy.deepcopy(random.choice(enemy_list))
    return current_enemy

# NOT NEEDED AS THE CARDS IN THE OPPONENTS HAND ARE NOT PRINTED
# Function to print cards in enemy's deck (will become Cards in Hand)
def opponent_deck():
    n = 1
    for card in enemy_deck:
        print(f"{n}. {card}")
        n += 1

# The enemy selects a card
def opponent_card():
    enemy_card = random.choice(enemy_deck)
    # Amended print() with return otherwise, of course, it would not RETURN values, lmaos
    return(enemy_card)