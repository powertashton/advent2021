array = open('1.txt', "r").read().splitlines()
i = 0
total = 0
for x in array :
	if i > 2 :
		if (int(array[i]) + int(array[i-1]) + int(array[i-2])) > (int(array[i-1]) + int(array[i-2]) + int(array[i-3])) : total += 1
	i += 1
print(total)
