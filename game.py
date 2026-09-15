from goblin import Goblin
from hero import Hero

ARENA_NAME = "ASCTE"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Scribble", False)

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    goblinTwo = Goblin("Gribble", True)

    print(f"{goblinTwo.name} enters the arena with {goblin.health} health.")

    print("A hero has answered the call!")

    hero = Hero("Sentinal", 135, 20, "Knight")

    print(f"{hero.name} the {hero.hero_class} enters the arena with {hero.health} health.")

    print("The battle begins...")

    heroAttack = hero.attack()
    goblin.take_damage(heroAttack, hero)

    if hero.crit_hit:
            print("Critical Hit!")





if __name__ == "__main__":
    main()
