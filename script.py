ToDoList = ["Hello World",'Hello World2', 'Hello Wolld', 'Mom']

print('Welocome to Do List')

def ShowList():
	for x in ToDoList:
	print(x)

	#i = 0
	#while i < len(ToDoList) :
	#	i += 1
	#	return print(ToDoList[i])

ShowList()
def GetInput():
	print("1-Add To DO Note \n 2-Remove To DO Note \n 3-See All Notes")
	print("Insert Your Option :")
	choice = str(input())
	if choice == '1':
		AddItem
	elif choice == '2':
		RemoveItem()
	elif choice == "3":
		GetInput()
	else:
		print ('Invalid Number')
def AddItem():
	Print("Type Your To Do List")
	Note = input('-->')
	ToDoList.append(Note)
	Print('Do you want to keep up (y/n)')
	Response = str(input())
	while Response != "y"
		Print("Type Your To Do list")
		Note = input('--->')
		ToDoList.append(Note)
		Print('Do you want to keep up (y/n)')
        	Response = str(input())
		if Response == "n"
			break
		elif Response == "y"
			continue


def RemoveItem():
	print('Select item you want to Delte')
	ItemDel = input()
	ToDoList.remove(ItemDel)
	print('Done !')
