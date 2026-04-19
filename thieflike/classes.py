# Classes
class Classe:
    def __init__(self, name, stats, status_effect):
        self.name = name
        self.stats = stats
        # This will allow me to store more status effects at once
        self.status_effect = {}
        
    # Printing nicer output
    def __str__(self):
        # I don't need to not to return status_effect because it's not in .stats, of course (not so obvious the 1st time for me)
        return f"{self.name} -> " + " ".join(f"{k}: {v}" for k, v in self.stats.items() if k != 'MAX_HP')

# Insert a visualizazion for MAX_HP/HP here
# Classes
warrior = Classe('Warrior',{'MAX_HP': 25, 'HP': 25, 'ATK': 15, 'DEF': 15}, None)
wizard = Classe('Wizard',{'MAX_HP': 15, 'HP': 15, 'ATK': 25, 'DEF': 5}, None)
oplita = Classe('Oplita',{'MAX_HP': 20, 'HP': 20, 'ATK': 10, 'DEF': 20}, None)

classe_list = [
    warrior,
    wizard,
    oplita
]

# Enemies
bandit = Classe('Bandit',{'MAX_HP': 10, 'HP': 10, 'ATK': 5, 'DEF': 2}, None)
warlock = Classe('Warlock',{'MAX_HP': 8, 'HP': 8, 'ATK': 7, 'DEF': 2}, None)

enemy_list = [
    bandit,
    warlock
]

# Status

poison = 'poison'

status_list = [
    poison
]