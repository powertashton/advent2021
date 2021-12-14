array = open('7.txt', "r").read().split(',')
highest = 0

for x in array :
	if int(x) > highest :
		highest = int(x)

fuels = []
pos = 0
while pos < highest :
	fuel = 0
	for x in array :
		fuel = (abs(pos - int(x)))
		i = 0
		while i < abs(pos - int(x)) :
			fuel += abs(pos - int(x))-i
			i += 1
		fuels.append(fuel)
	pos += 1	
print(fuels)

		
print(min(fuels))

