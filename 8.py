array = open('8.txt', "r").read().splitlines()
i = 0
for x in array :
	stepone = x.split(' | ')
	steptwo = stepone[0].split(' ')
	a = []
	b = [] 
	c = []
	d = [] 
	e = [] 
	f = []
	g = []
	for y in steptwo :
		if len(y) != 4 or  len(y) != 3 or  len(y) != 7 or  len(y) != 2 :
			if y == 'a':
				a.append(1)
			elif y == 'b':
				b.append(1)
			elif y == 'c':
				c.append(1)
			elif y == 'd':
				d.append(1)
			elif y == 'e':
				e.append(1)
			elif y == 'f':
				f.append(1)
			elif y == 'g':
				g.append(1)
			
		
			
	
	output = stepone[1].split(' ')
	for y in output :
		if len(y) == 4 or  len(y) == 3 or  len(y) == 7 or  len(y) == 2 :
			i += 1

print(i)
		