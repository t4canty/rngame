import random
import game, npc, clear
from time import sleep
def eldrannon():
    clear.clear()
    print("Your ship pulls into a run-down, shady space station orbiting a gas giant.\nYou know this planet as Eldrannon, a hub for ice merchants an Pirates. You should be careful out here.")
    print("What do you do?")
    print("1) Explore a local bar")
    print("2) Go into the shady side of town")
    print("3) Leave")
    choice = input("[==>]")
    if choice == "1":
        bar()
    elif choice == "2":
        town()
    elif choice == "3":
        game.menu()
    else:
        print("Invalid choice")
        sleep(1)
        eldrannon()

def bar():
    clear.clear()
    print("Here, you see a bustling bar full of ice miners, and other ship captains.\n You notice a strange fellow eying you from the corner, and also notice a cat-man at the bar drinking alone.\n What do you do? ")
    print("1) Go up to the shady figure\n2) go up to the cat-man\n3)order a drink\n4)leave")
    choice = input("[==>]")
    if choice == "1":
        npc.shadyFellow()
        bar()
    elif choice == "2":
        npc.Casey(0)
        bar()
    elif choice == "3":
        print("you go up to the bartender, throwing a few credits onto the counter. \n \"Hit me!\" you say, confidently.")
        a = random.randint(1, 5)
        if a == 1:
            print("The bartender grins, and hands you a frothing purple glass. It smells horrible, and burns your nostrils.\n You gulp, and slam down the horrible liquid. After a few gulps, you slam the glass down with a triumphant grin.\n Suddenly, the world spins, and your vision goes black.")
            sleep(5)
            print("After a bit, you come to and look around you. you're back on your ship, with considerably less coin.")
            input("Press any key to continue.")
            game.menu()
        elif a == 2:
            print("The bartender scowls, and simply turns away. You have a nagging suspicion that he may not want to serve you anymore ...")
            input("Press any key to continue.")
            eldrannon()
        elif a == 3:
            print("You get a perfectly nice beer. Despite your bold entrance, nobody really pays attention, and you sip your beer in peace.")
            input("press any key to continue")
            bar()
        elif a == 4:
            print("The bartender looks to you, and slides a perfectly fine brandy to you. You enjoy it. ")
            input("press any key to continue")
        else:
            print("The bartender hands you a beer without any further conversation, taking the credits you threw down.\n At that moment, you see the cat man get up and walk over to you.")
            npc.Casey(1)
    elif choice == "4":
        eldrannon()
    else:
        print("Invalid Choice")
        sleep(1)
        bar()

def town():
    print("Not implemented yet")
    sleep(1)
    eldrannon()