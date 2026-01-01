# Classes
class Classe:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
        
    # Printing nicer output
    def __str__(self):
        return f"{self.name} -> " + " ".join(f"{k}: {v}" for k, v in self.stats.items())
    
# Classes
warrior = Classe("Warrior",{"HP": 25, "ATK": 15, "DEF": 15})
wizard = Classe("Wizard",{"HP": 15, "ATK": 25, "DEF": 5})
oplita = Classe("Oplita",{"HP": 20, "ATK": 10, "DEF": 20})
# TODO Need to optimize the code with a similar function to the enemy_list
classe_list = [
    warrior,
    wizard,
    oplita
]

# Enemies
bandit = Classe("Bandit",{"HP": 10, "ATK": 5, "DEF": 2})
warlock = Classe("Warlock",{"HP": 8, "ATK": 7, "DEF": 2})

enemy_list = [
    bandit,
    warlock
]