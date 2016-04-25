from __future__ import unicode_literals
import spacy
from spacy.en import English 
from pattern.en import tag
from textblob import TextBlob
import sys
import re 
import json
import os
import os.path

def getEntity(parser,tweets,keyword): 
	filteredTweets = []
	#filepath = os.path.join('C:/Python27/PythonPrograms/TSAK/',keyword+".txt")
	targetFile = open(keyword+".txt", 'a')
	for tweet in tweets:
		entity_Resultlist = []
		text = tweet.text
		replaced_input_sentence = re.sub("[^' 'a-zA-Z]", "",text)
		replaced_input = unicode(re.sub(r"http\S+", "", replaced_input_sentence))
		try:
			spacyParsedObject = parser(replaced_input)
			sentence =  TextBlob(replaced_input)
			textblobTaggedObject = sentence.parse().split()
			patterntaggedObject = tag(replaced_input, tokenize=True)
			for word in patterntaggedObject:
				word, wordtag=word
				if  wordtag == "NNP" or  wordtag == "NN" or  wordtag == "PRP":
					if unicode(word) not in entity_Resultlist:
						entity_Resultlist.append(str(word))
						entity_Resultlist.append(str( wordtag))
						
			for taggedObject in textblobTaggedObject:
				for word in taggedObject:
					word, wordtag=word[0], word[1]
					if wordtag == "NNP" or wordtag == "NN" or wordtag == "PRP":
						if unicode(word) not in entity_Resultlist:
							entity_Resultlist.append(str(word))
							entity_Resultlist.append(str(wordtag))
			for word in spacyParsedObject:
				if word.tag_ == "NNP" or word.tag_ == "NN" or word.tag_ == "PRP":
					if unicode(str(word).rstrip()) not in entity_Resultlist:
						entity_Resultlist.append(str(word))
						entity_Resultlist.append(str(word.tag_))
			tweet._json['extracted_entities'] = entity_Resultlist
			targetFile.write(str(tweet._json))
			targetFile.write('\n')
			filteredTweets.append(tweet._json)
		except Exception as e:
			print replaced_input
			print e
	targetFile.close()	
	return filteredTweets