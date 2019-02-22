#import fights.py
#import enemies.py
#import crew.py
import random
from subprocess import call
from time import sleep
import sys
planetid=0
name="PlaceHolder Name, Replace with player Input"
health = 100
damage = 5
progress = 0
hasdock = 1
regen=0
thrust=0
wepon=0
credits=100
def menu():
	global hasdock
	global notdone
	print("Welcome to the menu! What would you like to do?")
	print("1) Buy Items Requires dock")
	print("2) Veiw ship")
	print("3) Upgrade Ship")
	print("4) Talk to crew members")
	print("5) Back")
	print("6) Continue")
	choice = input("[==>]")
	print("DEBUG:" + choice)
	sleep(0.5)
	if choice == "1":
		if hasdock:
			call(["clear"])
			shop()
		else:
			print("There is no dock!")
	elif choice == "2":
		inventory()
	elif choice == "3":
		upgrade()
	elif choice == "4":
		talk()
	elif choice == "5":
		global planetid
		call(["clear"])
		planet(planetid)
		veiw()
	elif choice == "6":
		notdone=0
	else:
		print("Invalid choice")
def veiw():
	global health
	global progress
	global upgrade
	global name
	global damage
	global credits
	print("Ship:" + name)
	print("Health:" , health)
	print("Progress:" , progress)
	print("You currently do " , damage , " Damage")
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
			print("You have heavy wepons!")
		elif wepon and thrust and not regen:
			print("You have heavy wepons and improved thrusters!")
		elif wepon and regen and not thrust:
			print("You have heavy wepons and a regen hull!")
		elif thrust and regen and not wepon:
			print("You have improved engines and a regen hull!")
		elif wepon and thrust and regen:
			print("You have a maxed out ship, what a chad!")
def shop():
	global credits
	num = 0
	print("Welcome to my shop! We have many wepons such as:")
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
			id=0
			print("Plasma gun: Damage + 5")
			print("Price = 20")
			price = 20
			choice = input("Would you like to buy this? [Y/N]")
			buy(choice, price, id)
		elif a == 2:
			id=1
			print("Missle launcher: Damage + 2, Sheild Peirce")
			print("Price = 30")
			price = 30
			choice = input("Would you like to buy this? [Y/N]")
			buy(choice, price, id)
		elif a == 3:
			id=2
			print("EMP: Damage +0, disables sheilds for 2 turns")
			print("Price: 15")
			price = 15
			choice = input("Would you like to buy this? [Y/N]")
			buy(choice, price, id)
	elif a == 2:
		a = random.randint(1, 3)
		if a == 1:
			id=3
			print("Plasma Cannon: Damage + 10")
			price = 30 + random.randint(1, 10)
			print("Price:", price)
			choice = input("Would you like to buy this? [Y/N]")
			buy(choice, price, id)
		elif a == 2:
			id=4
			print("Gauss Gun: Damage + 10, Sheild peirce +1")
			price = 50 + random.randint(5, 20)
			print("Price:", price)
			choice = input("Would you like to buy this? [Y/N]")
			buy(choice, price, id)
		elif a == 3:
			id=5
			print("Missle Barrage: Damage + 8, Sheild Peirce")
			price = 40 + random.randint(1, 50)
			print("Price:", price)
			choice = input("Would you like to buy this? [Y/N]")
			buy(choice, price, id)
	elif a == 3:
		a = random.randint(1, 3)
		if a == 1:
			id=6
			print("Plasma Gatling: Damage + 20")
			price = 70 + random.randint(1, 40)
			print("Price:", price)
			choice = input("Would you like to buy this? [Y/N]")
			buy(choice, price, id)
		elif a == 2:
			id=7
			print("Artillary System: Damage + 30")
			price = 100 + random.randint(1, 60)
			print("Price:", price)
			choice = input("Would you like to buy this? [Y/N]")
			buy(choice, price, id)
		elif a == 3:
			id=8
			print("Ion Cannon: Damage + 0, Disable sheilds for 5 turns")
			price = 140 + random.randint(-10, 20)
			print("Price:", price)
			choice = input("Would you like to buy this? [Y/N]")
			buy(choice, price, id)

def buy(choice, price, id):
	global credits
	if choice == "Y" or choice == "y" :
		if credits > 0 and price <= credits:
			print("Purchased, thank you!")
			#inventory(id)
			print(id)
			credits -= price
		else:
			print("OI!, You don't have enough money!")
	elif choice == "N" or choice == "n":
		print("Okay")
		pass
	elif credits <= 0:
		print("You do not have enough cash, screw off!")

def inventory(id):
	print("Not implemented yet")
def upgrade():
	print("Not implemented yet")
def talk():
	print("Not implemented yet")
def planet(planetid):
	global progress
	if planetid == 0:
		print("The wonderful world of Starlaxia, the greatest space station ever built.")
		print("You grew up here, and learned to love this place. This place has a special location in your heart, literally.")
		print("You got your first aortal implant here.")
		print("What do you want to do?")
		print("1: Menu")
		print("2: Continue")
		ch = input("[==>]")
		if ch == "1":
			menu()
		else:
			progress += 1
while True:
	sleep(1)
	call(["clear"])
	veiw()
	menu()
