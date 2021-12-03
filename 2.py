#Day 2 Part 1 - 12 Lines
array = open('2.txt', "r").read().splitlines()
horizontal = 0
vertical = 0
for x in array :
	y = x.split(' ')
	if y[0] == 'forward' :
		horizontal += int(y[1])
	elif y[0] == 'up' :
		vertical -= int(y[1])
	elif y[0] == 'down' :
		vertical += int(y[1])
print(vertical * horizontal)

#Day 2 Part 2 - 14 Lines
array = open('2.txt', "r").read().splitlines()
horizontal = 0
vertical = 0
aim = 0
for x in array :
	y = x.split(' ')
	if y[0] == 'forward' :
		horizontal += int(y[1])
		vertical += aim * int(y[1])
	elif y[0] == 'up' :
		aim -= int(y[1])
	elif y[0] == 'down' :
		aim += int(y[1])
print(vertical * horizontal)

