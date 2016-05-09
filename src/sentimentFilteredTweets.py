import csv
import json
import nltk
import os
import os.path
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def getFilteredTweets(tweets_collection, sentiment,keyword):
	filteredTweets = []	
	#filepath = os.path.join('C:/Python27/PythonPrograms/TSAK/',keyword+".txt")
	targetFile = open(keyword+".txt", 'a')
	sentimentIntensityAnalyzerObject = SentimentIntensityAnalyzer()
	for tweet in tweets_collection:
		print tweet.text
		tweetPolarityScore = sentimentIntensityAnalyzerObject.polarity_scores(tweet.text.encode('utf8'))
		print tweetPolarityScore
		if sentiment == "negative":
			if tweetPolarityScore['neg'] > tweetPolarityScore['pos'] and tweetPolarityScore['neg'] > tweetPolarityScore['neu']:
				tweet._json['sentiment'] = tweetPolarityScore
				targetFile.write(str(tweet._json))
				targetFile.write('\n')
				filteredTweets.append(tweet)
		elif sentiment == "positive":
			if tweetPolarityScore['pos'] > tweetPolarityScore['neg'] and tweetPolarityScore['pos'] > tweetPolarityScore['neu']:
				tweet._json['sentiment'] = tweetPolarityScore
				targetFile.write(str(tweet._json))
				targetFile.write('\n')
				filteredTweets.append(tweet)
		elif sentiment == "neutral":
			if tweetPolarityScore['neu'] > tweetPolarityScore['pos'] and tweetPolarityScore['neu'] > tweetPolarityScore['neg']:
				tweet._json['sentiment'] = tweetPolarityScore
				targetFile.write(str(tweet._json))
				targetFile.write('\n')
				filteredTweets.append(tweet)
		else:
			print "adding tweetPolarityScore to tweet"
			tweet._json['Sentiment'] = tweetPolarityScore
			filteredTweets.append(tweet._json)
	return filteredTweets