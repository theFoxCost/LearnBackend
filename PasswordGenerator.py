
import random


password = []
alphabets = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z",
    "0","1","2","3","4","5","6","7","8","9","!","@","#","$","%",
    "^","&","*","(",")","-","_","=","+","[","]","{","}",";",":",
    "'","\"",",",".","<",">","/","?","|","\\"
]


CharNumber = random.randint(0, 100)
def MakeRandomNumber():
	number = random.randint(0,65)
	return number
i = 0
while i < CharNumber :
	i += 1
	number = MakeRandomNumber()
	AlphaChar = alphabets[number]
	password.append(AlphaChar)
	if len(password) == CharNumber:
		print("".join(password))
	elif len(password) != CharNumber:
		continue

