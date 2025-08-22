# Roguelike game

import json
print("Hi and welcome to this simple Python roguelike game!")

# Classes
class Classe:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
        
    # Printing nicer output
    def __str__(self):
        return f"{self.name} -> " + " ".join(f"{k}: {v}" for k, v in self.stats.items())

warrior = Classe("Warrior",{"hp": 25, "atk": 15, "def": 15})
wizard = Classe("Wizard",{"hp": 15, "atk": 25, "def": 5})
oplita = Classe("Oplita",{"hp": 20, "atk": 10, "def": 20})


print("Please, select your Classe:")
selected_Classe = None
while selected_Classe == None:
    selection = input(f"1. {warrior}\n2. {wizard}\n3. {oplita}\n")
    match selection:
        case "1":
            answer = input(f"You selected {warrior}.\nAre you okay with this(y/n)?")
            if answer.lower() == "n":
                print("What Classe would you choose?")
                continue
            elif answer.lower() =="y":
                selected_Classe = warrior
                # break must be after the re-assignment of the variable
                break
            else:
                print("Select your Classe, ¡por favor!")
                continue
        case "2":
            answer = input(f"You selected {wizard}.\nAre you okay with this(y/n)?")
            if answer.lower() == "n":
                print("What Classe would you choose?")
                continue
            elif answer.lower() =="y":
                selected_Classe = wizard
                break
            else:
                print("Select your Classe, ¡por favor!")
                continue
        case "3":
           answer = input(f"You selected {oplita}.\nAre you okay with this(y/n)?")
           if answer.lower() == "n":
                print("What Classe would you choose?")
                continue
           elif answer.lower() =="y":
                selected_Classe = oplita
                break
           else:
                print("Select your Classe, ¡por favor!")
                continue
        case _:
            print(f"Select a Classe before starting!")

print(f"Are you ready to start, {selected_Classe.name}?")
# Game is starting now
#gameOn = True
#while gameOn == True:
