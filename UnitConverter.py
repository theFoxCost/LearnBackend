
#c to f
print("Choose your Options")
print('1# F --> C')
print("2# C --> F")

choice = input('My choice is : ')


def ftoc():
	x = int(input("x = "))
	f = (x * 1.8) + 32
	return print(f)
def ctof():
	x = int(input("x = "))
	c = (x/1.8) - 32
	return print(c)

def asking():
	if choice == '1':
		ftoc()
	elif choice == '2':
		ctof()
	else:
		print("number invalid")

while True:
	asking()
	Response = input('Do you want to keep up (y/n)')
	if Response == 'y':
		continue
	elif Response == "n":
		break
	else:
		print("Choice invalid")
		break
