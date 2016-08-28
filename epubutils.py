#!/usr/local/Cellar/python3/3.5.2_1/bin/python3.5

from bs4 import BeautifulSoup as BS
from zipfile import ZipFile

class EpubFile:
	def __init__(self, fname):
		self.zipFile = ZipFile(fname, 'r')

		# TODO need to add in error handling
		
	def giveTextList(self):
		textFiles = [file for file in self.zipFile.namelist() if file.startswith('OEBPS/Text/')]

		textAndFileNames = []
		for textFile in textFiles:
			text = self.zipFile.read(textFile)
			textSoup = BS(text, 'html.parser')

			# get all the text from the '<p>' elements
			allText = ""
			for p in textSoup.findAll('p'):
				allText += p.text + '\n\n'

			textAndFileNames.append( (textFile, allText) )

		return textAndFileNames
