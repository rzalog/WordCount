#!/usr/local/Cellar/python3/3.5.2_1/bin/python3.5

import epubutils

def createSortedWordList(textString):
	# takes a normal string formatted like a book
	
	newString = stripNonAlpha(textString)

def stripNonAlpha(string, leaveApostrophes=True):
	formattedString = ''
	for char in string:
		otherValidChars = [' ', '’', '\'']
		if char.isalpha() or char in otherValidChars:
			formattedString += char
		elif char == '\n':
			formattedString += ' '
	return formattedString

if __name__=='__main__':
	epub = epubutils.EpubFile('books/hp.epub')
	text = epub.giveTextList()[8][1]
	print(stripNonAlpha(text))
