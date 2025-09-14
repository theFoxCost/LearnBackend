#!/usr/bin/env python3


while True:
	print('What Operation You Want to Do :')
	print('1# Multiply \n')
	print('2# Devide \n')
	print('3# Addition \n')
	print('4# Substraction \n')
	Resp = input('Choice: ')
	if Resp == "1":
		x = int(input('x = '))
		y = int(input ('y = '))
		print(x * y)
	elif Resp == "2":
		x = int(input('x = '))
		y = int(input ('y = '))
		print(x / y)
	elif Resp == "3":
		x = int(input('x = '))
		y = int(input ('y = '))
		print(x + y)
	elif Resp == "4":
		x = int(input('x = '))
		y = int(input ('y = '))
		print(x - y)

	print('Do You Wnat to End (y/n)')
	end = input('Choice: ')
	if end == "y":
		break
	elif end == "n":
		continue
	else:
		print ("Fuck off")
