# Roguelike game

from classes import *
from functions import my_deck, choose_card


print("Hi and welcome to this simple Python roguelike game!\n")

print("Please, select your Classe:")
selectedClasse = None
# Needed to store the result outside the loop once it ends
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


print(f"Are you ready to start, {selectedClasse.name}?")
print(f"Your first enemy is {bandit}")
gameOver = False

while gameOver == False:
    #action = input(f"What card would you like to use?\n{fireball.name}, {heal.name}, {atkp.name}")
    print(f"What card would you like to use?\n")
    my_deck()

    selected_card = choose_card()
    print(f"You played: {selected_card.name}!\n")
    selected_card.applyEffect(selectedClasse, bandit)
    gameOver = True