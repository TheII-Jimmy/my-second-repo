from character import Character

def main():
    hero = Character("Knight", 30, 5)
    enemy1 = Character("Goblin", 20, 3)
    ememy2 = Character("King Slime", 50, 2)
    ememies = [enemy1, ememy2]

    print(hero)
    print(enemy1)
    print(ememy2)
    print()

    for enemy in ememies:
        while hero.is_alive() and enemy.is_alive():
            hero.attack(enemy)
            if enemy.is_alive():
                enemy.attack(hero)
            print(hero)
            print(enemy)
            print()

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")

if __name__ == "__main__":
    main()
