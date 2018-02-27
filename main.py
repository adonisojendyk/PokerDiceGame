from random import randint
# function ^
def isEven(number):
	if (number % 2 == 0):
		return True
	else:
		return False

def isOdd(number):
	if (number % 2 == 1):
		return True
	else:
		return False 
	
print("### POKER DICE ###")
print("")

score = 0 

dice1 = randint(1,6)
dice2 = randint(1,6)
dice3 = randint(1,6)

print("Dice 1: " +str(dice1))
print("Dice 2: " +str(dice2))
print("Dice 3: " +str(dice3))

if isEven(dice1)== True and isEven(dice2)== True and isEven(dice3)==True:
	print("3 Even Numbers!")
	score = score + 15
	
if isOdd(dice1)== True and isOdd(dice2)==True and isOdd(dice3)==True:
	print("3 Odd Numbers!")
	score = score + 15
	
if dice1==dice2 and dice2==dice3:
	print("3 of a Kind!")
	score = score + 50
	
if dice1==dice2 or dice1==dice3 or dice2==dice3:
	print("A Pair!")
	score = score + 10
	
if (dice1-dice2)==1 and (dice2-dice3)==1:
	score = score + 30
if (dice1-dice3)==1 and (dice3-dice2)==1:
	score = score + 30
if (dice3-dice2)==1 and (dice2-dice1)==1:
	score = score + 30
if (dice2-dice3)==1 and (dice3-dice1)==1:
	score = score + 30
if (dice2-dice1)==1 and (dice2-dice3)==1:
	score = score + 30
	
print("Score: " + str(score))
