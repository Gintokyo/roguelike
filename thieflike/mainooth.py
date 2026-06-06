# Roguelike game

from classes import *
from functions import *
from cards import *


print("Hi and welcome to this Thieflike, a... Roguelike game!\n")
pause(1)
print ("Please, select your class:")
pause()
selectedClasse = None
while selectedClasse == None:
    selection = input(
        f"1. {warrior}\n"
        f"2. {wizard}\n"
        f"3. {oplita}\n"
    )
    match selection:
        case "1":
            print(f"You selected {warrior}.")
            pause()
            answer = input("Are you okay with this? (y/n) ")
            if answer.lower() == "n":
                pause()
                print("What Classe would you choose?")
                continue
            elif answer.lower() =="y":
                selectedClasse = warrior
                # break must be after the re-assignment of the variable
                break
            else:
                pause()
                print("Select your Classe, ¡por favor!")
                pause()
                continue
        case "2":
            print(f"You selected {wizard}.")
            pause()
            answer = input("Are you okay with this? (y/n) ")
            if answer.lower() == "n":
                print("What Classe would you choose?")
                continue
            elif answer.lower() =="y":
                selectedClasse = wizard
                break
            else:
                pause()
                print("Select your Classe, ¡por favor!")
                pause()
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
                pause()
                print("Select your Classe, ¡por favor!")
                pause()
                continue
        case _:
            print(f"Select a Classe before starting!")
            pause()

gameOver = False
# turn should be here, outside the loop, in order to be updated
turn = 0
pause()
while gameOver == False:
    current_enemy = enemy_select()
    print(f"Are you ready to start, {selectedClasse}?")
    pause(.5)
    print(f"Your first enemy is {current_enemy}")
    pause(.5)

    while selectedClasse.stats['HP'] > 0 and current_enemy.stats['HP'] > 0:
        selectedClasse.process_status_effects()
        current_enemy.process_status_effects()
        print(f"What card would you like to use?\n")
        my_deck()
        # current_enemy.name returns an error because it tries to print a string while the function is returning an object
        selected_card = choose_card()
        print(f"You played: {selected_card.name}!\n")
        selected_card.applyEffect(selectedClasse, current_enemy)
        
        # Prevents dead enemies acting
        if current_enemy.stats['HP'] <= 0:
            break

        opponent_choice = opponent_card()
        print(f"{current_enemy.name} played: {opponent_choice.name}!\n")
        opponent_choice.applyEffect(current_enemy, selectedClasse)
        #battle_turns(turn, selectedClasse, current_enemy)
        turn += 1
        print(f"Turns elapsed: {turn}")
        # Just to check the status effect for debugging purposes
        #print(f"Status effect {current_enemy.status_effects}")
    else:
        # With gameOver = True right here, it seems to stop but it will begin anew after the enemy or the player reach 0 HP (which could be a good thing)
        break
    gameOver = True
print("GG WP!")