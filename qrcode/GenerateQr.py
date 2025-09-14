import qrcode

message = input('Enter the (text / URL) to put it as qrcode: ')
FileName = input ('Enter The image Name: ')

def GenerateQrCode():
	img = qrcode.make(f'{message}')
	type(img) #you dont need it
	img.save(f'{FileName}.png')

GenerateQrCode()
