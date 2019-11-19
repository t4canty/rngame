# import fights.py
# import enemies.py
# import crew.py
import random
from subprocess import call
from time import sleep, time
import sys
import clear
import save, planets
try:
    f = open("SaveGame.txt", "r")
    f1 = f.readlines()
    i = 0
    itemList = []
    if f1[0] != "--end items--\n":
        while f1[i] != "--end items--\n":
            itemList.append(f1[i])
            i += 1
    i += 1
    planetid = int(f1[i].rstrip("\n"))
    i += 1
    name = f1[i].rstrip("\n")
    i += 1
    health = int(f1[i].rstrip("\n"))
    i += 1
    damage = int(f1[i].rstrip("\n"))
    i += 1
    progress = int(f1[i].rstrip("\n"))
    i += 1
    regen = int(f1[i].rstrip("\n"))
    i += 1
    thrust = int(f1[i].rstrip("\n"))
    i += 1
    wepon = int(f1[i].rstrip("\n"))
    i += 1
    credits = int(f1[i].rstrip("\n"))
    f.close()
except FileNotFoundError:
    itemList = []
    planetid = 0
    name = "PlaceHolder Name, Replace with player Input"
    health = 100
    damage = 5
    progress = 0
    hasdock = 1
    regen = 0
    thrust = 0
    wepon = 0
    credits = 100
    planetid = 0





def menu():
    clear.clear()
    view()
    global name
    global planetid
    global hasdock
    print("Welcome to the menu! What would you like to do?")
    print("1) Buy Items Requires dock")
    print("2) view ship")
    print("3) Upgrade Ship")
    print("4) Talk to crew members")
    print("5) Back")
    print("6) Continue")
    print("7) Rename ship")
    print("8) Save game")
    print("9) Exit")
    choice = input("[==>]")
    print("DEBUG:" + choice)
    sleep(0.5)
    if choice == "1":
        if hasdock:
            #call(["clear"])
            clear.clear()
            shop()
        else:
            print("There is no dock!")
    elif choice == "2":
        inventory(9)
    elif choice == "3":
        upgrade()
    elif choice == "4":
        talk()
    elif choice == "5":
        #call(["clear"])
        clear.clear()
        planet(planetid)
        view()
    elif choice == "6":
        travel()
    elif choice == "7":
        name = input("Input new name:")
        name.rstrip("\n")
    elif choice == "8":
        save.save(itemList, planetid, name, health, damage, progress, regen, thrust, wepon, credits)
    elif choice == "9":
        sys.exit()
    else:
        print("Invalid choice")
        sleep(1)


def view():
    global health
    global progress
    global upgrade
    global name
    global damage
    global credits
    print("Ship:" + name)
    print("Health:", health)
    print("Progress:", progress)
    print("You currently do ", damage, " Damage")
    print("You currently have", credits, "credits")
    if upgrade:
        global regen
        global thrust
        global wepon
        if regen and not thrust and not wepon:
            print("You have a regen hull!")
        elif thrust and not regen and not wepon:
            print("You have improved thrusters!")
        elif wepon and not thrust and not regen:
            print("You have heavy weapons!")
        elif wepon and thrust and not regen:
            print("You have heavy weapons and improved thrusters!")
        elif wepon and regen and not thrust:
            print("You have heavy weapons and a regen hull!")
        elif thrust and regen and not wepon:
            print("You have improved engines and a regen hull!")
        elif wepon and thrust and regen:
            print("You have a maxed out ship, what a chad!")


def shop():
    global credits
    num = 0
    print("Welcome to my shop! We have many weapons such as:")
    num1 = random.randint(1, 5)
    while num != num1:
        num2 = random.randint(1, 3)
        item(num2)
        num += 1


def item(a):
    price = 0
    if a == 1:
        a = random.randint(1, 3)
        if a == 1:
            id = 0
            print("Plasma gun: Damage + 5")
            print("Price = 20")
            price = 20
            choice = input("Would you like to buy this? [Y/N]")
            buy(choice, price, id)
        elif a == 2:
            id = 1
            print("Missile launcher: Damage + 2, Shield Peirce")
            print("Price = 30")
            price = 30
            choice = input("Would you like to buy this? [Y/N]")
            buy(choice, price, id)
        elif a == 3:
            id = 2
            print("EMP: Damage +0, disables sheilds for 2 turns")
            print("Price: 15")
            price = 15
            choice = input("Would you like to buy this? [Y/N]")
            buy(choice, price, id)
    elif a == 2:
        a = random.randint(1, 3)
        if a == 1:
            id = 3
            print("Plasma Cannon: Damage + 10")
            price = 30 + random.randint(1, 10)
            print("Price:", price)
            choice = input("Would you like to buy this? [Y/N]")
            buy(choice, price, id)
        elif a == 2:
            id = 4
            print("Gauss Gun: Damage + 10, Sheild peirce +1")
            price = 50 + random.randint(5, 20)
            print("Price:", price)
            choice = input("Would you like to buy this? [Y/N]")
            buy(choice, price, id)
        elif a == 3:
            id = 5
            print("Missle Barrage: Damage + 8, Sheild Peirce")
            price = 40 + random.randint(1, 50)
            print("Price:", price)
            choice = input("Would you like to buy this? [Y/N]")
            buy(choice, price, id)
    elif a == 3:
        a = random.randint(1, 3)
        if a == 1:
            id = 6
            print("Plasma Gatling: Damage + 20")
            price = 70 + random.randint(1, 40)
            print("Price:", price)
            choice = input("Would you like to buy this? [Y/N]")
            buy(choice, price, id)
        elif a == 2:
            id = 7
            print("Artillary System: Damage + 30")
            price = 100 + random.randint(1, 60)
            print("Price:", price)
            choice = input("Would you like to buy this? [Y/N]")
            buy(choice, price, id)
        elif a == 3:
            id = 8
            print("Ion Cannon: Damage + 0, Disable sheilds for 5 turns")
            price = 140 + random.randint(-10, 20)
            print("Price:", price)
            choice = input("Would you like to buy this? [Y/N]")
            buy(choice, price, id)


def buy(choice, price, id):
    global credits
    if choice == "Y" or choice == "y":
        if credits > 0 and price <= credits:
            print("Purchased, thank you!")
            inventory(id)
            # print(id)
            credits -= price
        else:
            print("OI!, You don't have enough money!")
    elif choice == "N" or choice == "n":
        print("Okay")
        pass
    elif credits <= 0:
        print("You do not have enough cash, screw off!")


def inventory(id):
    global itemList
    if id == 0:
        itemList.append("Plasma Gun")
    elif id == 1:
        itemList.append("Missle Launcher")
    elif id == 2:
        itemList.append("EMP")
    elif id == 3:
        itemList.append("Plasma Cannon")
    elif id == 4:
        itemList.append("Guass Gun")
    elif id == 5:
        itemList.append("Missle Launcher")
    elif id == 6:
        itemList.append("Plasma Gatling")
    elif id == 7:
        itemList.append("Artillery")
    elif id == 8:
        itemList.append("Ion Cannon")
    elif id == 9:
        clear.clear()
        #call(["clear"])
        print("You take a look at your ship's contents, and are greeted by:")
        for x in itemList:
            print(x)
        print("Press any key to continue")
        input()
    else:
        print("error in inventory")


def upgrade():
    print("Not implemented yet")


def talk():
    print("Not implemented yet")


def planet(Nplanetid):
    global progress
    global planetid
    planetid = Nplanetid
    if planetid == 0:
        global hasdock
        hasdock = 1
        print("The wonderful world of Starlaxia, the greatest space station ever built.")
        print(
            "You grew up here, and learned to love this place. This place has a special location in your heart, literally.")
        print("You got your first aortal implant here.")
        print("What do you want to do?")
        print("1: Menu")
        print("2: Continue")
        ch = input("[==>]")
        if ch == "1":
            menu()
        else:
            travel()
    elif planetid == 1:
        planets.eldrannon()


def travel():
    global progress
    travelTime = progress + random.randint(10, 30)

    while progress < travelTime:
        clear.clear()
        event()
        progress += 1
    id = random.randint(0, 1)
    #id = 0
    planet(id)
def event():
    global progress
    global health
    num1 = random.randint(0, 100)
    if num1 == 0:
        view()
        bad(1)
        sleep(0.5)

    elif 10 > num1 > 7:  # 2
        view()
        bad(2)
        sleep(0.5)

    elif 20 > num1 > 17:  # 3
        view()
        bad(3)
        sleep(0.5)

    elif 30 > num1 > 27:  # 3
        view()
        bad(4)
        sleep(0.5)

    elif 40 > num1 > 35:  # 5
        view()
        bad(5)
        sleep(0.5)

    elif 50 > num1 > 45:  # 5 total 20
        view()
        bad(6)
        sleep(0.5)

    elif 60 > num1 > 54:  # 6
        view()
        good(1)
        sleep(0.5)

    elif 70 > num1 > 66:  # 4
        view()
        good(2)
        sleep(0.5)

    elif 80 > num1 > 76 and num1 != 77:  # 3
        view()
        good(3)
        sleep(0.5)

    elif num1 == 77:  # 1
        view()
        good(7)
        sleep(0.5)

    elif 90 > num1 > 87:  # 3
        view()
        good(4)
        sleep(0.5)

    elif 100 > num1 > 98:  # 2
        view()
        good(5)
        sleep(0.5)

    elif num1 == 100:  # 1 total 20
        view()
        good(6)
        sleep(0.5)

    else:
        view()
        print ("Nothing happend.")
        sleep(0.5)


def good(eventid):
    global health
    global progress
    # print ("This is a placeholder for a good event")
    # print ("Event Id: ", eventid)
    if eventid == 1:
        print("Congrats! you managed to find more coffee rations!")
        progress += 1
        a = input("Press Enter to continue")
    elif eventid == 2:
        print ("You managed to pach up the hull a bit, after finding some spare parts.")
        num1 = random.randint(1, 20)
        health += num1
        a = input("Press Enter to continue")
    elif eventid == 3:
        print("You find a cache of hyperfuel, allowing you to progress much faster!")
        progress += 2
        a = input("Press Enter to continue")
    elif eventid == 4:
        print("You find some freindly traders who are willing to fix your ship and spare some hyperfuel!")
        progress += 3
        health += int(health / 2)
        a = input("Press Enter to continue")
    elif eventid == 5:
        print("You found an upgrade!")
        a = random.randint(1, 2)
        upgrade()
        a = input("Press Enter to continue")
    elif eventid == 6:
        print(
            "You find a  wormhole and are magically transported inside, allowing you to cross vast distances instatly!")
        num1 = random.randint(1, 4)
        progress += num1 * 6
        a = input("Press Enter to continue")
    elif eventid == 7:
        print ("You find an elder space god, who is feeling generous today, and will grant you 1 of three things.")
        print ("1: Instant travel into deep space")
        print ("2: Massive repairs")
        print ("3: Random upgrade")
        a = input("Choice: ")
        a = int(a)
        if a == 1:
            num1 = random.randint(1, 2)
            if num1 == 1:
                num1 = random.randint(1, 5)
                progress += num1 * 5
                print(
                    "You have been instantly flug foward light years in the direction of your home, Thanks elder space god!")
                a = input("Press Enter to continue:")
            elif num1 == 2:
                num1 = random.randint(1, 5)
                progress -= num1 * 5
                print(
                    "Unfortunatly, in your hase to accept the gift of the gods, you forgot to specify what direction for him to throw you in.")
                print("You are thrown backwards in the direction which you came.")
                a = input("Press Enter to continue")
            else:
                print("MAJOR BUG FIX THIS ASSHOLE")
        elif a == 2:
            print("The god waves his hand and your ship is fully repaired.")
            health = 100
            a = input("Press Enter to continue")
        elif a == 3:
            print ("The god waves his hand and suddenly an upgrade appears on your hull.")
            a = random.randint(1, 2)
            upgrade()
            a = input("Press Enter to continue")
        else:
            print("The god is not amused. You see a flash of light, then you die.")
            health = 0
            a = input("Press Enter to coninue")


def bad(eventid):
    global health
    global progress
    # print ("This is a placeholder for a bad event")
    # print ("Event Id: ", eventid)
    if eventid == 1:
        print ("You are struck with a massive meteor, Sustaining MASSIVE hull damage.")
        num1 = random.randint(3, 10)
        health -= num1 * 10
        a = input("Press Enter to continue")
    elif eventid == 2:
        print ("You are caught in a ion storm! you have to spend a good week and a half trying to get out.")
        progress -= 20
        a = input("Press Enter to continue:")
    elif eventid == 3:
        line1 = "Congrats! \n You are caught in a meteor shower! \n your hull is torn to bits.\n"
        for x in line1:
            print(x, end='')
            sys.stdout.flush()
            sleep(0.1)
        num1 = random.randint(3, 10)
        health -= num1 * 5
        a = input("Press Enter to continue")
    elif eventid == 4:
        print ("You are caught in a massive alien fight, causing you to sustain damage and to get lost in the battle.")
        num1 = random.randint(1, 6)
        health -= num1 * 10
        a = input("Press Enter to continue")
    elif eventid == 5:
        print ("You have lost your way, again, you dolt.")
        num1 = random.randint(1, 3)
        progress -= num1 * 2
        a = input("Press Enter to continue")
    elif eventid == 6:
        print ("*THUMP* Dang. There goes another Space Wombat.")
        health -= 5
        a = input("Press Enter to continue")





