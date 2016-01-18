import os
import re
import sys
os.system("clear")

dict = open('/usr/share/dict/words', 'r')
words = dict.read().splitlines()


class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)


wordsout = []
def permutations(string):

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
		
	return wordsout
	

print ("ANAGRAM FINDER V 1.0 BY STEPHEN KNOTTS 2016")
count = 0
oldline = ""
for word in words:

	wo = permutations(str(word))
	count = 0	
	for line in wo:
			
		for w in words:
			count+=1
			if line != oldline:
				print ''
				print("Trying " + line),
				line = oldline
			if count % 20000 < 1:
				sys.stdout = Unbuffered(sys.stdout)
				print ".",	
			if w != word:

				if re.match("^" + w + "$", word):
					#print
					print ("FOUND MATCH! "),
					print w
