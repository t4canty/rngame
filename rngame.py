import random
import sys
from subprocess import call
import time
from itertools import cycle

turn = 0
health = 100
goodevents = 0
badevents = 0
upgrade1 = 0
upgrade2 = 0
def event():
	global turn
	global goodevents
	global badevents
	num1 = random.randint(0 , 100)
	#num1 = 77
	if num1 == 0: #1
		bad(1)
		badevents += 1
	elif num1 < 10 and num1 > 7: #2
		bad(2)
		badevents += 1
	elif num1 < 20 and num1 > 17: #3
		bad(3)
		badevents += 1
	elif num1 < 30 and num1 > 27: #3
		bad(4)
		badevents += 1
	elif num1 < 40 and num1 > 35: #5
		bad(5)
		badevents += 1
	elif num1 < 50 and num1 > 45: #5 total 20
		bad(6)
		badevents += 1
	elif num1 < 60 and num1 > 54: #6
		good(1)
		goodevents += 1
	elif num1 < 70 and num1 > 66: #4
		good(2)
		goodevents += 1
	elif num1 < 80 and num1 > 76 and num1 != 77: #3
		good(3)
		goodevents += 1
	elif num1 == 77: #1
		good(7)
		goodevents += 1
	elif num1 < 90 and num1 > 87: #3
		good(4)
		goodevents += 1
	elif num1 < 100 and num1 > 98: #2
		good(5)
		goodevents += 1
	elif num1 == 100: #1 total 20
		good(6)
		goodevents += 1
	else:
		print ("Nothing happend.")
def good(eventid):
	global health
	global turn
	#print ("This is a placeholder for a good event")
	#print ("Event Id: ", eventid)
	if eventid == 1:
		print("Congrats! you managed to find more coffee rations!")
		turn +=1
		a = input("Press Enter to continue")
	elif eventid == 2:
		print ("You managed to pach up the hull a bit, after finding some spare parts.")
		num1 = random.randint(1, 20)
		health += num1
		a = input("Press Enter to continue")
	elif eventid == 3:
		print("You find a cache of hyperfuel, allowing you to progress much faster!")
		turn += 2
		a = input("Press Enter to continue")
	elif eventid == 4:
		print("You find some freindly traders who are willing to fix your ship and spare some hyperfuel!")
		turn += 3
		health += health/2
		a = input("Press Enter to continue")
	elif eventid == 5:
		print("You found an upgrade!")
		a = random.randint(1, 2)
		upgrade(a)
		a = input("Press Enter to continue")
	elif eventid == 6:
		print("You find a  wormhole and are magically transported inside, allowing you to cross vast distances instatly!")
		num1 = random.randint(1, 4)
		turn += num1*6
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
				turn += num1*5
				print("You have been instantly flug foward light years in the direction of your home, Thanks elder space god!")
				a = input("Press Enter to continue:")
			elif num1 == 2:
				num1 = random.randint(1, 5)
				turn -= num1*5
				print("Unfortunatly, in your hase to accept the gift of the gods, you forgot to specify what direction for him to throw you in.")
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
			upgrade(a)
			a = input("Press Enter to continue")
		else:
			print("The god is not amused. You see a flash of light, then you die.")
			health = 0
			a = input("Press Enter to coninue")
def bad(eventid):
	global health
	global turn
	#print ("This is a placeholder for a bad event")
	#print ("Event Id: ", eventid)
	if eventid == 1:
		print ("You are struck with a massive meteor, Sustaining MASSIVE hull damage.")
		num1 = random.randint(3, 10)
		health -= num1*10
		a = input("Press Enter to continue")
	elif eventid == 2:
		print ("You are caught in a ion storm! you have to spend a good week and a half trying to get out.")
		turn -=20
		a =  input("Press Enter to continue:")
	elif eventid == 3:
		line1 = "Congrats! \n You are caught in a meteor shower! \n your hull is torn to bits.\n"
		for x in line1:
			print(x, end='')
			sys.stdout.flush()
			time.sleep(0.1)
		num1 = random.randint(3, 10)
		health -= num1*5
		a = input("Press Enter to continue")
	elif eventid == 4:
		print ("You are caught in a massive alien fight, causing you to sustain damage and to get lost in the battle.")
		num1 = random.randint(1, 6)
		health -= num1*10
		a = input("Press Enter to continue")
	elif eventid == 5:
		print ("You have lost your way, again, you dolt.")
		num1 = random.randint(1, 3)
		turn -= num1*2
		a = input("Press Enter to continue")
	elif eventid == 6:
		print ("*THUMP* Dang. There goes another Space Wombat.")
		health -= 5
		a = input("Press Enter to continue")
def display():
	global goodevents
	global badevents
	global turn
	global health
	call(["clear"])
	#animation = cycle('[' + ' ' * n + '=' + ' ' * (6 - n) + ']' for n in range(7) + range(6, -1, -1))
	#animation = ('[=      ]', '[ =     ]', '[  =    ]', '[   =   ]',
         #         '[    =  ]', '[     = ]', '[      =]', '[      =]',
         #         '[     = ]', '[    =  ]', '[   =   ]', '[  =    ]',
         #         '[ =     ]', '[=      ]')
	print ("   [\"")
	print ("|||=======[]\"")
	print ("|||------\___\"")
	print ("  ~~~~")
	print ("HP:",health)
	print ("Progress:",turn)
	print ("Good Events:",goodevents)
	print ("Bad Events:",badevents)
	if upgrade1 == 1:
		print ("You have an improved engine")
	elif upgrade2 == 1:
		print ("You have a regen hull!")
	elif upgrade2 == 1 and upgrade1 == 1:
		print ("You have a jacked ass ship")
	else:
		pass
	#for i in range(100):
	#	sys.stdout.write('\b\b\b')
	#	sys.stdout.write(animation[i % len(animation)])
	#	sys.stdout.flush()
	#	time.sleep(0.2)
def upgrade(a):
	global upgrade1
	global upgrade2
	if a == 1:
		upgrade1 = 1
	elif a  == 2:
		upgrade2 = 1

while turn < 100 and health > 0:
	while turn == 0:
		display()
		print("Your ship is a family heirloom that has been passed down from generation to generation, now falling to you.")
		print("Unfortunatly, you are a dolt and have managed to get yourself lost in space, and must find your way home.")
		print("Good Luck!")
		print("What do you want to do?")
		print("1) Leave ship")
		print("2) Begin")
		choice = input("Choice:")
		if choice == "1":
			while turn == 0:
				print ("You leave your ship, thinking 'Boy that whole ship thing seemed like a lot of work, i dont think im going to do that.'")
				print ("You step off the ship and immediently begin playing a much better game with actual coders and writers instead of this POS.")
				print ("Congrats! You beat the game by doing LITERALLY NOTHING! Would you like to play again for real this time?")
				choice2 = input ("Y or N: ")
				if choice2 == "Y":
					turn += 1
				elif choice2 == "N":
					print("Figures")
					sys.exit()
				else:
					print("Pick Y or N you dolt!")
		elif choice == "2":
			turn += 1
		else:
			print ("Pick 1 or 2 you dolt!")
			time.sleep(1)
	else:
		display()
		event()
		time.sleep(0.5)
		if upgrade2 == 1:
			if health < 100:
				health += 1
		if upgrade1 == 1:
			turn += 2
		else:
			turn += 1
if health > 0:
	display()
	print("Congrats, you made it home!")
	print("you win!")

else:
	display()
	print("You have died!")

