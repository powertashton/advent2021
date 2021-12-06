array = open('6.txt', "r").read().split(',')
print(array)
day = 0

while day < 256 :
	i = 0
	for x in array : 
		array[i] = int(array[i]) - 1
		if int(array[i]) == -1 :
			array[i] = 6
			array.append('9')
		i += 1
	day += 1

print(len(array))

