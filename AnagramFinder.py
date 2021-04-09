#!/usr/bin/env python
import os
import re
import subprocess
import sys
from permutations import getPermutations
from itertools import permutations

file = '/usr/share/dict/words'
os.system("clear")
wordList = open(file, 'r').read()
wordList = wordList.splitlines()
wordOut = []
wordDict = {}
words = []
#use built-in vs custom permutation method
use_itertools = True
# unbuffered = os.fdopen(sys.stdout.fileno(), 'w', 0)
# sys.stdout = unbufferd
wordSet = set(wordList)
wordFromStdin = False

# if finding anagrams of word from stdin
if len(sys.argv) > 1:
	wordList = [sys.argv[1]]
	wordFromStdin = True
# performing analysis of all words from dictionary file
else:
	print ("Anagram analysis of words from {}".format(file))

anagrams = 0
word_with_most_anagrams = ""
longest_word_with_anagram = ""
most_anagrams = 0
longest_anagram = 0

# finding permutations of each word in list
for word in wordList:
	#reset permutation set
	permSet = set()

	# display word
	print(word + ": ",end="")

	# use either built-in or custom permutations
	#
	# this operation takes the most time
	# O(n!) possibly?
	#
	if use_itertools:
		permList = set(permutations(str(word)))
	else:
		permList = set(getPermutations(str(word)))

	# adding every permutation to permutation set
	permSet = set(["".join(perm) for perm in permList])
	# find all permutations that are in word dictionary
	anagrams = list(wordSet.intersection(permSet))

	# update statistics
	if(len(anagrams)>0):
		# finding longest word with anagrams
		if len(word) > longest_anagram:
			longest_word_with_anagram = word
		longest_anagram = max(len(word), longest_anagram)

		# finding word with most anagrams
		if len(word) > most_anagrams:
			word_with_most_anagrams = word
		most_anagrams = max(len(anagrams), most_anagrams)

		# print anagrams
		for word in anagrams:
			print(word, end=" ")
			# check
		print()

	# print perms
if anagrams == 0:
	print("None.")
if not wordFromStdin:
	print("Longest word with anagrams: {} ({}) letters".format(longest_word_with_anagram, longest_anagram))
	print("Word with most anagrams: {} ({}) anagrams".format(word_with_most_anagrams, most_anagrams))
