# Contains most of the functions

# Importing the player_deck
from cards import player_deck, enemy_deck
from classes import enemy_list
# This is needed to randomly select what enemy the player's gonna face at a time
import random

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
    currentEnemy = random.choice(enemy_list)
    return currentEnemy

# Function to print cards in enemy's deck (will become Cards in Hand)
def opponent_deck():
    n = 1
    for card in enemy_deck:
        print(f"{n}. {card}")
        n += 1

# The enemy selects a card
def opponent_card():
    enemy_card = random.choice(enemy_deck)
    print(enemy_card)

# Function to keep track of turns NOT READY YET
#def battle_turns(x, player, enemy):
#   turno = x
#   while player.stats["HP"] >0 and enemy.stats["HP"] > 0:
#       current_turn = turno
#       current_turn += 1
#       print(current_turn)
#   else:
#       gameOver = True