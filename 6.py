array = open('6.txt', "r").read().split(',')
print(array)
day = 0
one = array.count('1')
two = array.count('2')
three = array.count('3')
four = array.count('4')
five = array.count('5')
six = array.count('6')
seven = array.count('7')
eight = array.count('8')



ones = [1]
count = 0
day = 0
while day < 80 :
	i = 0
	print('1:',day)
	for x in ones : 
		ones[i] = int(ones[i]) - 1
		if int(ones[i]) == -1 :
			ones[i] = 6
			ones.append('9')
		i += 1
	day += 1
	
twos = [2]
count = 0
day = 0
while day < 80 :
	i = 0
	print('2:',day)
	for x in twos : 
		twos[i] = int(twos[i]) - 1
		if int(twos[i]) == -1 :
			twos[i] = 6
			twos.append('9')
		i += 1
	day += 1
	
threes = [3]
count = 0
day = 0
while day < 80 :
	i = 0
	print('3:',day)
	for x in threes : 
		threes[i] = int(threes[i]) - 1
		if int(threes[i]) == -1 :
			threes[i] = 6
			threes.append('9')
		i += 1
	day += 1

fours = [4]
count = 0
day = 0
while day < 80 :
	i = 0
	print('4:',day)
	for x in fours : 
		fours[i] = int(fours[i]) - 1
		if int(fours[i]) == -1 :
			fours[i] = 6
			fours.append('9')
		i += 1
	day += 1

fives = [5]
count = 0
day = 0
while day < 80 :
	i = 0
	print('5:',day)
	for x in fives : 
		fives[i] = int(fives[i]) - 1
		if int(fives[i]) == -1 :
			fives[i] = 6
			fives.append('9')
		i += 1
	day += 1


	
	

print(len(ones))
print(len(twos)) # 210
print(len(threes)) #37
print(len(fours)) #120
print(len(fives)) #84

print(len(ones)*one+len(twos)*two+len(threes)*three+len(fours)*four+len(fives)*five)



#346200 is too low
#5550000000000 too high