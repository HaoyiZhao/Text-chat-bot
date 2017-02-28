#!/usr/bin/python
import sys
import os.path

# check if correct number of arguments
if len(sys.argv)!=2:
	print "Invalid number of arguments, please only enter only one text file name as the command line argument"
	sys.exit()
# check if file exists
if os.path.isfile(sys.argv[1]):
	file=open(sys.argv[1], "r+")
	wordFrequency={}
	# read all words in file into a list, then iterate through list words
	for word in file.read().split():
		# separate word by hyphens, if it has hyphens
		for hyphenWord in word.split('-'):
			hyphenWord = ''.join(l for l in hyphenWord if l.isalpha())
			# don't add word if it is a empty string after removing non-alphabetic characters(e.g. numbers)
			if hyphenWord == '':
				continue;
			hyphenWord = hyphenWord.lower()
			if hyphenWord in wordFrequency:
				wordFrequency[hyphenWord] += 1
			else:
				wordFrequency[hyphenWord] = 1
	# sort by second field of tuples (values) returned by items(), then print tuple pairs
	file.close()
	for k,v in sorted(wordFrequency.items(), key=lambda tup:tup[1], reverse=True):
		print "%s:%s" %(k,v)
else:
	print "Invalid file name specified"



