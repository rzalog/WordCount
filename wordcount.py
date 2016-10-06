#!/usr/local/Cellar/python3/3.5.2_1/bin/python3.5

# The actual command line tool to be run

import epubutils
from wordcountutils import *
import argparse

def countAllWords(fnames):
        total = 0
        for fname in fnames:
                try:
                        total += countTotalEpubWords(fname)
                except FileNotFoundError:
                        print("The file {} could not be found".format(fname))
        return total

def output(fnames, verboseLevel):
        total = countAllWords(fnames)
        if verboseLevel == 0:
                print(total)
        if verboseLevel > 0:
                for fname in fnames:
                        print("{}: {} words".format(fname, countTotalEpubWords(fname)))
                print("Total: {} words".format(total))
                
                        
parser = argparse.ArgumentParser("Count the number of words in a .EPUB file.")

parser.add_argument("fnames", nargs='+', help=".EPUB file(s)")
parser.add_argument("-v", "--verbose", action="count", default=0, help="identify level of verboseness")

args = parser.parse_args()

output(args.fnames, args.verbose)
