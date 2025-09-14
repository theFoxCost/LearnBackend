ToDoList = ["Hello World",'Hello World2', 'Hello Wolld', 'Mom']

print('Welocome to Do List')


def RemoveItem():
        ItemDel = int(input("Select item you want to delete: "))
        ToDoList.pop(ItemDel)
        print('Done !')

def ShowList():
	i = 0
	for i in range(len(ToDoList)):
		print(f'{i}. {ToDoList[i]}')


def GetInput():
	print(" 1- Add To DO Note \n 2- Remove To DO Note \n 3- See All Notes")
	print("Insert Your Option :")
	choice = input()
	if choice == '1':
		AddItem()
	elif choice == '2':
		RemoveItem()
	elif choice == "3":
		ShowList()
	else:
		print('Invalid Number')

def AddItem():
	while True:
		print("Do you Wnat To keep Up (y/n)")
		Resp = input("-->")
		if Resp == "y":
			print("Type Your To Do List")
			Note = input('-->')
			ToDoList.append(Note)
			print('Do you want to keep up (y/n)')
			Response = str(input())

		elif Resp == "n":
			break
		else:
			print('Is This Joke')
			break

GetInput()
