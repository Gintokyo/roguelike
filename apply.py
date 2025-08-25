# self == card, player == card player, enemy == receiver
def applyEffect (self, player, enemy):
    if self.effect == "Attack":
        enemy["HP"] -= self.power
        print(f"{self.name} does {self.power} damage to {enemy.name}'s HP")
    elif self.effect == "Heal":
        enemy["HP"] += self.power
        print(f"{self.name} heals {self.power} HPs to {enemy.name}")
    elif self.effect == "Buff ATK":
        enemy["ATK"] += self.power
        print(f"{self.name} boosts {enemy.name} ATK by self.power ")
