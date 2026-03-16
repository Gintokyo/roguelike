# Classes
class Classe:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
        
    # Printing nicer output
    def __str__(self):
        return f"{self.name} -> " + " ".join(f"{k}: {v}" for k, v in self.stats.items() if k != "MAX_HP")
    
# Classes
warrior = Classe("Warrior",{"MAX_HP": 25, "HP": 25, "ATK": 15, "DEF": 15})
wizard = Classe("Wizard",{"MAX_HP": 15, "HP": 15, "ATK": 25, "DEF": 5})
oplita = Classe("Oplita",{"MAX_HP": 20, "HP": 20, "ATK": 10, "DEF": 20})

classe_list = [
    warrior,
    wizard,
    oplita
]

# Enemies
bandit = Classe("Bandit",{"MAX_HP": 10, "HP": 10, "ATK": 5, "DEF": 2})
warlock = Classe("Warlock",{"MAX_HP": 8, "HP": 8, "ATK": 7, "DEF": 2})

enemy_list = [
    bandit,
    warlock
]