#!/usr/bin/env python
import os
import re
import subprocess
import sys
os.system("clear")
dict = open('/usr/share/dict/wordlist', 'r')		
dictwords = dict.read().splitlines()	 	
wordsout = []				
words = []
def permutations(string):		 
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
unbuffered = os.fdopen(sys.stdout.fileno(), 'w', 0)		
sys.stdout = unbuffered		
print ("Anagrams")	
count = 0		
oldline = ""		
anagrams = []
#inp = raw_input(">")
count = 0
for word in dictwords:
	print word + ":",
	#print anagrams, word 
	perms = []
	perms = permutations(str(word))
	#print perms
	for perm in perms:
		for word in open("/usr/share/dict/wordlist").read().split():
			if word in perm:
				if len(word) > 2:
					m = True
					for anagram in anagrams:
						#print anagrams
						if word.lower() == anagram.lower():
							 m = False
					if m == True and perm != word:
						print word.lower(),
						anagrams.append(word.lower())
	print
	#print anagrams
	anagrams = []
