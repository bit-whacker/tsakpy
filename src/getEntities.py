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
from flask import json

def getEntity(parser,tweets,outputFile): 
	filteredTweets = []
	xEntities = {}
	targetFile = open(outputFile, 'a')
	for tweet in tweets:
		entity_Resultlist = []
		text = tweet.text
		replaced_input_sentence = re.sub("[^' 'a-zA-Z]", "",text)
		replaced_input = unicode(re.sub(r"http\S+", "", replaced_input_sentence))
		try:
			xEntities = getEntities(parser,replaced_input,xEntities)
			tweet._json['extracted_entities'] = xEntities#json.dumps(entity_Resultlist)
			targetFile.write(str(tweet._json))
			targetFile.write('\n')
			filteredTweets.append(tweet._json)
		except Exception as e:
			return e
	targetFile.close()	
	return filteredTweets
	
def getEntities(parser, tweet, xEntities):
	try:
		spacyParsedObject = parser(tweet)
		sentence =  TextBlob(tweet)
		textblobTaggedObject = sentence.parse().split()
		patterntaggedObject = tag(tweet, tokenize=True)
		for word in patterntaggedObject:
			word, wordtag=word
			if  wordtag == "NNP" or  wordtag == "NN" or  wordtag == "PRP":
				v = str(word)
				v = v.strip()
				if(v not in xEntities):	
					xEntities[v]=str(wordtag)						
		for taggedObject in textblobTaggedObject:
			for word in taggedObject:
				word, wordtag=word[0], word[1]
				if wordtag == "NNP" or wordtag == "NN" or wordtag == "PRP":
					v = str(word)
					v = v.strip()
					if(v not in xEntities):	
						xEntities[v]=str(wordtag)
		for word in spacyParsedObject:
			if word.tag_ == "NNP" or word.tag_ == "NN" or word.tag_ == "PRP":
				v = str(word)
				v = v.strip()
				if(v not in xEntities):	
					xEntities[v]=str(word.tag_)
		return xEntities
	except Exception as e:
		return e
		