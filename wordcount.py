#!/usr/local/Cellar/python3/3.5.2_1/bin/python3.5

import epubutils
import sys

def countTotalEpubWords(fname):
	epub = epubutils.EpubFile(fname)
	totalWords = 0
	for text in epub.giveTextList():
		totalWords += countWords(text[1])
	return totalWords

def countWords(string):
	return len(string.split(' '))

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
	try:
		fname = sys.argv[1]
		wordCount = countTotalEpubWords(fname)
	except IndexError:
		print("Please provide a .epub filename.")
		quit()
	except:
		print("Something went wrong with opening your file.")
		quit()

	print("File name: " + fname)
	print("Total words: %d" % wordCount)

