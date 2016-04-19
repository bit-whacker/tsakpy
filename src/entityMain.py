from __future__ import unicode_literals
import showEntities
import spacy
import showEntities
import csv
from spacy.en import English # download english model first
import os
import sys
import re 

class displayEntities():
	
	def _init_(self):
		print("Loading Parser")
		parser = English()
		print("Parser Loaded")
		getEntities(parser)
	
def getEntities(parser):
	resultlist = []
	while True:
		input_senetence = raw_input("Enter Sentence :")
		replaced_input_sentence = re.sub("[^' 'a-zA-Z0-9]", "", input_senetence)
		sentence = unicode(replaced_input_sentence)
		if input_senetence == "exit":
			print "Good Bye"
			break
		
		print showEntities.getEntity(parser,sentence) 
		
			
def main():
	entityObject = displayEntities()
	entityObject._init_()
