
import time
import os

sec = 00
min = 00
hr = 00

while True:
	sec += 1
	time.sleep(1)
	os.system("clear")
	if sec == 60:
		min += 1
		sec = 0
		if min == 60:
			hr += 1
			sec = 0
			min = 0
			if hr == 25:
				hr = 0
				sec = 0
				min = 0
			else:
				continue
		else:
			continue
	else:
		print(f"{hr:02}:{min:02}:{sec:02}")
		continue
