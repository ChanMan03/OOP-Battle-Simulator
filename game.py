from goblin import Goblin
from hero import Hero

ARENA_NAME = "ASCTE"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Scribble")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    goblinTwo = Goblin("Gribble")

    print(f"{goblinTwo.name} enters the arena with {goblin.health} health.")

    print("But no hero has answered the call... yet.")

    hero = Hero("Sentinal", 125, 17.5)

    print(f"{hero.name} enters the arena with {hero.health} health.")

    heroAttack = hero.attack()
    goblin.take_damage(heroAttack)





if __name__ == "__main__":
    main()
