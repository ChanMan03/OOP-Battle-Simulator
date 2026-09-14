import random

class Hero:
    """The hero blueprint will be implemented later in the project."""
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        return (random.randint(1, self.attack_power))

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
    
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    pass
