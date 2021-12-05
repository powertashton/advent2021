#Part 1 - 57 lines (unoptimised)
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

i=0
for x in board :
	p=0
	while p < 5 :
		x.append([x[i][p],x[i+1][p],x[i+2][p],x[i+3][p],x[i+4][p]])
		p += 1

bingo = 'FALSE'
p = 0
for x in numbers :
	if bingo == 'FALSE' :
		current = 0
		for z in board :
			if ['TRUE', 'TRUE', 'TRUE', 'TRUE', 'TRUE'] not in z :
				for y in z :
					i=0
					for k in y :
						if k == x :
							y[i] = 'TRUE'
						i += 1
			else :
				bingo = z
				final = int(numbers[p-1])
				break
			current += 1
	p +=1

g = 0
winner = board[current]

for x in winner :
	for y in x:
		if y != 'TRUE' :
			g += int(y)
	
print(int(g/2) * final)
	
