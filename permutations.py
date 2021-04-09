# custom get permutations
# (not working)
#
def getPermutations(string):
	wordsout = []
	words = []
	letters = []
	suffix = []
	for letter in string:
		letters.append(letter)
	f = 0
	for i, val in enumerate(letters):
		suffix = []
		prefix = letters[i]
		for l, val in enumerate(letters):
			if l != i:
				suffix.append(letters[l])
		a = len(suffix)
		b = len(suffix)-1
		x = a*b
		for z in range(0, x):
			out = ""
			out += prefix
			for s in suffix:
				out += s
			wordsout.append(out)
			if f < len(suffix)-1:
				c = suffix[f]
				suffix[f] = suffix[f+1]
				suffix[f+1] = c
				f += 1
			if f >= len(suffix)-1:
				f = 0
		f = 0
		direction = 1
		for z in range(0, x):
			out = ""
			out += prefix
			for s in suffix:
				out += s
			wordsout.append(out)
			if direction == 1 and f < len(suffix)-1:
				c = suffix[f]
				suffix[f] = suffix[f+1]
				suffix[f+1] = c
				f += direction
			if direction < 0 and f >= 0:
				f += direction
				c = suffix[f]
				suffix[f] = suffix[f+1]
				suffix[f+1] = c
			if f <= 0:
				direction = 1
				f += direction
			if f == len(suffix)-1:
				direction = -1
				f+=direction
			wordsout.append(out)
	return wordsout
