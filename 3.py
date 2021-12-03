#Part 1 - 37 Lines
def BinaryToDecimal(binary) :
	decimal = 0
	for num in binary:
			decimal = decimal*2 + int(num)
	return decimal

def bitCounts(bits, test) :
	zeros = [0,0,0,0,0,0,0,0,0,0,0,0]
	ones = [0,0,0,0,0,0,0,0,0,0,0,0]
	gamma = [0,0,0,0,0,0,0,0,0,0,0,0]
	epsilon = [0,0,0,0,0,0,0,0,0,0,0,0]
	for q in bits :
		e = 0
		w = [char for char in q]
		for t in w :
			if int(t) == int(1) :
				ones[e] += 1
			elif int(t) == int(0) :
				zeros[e] += 1
			e += 1
	h = 0 
	for r in zeros :
		if int(zeros[h]) > int(ones[h]) :
			epsilon[h] = 1
		elif int(ones[h]) > int(zeros[h]) :
			gamma[h] = 1
		elif int(ones[h]) == int(zeros[h]) :
			gamma[h] = 1
		h += 1
	if test == 'TRUE' :
		return gamma
	else :
		return epsilon

epsilon = bitCounts(open('3.txt', "r").read().splitlines(), 'TRUE')
gamma = bitCounts(open('3.txt', "r").read().splitlines(), 'FALSE')
print(BinaryToDecimal(''.join(map(str, epsilon)))*BinaryToDecimal(''.join(map(str, gamma))))

#Part 2 - 45 Lines
def BinaryToDecimal(binary) :
	decimal = 0
	for num in binary:
			decimal = decimal*2 + int(num)
	return decimal

def bitCounts(bits, test) :
	zeros = [0,0,0,0,0,0,0,0,0,0,0,0]
	ones = [0,0,0,0,0,0,0,0,0,0,0,0]
	gamma = [0,0,0,0,0,0,0,0,0,0,0,0]
	epsilon = [0,0,0,0,0,0,0,0,0,0,0,0]
	for q in bits :
		e = 0
		w = [char for char in q]
		for t in w :
			if int(t) == int(1) :
				ones[e] += 1
			elif int(t) == int(0) :
				zeros[e] += 1
			e += 1
	h = 0 
	for r in zeros :
		if int(zeros[h]) > int(ones[h]) :
			epsilon[h] = 1
		elif int(ones[h]) > int(zeros[h]) :
			gamma[h] = 1
		elif int(ones[h]) == int(zeros[h]) :
			gamma[h] = 1
		h += 1
	if test == 'TRUE' :
		return gamma
	else :
		return epsilon

def stupidListShit(array, test) :
	p = 0
	while len(array) > 1 :
		thing = bitCounts(array, test)
		array = [line for line in array if line[p] == str(thing[p])]
		p += 1
	return array

oxygen = stupidListShit(open('3.txt', "r").read().splitlines(), 'TRUE')
co2 = stupidListShit(open('3.txt', "r").read().splitlines(), 'FALSE')
print(BinaryToDecimal(''.join(map(str, co2)))*BinaryToDecimal(''.join(map(str, oxygen))))