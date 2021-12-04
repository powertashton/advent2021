array = open('4.txt', "r").read().splitlines()
numbers = array[0]
numbers = numbers.split(',')
boards = []
i = 1
while i < len(array) :
	boards.append('0')
	boards[i-1] = array[i].split(' ')
	while '' in boards[i-1] :
		boards[i-1].remove('')
	i += 1

while [] in boards :
		boards.remove([])
board = []
i=0
while i < len(boards) :
	board.append([boards[i], boards[i+1], boards[i+2], boards[i+3], boards[i+4]])
	i+=5
number = 0
for x in numbers :
	for z in board :
		if ['TRUE', 'TRUE', 'TRUE', 'TRUE', 'TRUE'] not in z :
			for y in z :
				i=0
				for k in y :
					if k == x :
						y[i] = 'TRUE'
					i += 1
			# figure out why its going to 16 and not stopping at 24...
			print(numbers[number])
		else :
			break
	
	number += 1
