# Contains most of the functions

# Importing the player_deck
from cards import player_deck

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

# Function to keep track of turns
#def battle_turns():
#    turn = 1
#    if bandit["HP"] <= 0:
#        
#    else:
#        endBattle = True
#    print(turn)