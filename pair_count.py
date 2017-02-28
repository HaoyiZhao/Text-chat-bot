#!/usr/bin/python
import sys
import os.path

# check if correct number of arguments
if len(sys.argv) != 2:
	print "Invalid number of arguments, please only enter only one text file name as the command line argument"
	sys.exit()
# check if valid file specified
if os.path.isfile(sys.argv[1]):
	file=open(sys.argv[1], "r+")
	pairingList=[]
	pairFrequency={}

	# read all words from file into a list, then iterate through list words
	for word in file.read().split():
		# split words up if there is a hyphen then format + store word(s) into pairingList
		for hyphenWord in word.split('-'):
			hyphenWord = ''.join(l for l in hyphenWord if l.isalpha())
			#don't add word to pairing list if simply empty string(e.g. numbers)
			if hyphenWord == '':
				continue
			hyphenWord = hyphenWord.lower()
			pairingList.append(hyphenWord)
	file.close()
	# pair all words in pairingList with the word in the next index and add pair to pairFrequency dictionary/ increment pair value
	for i in range(len(pairingList)-1):
		pair = "%s-%s" %(pairingList[i], pairingList[i+1])
		if pair in pairFrequency:	
			pairFrequency[pair] += 1
		else:
			pairFrequency[pair] = 1
	# sort by second field of tuples (values) returned by items(), then print tuple pairs
	for k,v in sorted(pairFrequency.items(), key=lambda tup:tup[1], reverse=True):
		print "%s:%s" %(k,v)
else:
	print "Invalid file name specified or file does not exist"				
