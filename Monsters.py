print("Encounters With Monsters: version 1.0.0")
running = True
while running == True :
    mode = input("1 for 1-Player or 2 for 2-Player?")
    if mode == "2" :
        mode = 2
    elif mode == "1" :
        mode = 1
    else :
        print("Okay. 1-player then...")
    You = input("Enter a name for P.1.")
    if mode == 2 :
        Enemy = input("Enter a name for P.2.")
    else :
        Enemy = "Goblin"
    you_health = 100
    enemy_health = 100
    you_do = ""
    enemy_do = ""
    you_heal = 3
    enemy_heal = 3
    you_cooldown = 0
    enemy_cooldown = 1
    while you_health > 0 and enemy_health > 0 :

        print(You + "'s health: " + str(you_health) + "%")
        print(Enemy + "'s health: " + str(enemy_health) + "%")
        print(You + "'s potions: " + str(you_heal))
        print(Enemy + "'s potions: " + str(enemy_heal))
        if you_cooldown == 1 :
            print(You + "'s cooldown time: 1 turn")
        else :
            print(You + "'s cooldown time: " + str(you_cooldown) + " turns")
        if enemy_cooldown == 1 :
            print(Enemy + "'s cooldown time: 1 turn")
        else :
            print(Enemy + "'s cooldown time: " + str(enemy_cooldown) + " turns")
        if you_do == "D" and you_cooldown > 0 :
            print(You + " is on the defense!")
        if enemy_do == "D" and enemy_cooldown > 0 :
            print(Enemy + " is on the defense!")

        if you_health > 0 and you_cooldown <= 0 and enemy_health > 0 :
            you_do = input("What do you do? A for Attack, SA for Strong Attack (stronger than two normal attacks, but makes you weak for a turn), D for Defend, or H for Heal?")
            if you_do == "A" :
                if enemy_do == "D" :
                    enemy_health = enemy_health - 10 // 2
                    print(You + " attacked! " + Enemy + " lost 5 health!")
                else :
                    enemy_health = enemy_health - 10
                    print(You + " attacked! " + Enemy + " lost 10 health!")

            elif you_do == "SA" :
                if enemy_do == "D" :
                    enemy_health = enemy_health - 25 // 2
                    print(You + " did a strong attack! " + Enemy + " lost 12 health!")
                else :
                    enemy_health = enemy_health - 25
                    print(You + " did a strong attack! " + Enemy + " lost 25 health!")
                you_cooldown += 1                    
            
            elif you_do == "D" :
                print(You + " defended, half damage deflected.")
            elif you_do == "H" and you_heal > 0:
                you_health = you_health + 10
                print(You + " used a potion to heal!")
                you_heal = you_heal - 1
            elif you_do == "H" and you_heal == 0:
                print(You + " does not have any potions!")
            else :
                print("Great! " + You + " gave " + Enemy + " a free attack!")
            you_cooldown += 1
        elif enemy_health > 0 and you_health > 0 :
            print(You + "'s on cooldown! " + You + " must wait for " + Enemy + "'s turn!")
            you_do = "B"

        if enemy_health > 100 :
            enemy_health = 100
        if you_health < 0 :
                you_health = 0
        if you_health > 100 :
            you_health = 100
        if enemy_health < 0 :
            enemy_health = 0
        enemy_cooldown -= 1
        if you_cooldown < 0 :
            you_cooldown = 0
        if enemy_cooldown < 0 :
            enemy_cooldown = 0

        print(You + "'s health: " + str(you_health) + "%")
        print(Enemy + "'s health: " + str(enemy_health) + "%")
        print(You + "'s potions: " + str(you_heal))
        print(Enemy + "'s potions: " + str(enemy_heal))
        if you_cooldown == 1 :
            print(You + "'s cooldown time: 1 turn")
        else :
            print(You + "'s cooldown time: " + str(you_cooldown) + " turns")
        if enemy_cooldown == 1 :
            print(Enemy + "'s cooldown time: 1 turn")
        else :
            print(Enemy + "'s cooldown time: " + str(enemy_cooldown) + " turns")
        if you_do == "D" and you_cooldown > 0:
            print(You + " is on the defense!")
        if enemy_do == "D"  and enemy_cooldown > 0:
            print(Enemy + " is on the defense!")
        
        if enemy_cooldown <= 0 and enemy_health > 0 and you_health > 0:
            if mode == 2 :
                enemy_do = input("Player 2: What do you do? A for Attack, SA for Strong Attack (stronger than two normal attacks, but makes you weak for a turn), D for Defend, or H for Heal?")
            else :
                if you_do == "SA" and enemy_health < 50 :
                    enemy_do = "H"
                elif you_do == "SA" and enemy_health >= 50 :
                    enemy_do = "SA"
                elif you_do == "B":
                    enemy_do = "SA"
                elif you_do == "D" :
                    enemy_do = "D"
                else:
                    enemy_do = "A"

            if enemy_do == "A" :
                if you_do == "D" :
                    you_health = you_health - 10 // 2
                    print(Enemy + " attacked! " + You + " lost 5 health!")
                else :
                    you_health = you_health - 10
                    print(Enemy + " attacked! " + You + " lost 10 health!")
            elif enemy_do == "SA" :
                if you_do == "D" :
                    you_health = you_health - 25 // 2
                    print(Enemy + " did a strong attack! " + You + " lost 12 health!")
                else :
                    you_health = you_health - 25
                    print(Enemy + " did a strong attack! " + You + " lost 25 health!")
                enemy_cooldown += 1
            elif enemy_do == "D" :
                print(Enemy + " defended, half damage deflected.")
            elif enemy_do == "H" and enemy_heal > 0 :
                enemy_health = enemy_health + 10
                print(Enemy + " used a potion to heal!")
                enemy_heal = enemy_heal - 1
            elif enemy_do == "H" and enemy_heal <= 0:
                print(Enemy + " does not have any potions!")
            else :
                print("Great! " + Enemy + " gave " + You + " a free attack!")
            enemy_cooldown += 1
        elif enemy_health > 0 and you_health > 0:
            print(Enemy + "'s on cooldown! " + Enemy + " must wait for " + You + "'s turn!")
            enemy_do = "B"

        if you_health < 0 :
                you_health = 0
        if you_health > 100 :
            you_health = 100
        if enemy_health > 100 :
            enemy_health = 100
        if enemy_health < 0 :
            enemy_health = 0
        you_cooldown -= 1
        if you_cooldown < 0 :
            you_cooldown = 0
        if enemy_cooldown < 0 :
            enemy_cooldown = 0


    if you_health <= 0 :
        print(Enemy + " defeated " + You + "!")
    elif enemy_health <= 0 :
        print(You + " defeated " + Enemy + "!")
    running = input("Do you want to retry? Y or N. ") == "Y"
