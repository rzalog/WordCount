#!/usr/local/Cellar/python3/3.5.2_1/bin/python3.5

import epubutils

if __name__=='__main__':
	epub = epubutils.EpubFile('books/hp.epub')
	print(epub.giveTextList()[9][1])
