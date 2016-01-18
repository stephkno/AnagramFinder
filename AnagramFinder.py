import os
import re
import sys
os.system("clear")                                                      #clear screen
dict = open('/usr/share/dict/words', 'r')                               #open file
words = dict.read().splitlines()                                        #split words into lines
wordsout = []                                                           #create wordsout array
def permutations(string):                                               #define function
        words = []                                                      #make words array
        letters = []                                                    #make letters array
        suffix = []                                                     #make suffix array
        for letter in string:                                           #for each letter in word
                letters.append(letter)                                  #build string letter by letter
        f = 0                                                           #set swap pointer to 0
        for i, val in enumerate(letters):                               #for each letter in letters
                suffix = []                                             #clear suffix array
                prefix = letters[i]                                     #find prefix
                for l, val in enumerate(letters):                       #for each letter in letters
                        if l != i:                                      #if letter is NOT prefix then
                                suffix.append(letters[l])               #append letter to suffix array
                a = len(suffix)                                         #find length of suffix
                b = len(suffix)-1                                       #find length of suffix minus one
                x = a*b                                                 #multiply
                for z in range(0, x):                                   #for each z in 0 to product
                        out = ""                                        #clear out string
                        out += prefix                                   #add prefix to out string
                        for s in suffix:                                #for each letter in suffix
                                out += s                                #add s to out string
                        wordsout.append(out)                            #append out string to wordsout array
                        if f < len(suffix)-1:                   #if pointer is less than length of suffix minus one
                                c = suffix[f]                           #set swap buffer to letter
                                suffix[f] = suffix[f+1]                 #swap chars
                                suffix[f+1] = c                         #put swap buffer into letter+1
                                f += 1                                  #increment swap pointer
                        if f >= len(suffix)-1:                          #if pointer >= length of suffix minus one
                                f = 0                                   #set swap pointer to 0
        return wordsout                                                 #return with wordsout array
unbuffered = os.fdopen(sys.stdout.fileno(), 'w', 0)                     #set unbuffered printing mode
sys.stdout = unbuffered                                                 # ''
print ("ANAGRAM FINDER V 1.0 COPYLEFT STEPHEN KNOTTS 2016")             #splash message
count = 0                                                               #set count to zero
oldline = ""                                                            #clear oldline string
for word in words:                                                      #each word in words
        print ("Word: " + word),                                        #print word
        wo = permutations(str(word))                                    #find permutations
        wo.pop(0)                                                       #remove word from permutations
        if len(wo) < 1:                                                 #if length of permutations array < 1
                print " . . . . . . . . . . [SKIP]"                     #skip
        if len(wo) > 0:                                                 #if length of perm array > 0
                count = 0                                               #set counter to zero
                for line in wo:                                         #for each line in perm array
                        for w in words:                                 #for each word in word list
                                count+=1                                #increment counter
                                if line != oldline and line != word:    #if line is different and not word
                                        print ''                        #carriage return 
                                        print("Trying " + line),        #print permutation search attempt
                                        line = oldline                  #set line 
                                if count % 20000 < 1:                   #if time
                                        print ".",                      #print .
                                if w != word:                           #if w is not word
                                        if re.match("^" + w + "$", word):#if found match
                                                print ("FOUND MATCH! "),#
                                                print w                 #end
~                                                                               
