import spacy
from spacy.en import English 
from pattern.en import tag
from textblob import TextBlob

def getEntity(parser,input_sentence): 
	entity_Resultlist = [] 
	sentence = unicode(input_sentence)
	spacyParsedObject = parser(sentence)
	sentence =  TextBlob(sentence)
	textblobTaggedObject = sentence.parse().split()
	patterntaggedObject = tag(input_sentence, tokenize=True, encoding='utf-8')
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
	return entity_Resultlist