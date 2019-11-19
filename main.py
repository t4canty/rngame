import game
import clear

try:
    f = open("SaveGame.txt", "r")
    f1 = f.readlines()
    i = 0
    itemList = []
    if f1[0] != "--end items--\n":
        while f1[i] != "--end items--\n":
            itemList.append(f1[0])
            i += 1
    i += 1
    planetid = int(f1[i])
    i += 1
    name = f1[i]
    i += 1
    health = int(f1[i])
    i += 1
    damage = int(f1[i])
    i += 1
    progress = int(f1[i])
    i += 1
    regen = int(f1[i])
    i += 1
    thrust = int(f1[i])
    i += 1
    wepon = int(f1[i])
    i += 1
    credits = int(f1[i])
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
while health > 0:
    clear.clear()
    #call(["clear"])
    game.menu()
print("You died!")