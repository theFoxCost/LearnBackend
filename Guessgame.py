
import random

GuessedNumber = random.randint(0, 100)

YourNum = int(input('What is Your Number (0 - 100): '))

def CalcTopNum():
	return GuessedNumber + 10
def CalcMinNum():
	return GuessedNumber - 10

TopNum = CalcTopNum()
MinNum = CalcMinNum()

if YourNum < MinNum :
	print("The Number Is Too Low")
elif YourNum > TopNum:
	print("The Number is Too High")
elif YourNum == GuessedNumber:
	print("Exactly !!!")
else:
	print('You are TOOOO Close')
