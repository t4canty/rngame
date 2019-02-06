import random
from subprocess import call
from time import sleep
health = 100
damage = 5
progress = 0
hasdock = 0
def menu():
	global hasdock
	print("Welcome to the menu! What would you like to do?")
	print("1) Buy Items Requires dock")
	print("2) Veiw ship")
	print("3) Upgrade Ship")
	print("4) Talk to crew members")
	print("5) Back")
	choice = input("[==>]")
	print("DEBUG:" + choice)
	if choice == "1":
		if hasdock:
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
		veiw()
	else:
		print("Invalid choice")
def veiw():
	global health
	global progress
	global upgrade
	global name
	global damage
	print("Ship:" + name)
	print("Health:" + health)
	print("Progress" + progress)
	print("You currently do " + damage + " Damage")
	if upgrade:
		global regen
		global thrust
		global wepon
		if regen:
		 	print("You have a regen hull!")
		elif thrust:
			print("You have improved thrusters!")
		elif wepon:
			print("You have heavy wepons!")
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
			print("Plasma gun: Damage + 5")
			print("Price = 20")
			price = 20
			choice = input("Would you like to buy this? [Y/N]")
			buy(choice)
		elif a == 2:
			print("Missle launcher: Damage + 2, Sheild Peirce")
			print("Price = 30")
			price = 30
			choice = input("Would you like to buy this? [Y/N]")
			buy(choice, price)
		elif a == 3:
			print("EMP: Damage +0, disables sheilds for 2 turns")
			print("Price: 15")
			price = 15
			choice = input("Would you like to buy this? [Y/N]")
			buy(choice, price)
	elif a == 2:
		a = random.randint(1, 3)
		if a == 1:
			print("Plasma Cannon: Damage + 10")
			price = 30
		elif a == 2:
			print("Gauss Gun: Damage + 10, Sheild peirce +1")
		elif a == 3:
			print("Missle Barrage: Damage + 8, Sheild Peirce")
	elif a == 3:
		a = random.randint(1, 3)
		if a == 1:
			print("Plasma Gatling: Damage + 20")
		elif a == 2:
			print("Artillary System: Damage + 30")
		elif a == 3:
			print("Ion Cannon: Damage + 0, Disable sheilds for 5 turns")

def buy(choice, price):
	if choice == "Y" or choice == "y":
		print("Purchased, thank you!")
		inventory(1)
		credits -= price
	elif choice == "N" or choice == "n":
		print("Okay")
		pass
while True:
	sleep(1)
	call(["clear"])
	menu()

