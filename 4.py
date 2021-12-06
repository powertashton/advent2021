#Part 2 - 54 lines (unoptimised)
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
final = []
score = []
c = []
while len(board) > 0 :
	for z in board :
		p = 0
		for x in numbers :
			if ['TRUE', 'TRUE', 'TRUE', 'TRUE', 'TRUE'] not in z :
				for y in z :
					i=0
					for k in y :
						if k == x :
							y[i] = 'TRUE'
						i += 1
				if ['TRUE', 'TRUE', 'TRUE', 'TRUE', 'TRUE'] in z :
					g = 0
					for x in z :
						for y in x:
							if y != 'TRUE' :
								g += int(y)
					score.append(int(g/2))
					c.append(p)
					board.remove(z)
					break
			p += 1
largest = c[0]
for x in c :
	if x > largest :
		largest = x
print(score[c.index(largest)] * int(numbers[largest]))