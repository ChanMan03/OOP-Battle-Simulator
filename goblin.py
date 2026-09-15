import random
from hero import Hero


class Goblin:
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name, armor):
        self.name = name
        self.health = 100
        self.attack_power = 15
        self.armor = armor

    def attack(self):
        """Return a random amount of damage."""
        crit_percent =  random.randint(1, 100)
        
        if crit_percent <= 5:
            self.crit_hit = True
            return (random.randint(1, self.attack_power) + random.randint(1, 100))
        else:
            self.crit_hit = False

        return random.randint(1, self.attack_power)

    def take_damage(self, damage, hero):
        """Reduce health without allowing it to fall below zero."""
        if self.armor:
            armor_percent = random.randint(1, 90) / 100
            damage = damage * (1 - armor_percent)

        self.health = max(0, self.health - damage)

        print(f"{self.name} takes {damage} damage from {hero.name}. Health: {self.health}")

    def is_alive(self):
        """Return True while the goblin has health remaining."""
        return self.health > 0
