# Cards
class Card:
    def __init__(self, name, effect, power):
        self.name = name
        self.effect = effect
        self.power = power
        
    # Printing card
    def __str__(self):
        return f"{self.name} {self.effect} {self.power}"
    
    # self == card, player == who plays the card, enemy == receiver
    def applyEffect (self, player, enemy):
        effect = self.effect.lower()
        if effect == "attack":
            enemy.stats["HP"] -= self.power
            print(f"{self.name} does {self.power} damage to {enemy.name}'s HP")
            print(f"{enemy.name}'s HP: {enemy.stats["HP"]}")
        elif effect == "heal":
            print(f"{player.name}'s HP: {player.stats["HP"]}")
            player.stats["HP"] += self.power
            print(f"{self.name} heals {self.power} HPs to {player.name}")
            print(f"{player.name}'s HP: {player.stats["HP"]}")

	    # Buffs & debuffs
        elif effect.startswith("buff") or effect.startswith("debuff"):
            # Splits the words "buff ATK" -> ["buff", "ATK"]
            parts = effect.split()
            if len(parts) == 2:
                # 'parts' will be composed of 'action' and 'stat'
                action, stat = parts
                stat = stat.upper()
                if action == "buff":
                    player.stats[stat] += self.power
                    print(f"{self.name} boosts {player.name}'s {stat} by {self.power}")
                    print(f"{player.name}'s {stat}: {player.stats[stat]}")
                elif action == "debuff":
                    enemy.stats[stat] -= self.power
                    print(f"{self.name} lowers {enemy.name}'s {stat} by {self.power}")
                    print(f"{enemy.name}'s {stat}: {enemy.stats[stat]}")
                else:
                    print(f"{stat} not found!")

# Card database

# Damage cards
fireball = Card("Fireball", "attack", 5)
dmg_deck = [
    fireball
]

# Healing cards
heal = Card("Heal", "heal", 5)
heal_deck = [
    heal
]

# Status cards
poison = Card("Poison", "poison 3", 1)
atkp = Card("Strength", "buff ATK", 1)
defm = Card("Soft", "debuff DEF", 1)
status_deck = [
    poison,
    atkp,
    defm
]

# Player's deck
player_deck = [
    fireball,
    heal,
    atkp
    ]