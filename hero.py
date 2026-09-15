import random

class Hero:
    """The hero blueprint will be implemented later in the project."""
    def __init__(self, name, health, attack_power, hero_class):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.hero_class = hero_class

    def attack(self):
        crit_percent =  random.randint(1, 100)
        if crit_percent <= 5:
            self.crit_hit = True
            return (random.randint(1, self.attack_power) + random.randint(1, 100))
        else:
            self.crit_hit = False
            return (random.randint(1, self.attack_power))

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
    
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    pass
