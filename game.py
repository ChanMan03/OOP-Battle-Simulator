from goblin import Goblin
from hero import Hero

ARENA_NAME = "ASCTE"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
          hero_damage = hero.attack()
          enemy.take_damage(hero_damage, hero)

          if hero.crit_hit:
               print("Critical Hit!")
        
          if enemy.is_alive():
               enemy_damage = enemy.attack()
               hero.take_damage(enemy_damage, enemy)
            
          if enemy.crit_hit:
               print("Critical Hit!")  

    if hero.is_alive():
        print(f"{hero.name} the {hero.hero_class} wins!")
    else:
         print(f"{enemy.name} wins!")

     

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

    hero = Hero("Sentinal", 135, 20, "Knight", True)

    print(f"{hero.name} the {hero.hero_class} enters the arena with {hero.health} health.")

    print("The battle begins...")

    battle(hero, goblin)





if __name__ == "__main__":
    main()
