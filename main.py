# Roguelike game

# Importing other files
#import cards
#import apply

print("Hi and welcome to this simple Python roguelike game!")

# Classes
class Classe:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
        
    # Printing nicer output
    def __str__(self):
        return f"{self.name} -> " + " ".join(f"{k}: {v}" for k, v in self.stats.items())

warrior = Classe("Warrior",{"HP": 25, "ATK": 15, "DEF": 15})
wizard = Classe("Wizard",{"HP": 15, "ATK": 25, "DEF": 5})
oplita = Classe("Oplita",{"HP": 20, "ATK": 10, "DEF": 20})


print("Please, select your Classe:")
selectedClasse = None
# Needed to store the resutl outside the loop once it ends
while selectedClasse == None:
    selection = input(f"1. {warrior}\n2. {wizard}\n3. {oplita}\n")
    match selection:
        case "1":
            answer = input(f"You selected {warrior}.\nAre you okay with this(y/n)? ")
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
            answer = input(f"You selected {wizard}.\nAre you okay with this(y/n)? ")
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
           answer = input(f"You selected {oplita}.\nAre you okay with this(y/n)? ")
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
print(f"{cards.fireball}")

#print(f"Your {selectedClasse.name}'s hp are {selectedClasse.stats["hp"]}")
# How to change a stat
#selectedClasse.stats["hp"] -= 5
#print(f"Now your {selectedClasse.name}'s hp are {selectedClasse.stats["hp"]}")
# Game is starting now
#gameOver = False
#while gameOver == False:
    
