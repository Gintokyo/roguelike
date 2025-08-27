# Cards
# Damage cards
class Card:
    def __init__(self, name, effect, power):
        self.name = name
        self.effect = effect
        self.power = power
        
    # Printing card
    def __str__(self):
        return f"{self.name} {self.effect} {self.power}"

fireball = Card("Fireball", "attack", 5)
dmg_deck = [
    fireball
]

print(f"{fireball}")

# Healing cards
heal = Card("Heal", "Heal", 5)
heal_deck = [
    heal
]

print(f"{heal}")

# Status cards
poison = Card("Poison", "Poison damage", 1)
atkp = Card("Strength", "Buff ATK", 1)
status_deck = [
    poison
    atkp
]

print(f"{poison}")
