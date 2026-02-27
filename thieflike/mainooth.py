# Roguelike game

from classes import *
from functions import my_deck, choose_card, enemy_select, opponent_card#, battle_turns


print("Hi and welcome to this Thieflike, a... Roguelike game!\n")
print ("Please, select your class:")
selectedClasse = None
while selectedClasse == None:
    selection = input(f"1. {warrior}\n2. {wizard}\n3. {oplita}\n")
    match selection:
        case "1":
            answer = input(f"You selected {warrior}.\nAre you okay with this? (y/n) ")
            if answer.lower() == "n":
                print("What Classe would you choose?")
                continue
            elif answer.lower() =="y":
                selectedClasse = warrior
                # break must be after the re-assignment of the variable
                break
            else:
                print("Select your Classe, ¡por favor!")
                continue
        case "2":
            answer = input(f"You selected {wizard}.\nAre you okay with this? (y/n) ")
            if answer.lower() == "n":
                print("What Classe would you choose?")
                continue
            elif answer.lower() =="y":
                selectedClasse = wizard
                break
            else:
                print("Select your Classe, ¡por favor!")
                continue
        case "3":
           answer = input(f"You selected {oplita}.\nAre you okay with this? (y/n) ")
           if answer.lower() == "n":
                print("What Classe would you choose?")
                continue
           elif answer.lower() =="y":
                selectedClasse = oplita
                break
           else:
                print("Select your Classe, ¡por favor!")
                continue
        case _:
            print(f"Select a Classe before starting!")

gameOver = False
# turn should be here, outside the loop, in order to be updated
turn = 0
while gameOver == False:
    current_enemy = enemy_select()
    print(f"Are you ready to start, {selectedClasse}?")
    print(f"Your first enemy is {current_enemy}")

    while selectedClasse.stats["HP"] > 0 and current_enemy.stats["HP"] > 0:
        print(f"What card would you like to use?\n")
        my_deck()
        # current_enemy.name returns an error because it tries to print a string while the function is returning an object
        selected_card = choose_card()
        print(f"You played: {selected_card.name}!\n")
        selected_card.applyEffect(selectedClasse, current_enemy)
        # TODO: make it apply the effect of the card and only play if the enemy is still alive
        opponent_choice = opponent_card()
        #battle_turns(turn, selectedClasse, current_enemy)
        turn += 1
        print(turn)
    else:
        # With gameOver = True it seems to stop but it will begin anew after the enemy or the player reach 0 HP (which could be a good thing)
        gameOver = True
print("GG WP!")