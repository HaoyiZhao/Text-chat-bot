#!/usr/bin/python
import os.path 
import sys
import random
import pdb
# dictionary and list variables
pairDict={}
tempList=[]
# ensure there is at least one command line argument, otherwise exit
if len(sys.argv)<2:
	print "Invalid number of command line arguments"
	sys.exit()
# iterate through all files, and add all words into a list
for j in range(1, len(sys.argv)):
	if os.path.isfile(sys.argv[j]):
		file=open(sys.argv[j], "r+")
		# read all words from file into a list, then iterate through list words, adding to tempList
		for word in file.read().split():
			# split "word" up if there is a hyphen then format + store word(s) into tempList, but keep sentence-ending punctuation
			for hyphenWord in word.split('-'):
				if hyphenWord == "":
					continue
				if hyphenWord[len(hyphenWord)-1]=='.':
					hyphenWord = ''.join(l for l in hyphenWord if l.isalpha())
					hyphenWord += '.'
				elif hyphenWord[len(hyphenWord)-1]=='?':
					hyphenWord = ''.join(l for l in hyphenWord if l.isalpha())
					hyphenWord += '?'
				elif hyphenWord[len(hyphenWord)-1]=='!':
					hyphenWord = ''.join(l for l in hyphenWord if l.isalpha())
					hyphenWord += '!'
				else:
					hyphenWord = ''.join(l for l in hyphenWord if l.isalpha())
				# don't add word to pairing list if simply empty string(e.g. numbers)
				if hyphenWord == "":
					continue
				# if sentence ends in a number, add period to previous word and continue
				if hyphenWord == ".":
					tempList[len(tempList)-1] = tempList[len(tempList)-1] + "."
					continue
				hyphenWord = hyphenWord.lower()
				tempList.append(hyphenWord)
		file.close()
		# add eof as a marker in order to prevent cross-file word pairs
		tempList.append("eof")
	else: 
		print "%s does not exist" %(sys.argv[j])
# add word pairs to dictionary using tempList
for i in range(len(tempList)-1):
	# at index before end of file, increment index by 2 to get to beginning of next file
	if tempList[i+1] == "eof":
		# break if last word in last file is reached
		if i==len(tempList)-2:
			break
		else:
			i += 2
	else:
		pair = "%s-%s" %(tempList[i], tempList[i+1])
		if pair in pairDict:
			pairDict[pair] += 1
		else:
			pairDict[pair] = 1
# Loop until program exits

while(1):
	wordCounter = 0
	botMessage = ""
	previousWord = ""
	end = 0
	input = raw_input("Send:")
	# if no input entered, prompt for message
	if input == None:
		print "Please enter a message"
		continue
	# check if last word in user message is in pairDictionary as the first word of a word pair, and add second word of pair to botMessage 		if it is 
	else:
		qn = input.rsplit(None, 1)[-1]
		qn = qn.lower()
		qn = ''.join(l for l in qn if l.isalpha())
	for pair in pairDict:
		word = pair.rsplit('-', 1)[0]
		word = ''.join(l for l in word if l.isalpha())
		if qn == word:
			tempWord = pair.rsplit('-', 1)[1]
			# check if temp word is first of a word pair in dictionary, removing end punctuation if applicable
			tempWord = ''.join(l for l in tempWord if l.isalpha())
			# exit if temp word is not first of a word pair
			end = 1
			for tempPair in pairDict:
				# remove end punctuation from first tempPair elements if applicable before comparing
				if ''.join(l for l in tempPair.rsplit('-', 1)[0] if l.isalpha()) == tempWord:
					end = 0
					break
			tempWord = tempWord.capitalize()
			botMessage += tempWord
			if end==0:
				botMessage += " "
				wordCounter += 1
				previousWord=tempWord
			break
	# if word not in pairDictionary as the first word of a pair, choose a random word from text to begin botMessage
	if botMessage == "":
		tempPair = random.sample(pairDict, 1)[0]
		tempWord = random.choice(tempPair.rsplit('-', 1))
		# Check if tempword is the first word of a word pair in dictionary, removing end punctuation if applicable
		tempWord = ''.join(l for l in tempWord if l.isalpha())
		# exit if tempword is not first word of a word pair in dictionary
		end = 1
		for pair in pairDict:
			word = pair.rsplit('-', 1)[0]
			# remove end punctuation from first elements of pair before comparing
			word = ''.join(l for l in word if l.isalpha())
			if tempWord==word:
				end = 0
				break	
		botMessage += tempWord.capitalize() 
		# format botMessage, set previousWord to tempWord and increment wordCounter if end==0
		if end==0:
			botMessage += " "
			wordCounter += 1
			previousWord = tempWord		
	possibleWords=[]	
	while(end==0):
		# if wordCounter<20, continue adding words to response
		if wordCounter<20:
			# add possible words depending on previousWord to list possibleWords
			for pair in pairDict:
				tempWord=''.join(l for l in pair.rsplit('-', 1)[0] if l.isalpha())
				if tempWord==previousWord.lower():
					possibleWords.append(pair.rsplit('-', 1)[1])
			# if possible words exist, assign to word, otherwise exit
			if len(possibleWords)>0:
				word = random.choice(possibleWords)
			else:
				end = 1
				break
			# reset possibleWords for next word
			del possibleWords[:]
			# check if stop pair, if true, add to botMesssage, then exit
			if word[len(word)-1]=="." or word[len(word)-1]=="?" or word[len(word)-1]=="!":
				botMessage += word[0:len(word)-1]
				end=1
			# add to botMessage, then set up for next word
			else:
				botMessage += word
				if wordCounter!=19:
					botMessage += " "
					previousWord = word
				wordCounter += 1
		# if wordCounter>20, exit		
		else:
			end=1
	# add period to end of botMessage, then print
	botMessage += "."
	print "Received:%s" %(botMessage)
		
	

	
