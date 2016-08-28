#!/usr/local/Cellar/python3/3.5.2_1/bin/python3.5

from bs4 import BeautifulSoup as BS
from zipfile import ZipFile

class EpubFile:
	def __init__(self, fname):
		zipFile = ZipFile(fname, 'r')