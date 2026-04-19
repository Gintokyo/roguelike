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
        if effect == 'attack':
            enemy.stats['HP'] -= self.power
            print(f"{self.name} does {self.power} damage to {enemy.name}'s HP")
            if enemy.stats['HP'] < 0:
                print(f"{enemy.name}'s HP: {max(0, enemy.stats['HP'])}")
            else:
                print(f"{enemy.name}'s HP: {enemy.stats['HP']}/{enemy.stats['MAX_HP']}")
        elif effect == 'heal':
            player.stats['HP'] += self.power
            # Make the HP actually change up to the MAX hp of the character
            if player.stats['HP'] > player.stats['MAX_HP']:
                player.stats['HP'] = player.stats['MAX_HP']
                print(f"{player.name}'s HP are aready maxed out: {player.stats['MAX_HP']}/{player.stats['MAX_HP']}")
            else:
                print(f"{self.name} heals {self.power} HPs to {player.name}")
                print(f"{player.name}'s HP: {player.stats['HP']}/{player.stats['MAX_HP']}")
       
	    # Buffs & debuffs
        elif effect.startswith('buff') or effect.startswith('debuff'):
            # Splits the words "buff ATK" -> ["buff", "ATK"]
            parts = effect.split()
            if len(parts) == 2:
                # 'parts' will be composed of 'action' and 'stat'
                action, stat = parts
                stat = stat.upper()
                if action == 'buff':
                    player.stats[stat] += self.power
                    print(f"{self.name} boosts {player.name}'s {stat} by {self.power}")
                    print(f"{player.name}'s {stat}: {player.stats[stat]}")
                elif action == 'debuff':
                    enemy.stats[stat] -= self.power
                    print(f"{self.name} lowers {enemy.name}'s {stat} by {self.power}")
                    if enemy.stats[stat] < 0:
                        print(f"{enemy.name}'s {stat}: 0")
                    else:
                        print(f"{enemy.name}'s {stat}: {enemy.stats[stat]}")
                else:
                    print(f"{stat} not found!")

       # Status effects
       # Poison
        elif effect.startswith('poison'):
            parts = effect.split()
            if len(parts) == 2:
                _, duration = parts
                duration = int(duration)
                # This will allow to check poison regardless of other status_effect are already active
                # if enemy.status_effect == 'poison' only checks if the values equal to 'poison'
                if 'poison' in enemy.status_effect:
                    print(f"{enemy.name} is already poisoned!")
                else:
                    enemy.status_effect['poison'] = duration
                    print(f"{enemy.name} has been poisoned for {duration} turns!")

# Card database

# Damage cards
fireball = Card('Fireball', 'attack', 5)
dmg_deck = [
    fireball
]

# Healing cards
heal = Card('Heal', 'heal', 5)
heal_deck = [
    heal
]

# Status cards
poison = Card('Poison', 'poison 3', 3)
status_deck =[
    poison
]

# Buff/Debuff cards
atkp = Card('Strength', 'buff ATK', 1)
defm = Card('Soft', 'debuff DEF', 1)
uff_deck = [
    atkp,
    defm
]

# Player's deck
player_deck = [
    fireball,
    heal,
    atkp,
    poison
    ]

# Enemy's deck
enemy_deck = [
    fireball,
    heal,
    atkp,
    poison
    ]