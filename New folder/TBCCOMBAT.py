import TBC

def main():
    hero = TBC.Character()
    hero.name = "Hero"
    hero.hitPoints = 10
    hero.armor = 2
    hero.hitChance = 50
    hero.maxDamage = 5

    monster = TBC.Character("Monster", 20, 1, 30, 5)

    hero.printStats()
    monster.printStats()

    TBC.fight(hero, monster)

if __name__ == "__main__":
    main()