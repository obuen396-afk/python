print("Creator Kitz: version 0.0.6")
Videogames = True
print("I made videogames here: ", Videogames)

if Videogames == True :
    VideoNumbers = 1
    print("Videogames made: ", VideoNumbers)
    print("Next sub!")
else :
    print("Nevermind.") 

print("\nDeveloped by Oliver at EVIT, 2026/2027")
months = ["July", "August", "September", "October", "November", "December", "January", "Febuary", "March", "April", "May"]
for x in months :
    if x == "July" :
        print(x + ": Creator Kitz")
    elif x == "August" :
        print(x + ": Encounter with Monsters")
    elif x == "September" :
        print(x + ": Gravity Spheres")
    elif x == "October" :
        print(x + ": October Special Spooks")
    elif x == "November" :
        print(x + ": November Turkey Attack!")
    elif x == "December" :
        print(x + ": December Frozen Special")
    elif x == "January" :
        print(x + ": Gregory1")
    elif x == "Febuary" :
        print(x + ": Febuary love ladden")
    elif x == "March" :
        print(x + ": march trap maze")
    elif x == "April" :
        print(x + ": hothothot1")
    elif x == "May" :
        print(x + ": Gregory1Full")
    else :
        print(x)

print("\nHow do variables add/subtract?")
print("Say the first number is 55.")
Y_change_test = 55
number_change = 3
while Y_change_test > -1 :
    print(Y_change_test)
    Y_change_test = Y_change_test + number_change
    if number_change > -11 :
        number_change = number_change - 1
    else :
            number_change = -10
print("0\nWell...")

print("\nLets try \"Encounter with Monsters\"")
running = True
while running == True :
    you_health = 100
    enemy_health = 100
    you_do = ""
    enemy_do = ""
    you_heal = 3
    enemy_heal = 3
    while you_health > 0 and enemy_health > 0 :
        print("your health: " + str(you_health))
        print("your enemy's health: " + str(enemy_health))
        if not you_do == "SAX" :
            you_do = input("What do you do? A for Attack, SA for Strong Attack (stronger than two normal attacks, but makes you weak for a turn), or D for Defend?")
            if you_do == "A" :
                enemy_health = enemy_health - 10
                print("You attacked! Enemy lost 10 health!")
            elif you_do == "SA" :
                enemy_health = enemy_health - 25
                print("You did a strong attack! Enemy lost 25 health!")
            elif you_do == "D" :
                print("You defended, half damage deflected.")
            elif you_do == "H" and you_heal > 0:
                you_health = you_health + 10
                print("You used a potion to heal yourself!")
                you_heal = you_heal - 1
                print("Potions: " + str(you_heal))
            elif you_do == "K" :
                enemy_health = 0
            elif you_do == "PK" :
                you_health = 0
            else :
                print("Great! You gave your enemy a free attack!")
        else:
            print("You're on cooldown! You must wait for the enemy's turn, again!")
        if you_health > 100 :
            you_health = 100
        if not enemy_do == "SAX" :
            if you_do == "SA" and enemy_health < 50 :
                enemy_do = "H"
            elif you_do == "SA" and enemy_health > 50 :
                enemy_do = "SA"
            elif you_do == "SAX":
                enemy_do = "SA"
            elif you_do == "D" :
                enemy_do = "D"
            elif you_do == "A" :
                enemy_do = "A"
            else:
                enemy_do = "A"

            if enemy_health < 0 :
                enemy_health = 0

            if enemy_do == "A" :
                you_health = you_health - 10
                print("enemy attacked! You lost 10 health!")
            elif enemy_do == "SA" :
                you_health = you_health - 25
                print("enemy did a strong attack! You lost 25 health!")
            elif enemy_do == "D" :
                print("enemy defended, half damage deflected.")
            elif enemy_do == "H" and enemy_heal > 0 :
                enemy_health = enemy_health + 10
                print("enemy used a potion to heal itself!")
                enemy_heal = enemy_heal - 1
                print("Enemy's Potions: " + str(enemy_heal))
            else :
                print("Great! Your enemy gave you a free attack!")
        else:
            print("Your enemy's on cooldown! Your enemy must wait for your turn, again!")
        if enemy_health > 100 :
            enemy_health = 100

        
        if you_do == "SAX":
            you_do = ""
        elif you_do == "SA" :
            you_do = "SAX"

        if enemy_do == "SAX":
            enemy_do = ""
        elif enemy_do == "SA" :
            enemy_do = "SAX"

    if you_health <= 0 :
        print("Oh no! You lost!")
    elif enemy_health <= 0 :
        print("Horray! You defeated your opponent!")
    running = input("Do you want to retry? Y or N. ") == "Y"
print("The end!")
