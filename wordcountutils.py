#!/usr/local/Cellar/python3/3.5.2_1/bin/python3.5

import epubutils
import argparse

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
		if char.isalnum() or char in otherValidChars:
			formattedString += char
		elif char == '\n':
			formattedString += ' '
	return formattedString

if __name__=='__main__':
        print("The tools in this file are intended to be run with\
\"wordcount.py\". Try running that instead!")
        

