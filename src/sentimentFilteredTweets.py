import csv
import json
import nltk
import os
import os.path
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def getFilteredTweets(tweets_collection, sentiment,outputFile):
	filteredTweets = []	
	targetFile = open(outputFile, 'a')
	for tweet in tweets_collection:
		text = tweet.text.encode('utf-8')
		polarity_scores = getPolarityScores(text)
		ret_sentiment = getSentiment(polarity_scores)
		if(ret_sentiment == sentiment):
			tweet._json['Sentiment'] = ret_sentiment
			targetFile.write(str(tweet._json))
			targetFile.write("\n")
			filteredTweets.append(tweet._json)
	targetFile.close()
	return filteredTweets

def getPolarityScores(text):
	sentimentIntensityAnalyzerObject = SentimentIntensityAnalyzer()
	polarity_score = sentimentIntensityAnalyzerObject.polarity_scores(text)
	return polarity_score

def	getSentiment(polarity_score):
	max_value = max(polarity_score['pos'], polarity_score['neg'], polarity_score['neu'])
	sentiment = ""
	
	if(polarity_score['pos'] == max_value):
		sentiment = "positive"
	elif(polarity_score['neg'] == max_value):
		sentiment = "negative"
	elif(polarity_score['neu'] == max_value):
		sentiment = "neutral"
	
	return sentiment;
		
