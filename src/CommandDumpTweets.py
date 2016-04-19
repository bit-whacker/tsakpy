import tweepy 
import csv
import time
import sys
import json
import nltk
import os
import os.path
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def get_all_tweets(keyword, limit, consumer_key, consumer_secret, access_key, access_secret):
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	
	#initialize a list to hold all the tweepy Tweets	
	sentimentIntensityAnalyzerObject = SentimentIntensityAnalyzer()
	
	#filepath = os.path.join('C:/Python27/PythonPrograms/get_tweets/',keyword+".txt")
	targetFile = open(keyword+".txt", 'a')			#File Opened in Append Mode
	tweets_Collection = []
	try:
		tweets_Collection = api.search(q = keyword, count=limit, lang= 'en')
		while len(tweets_Collection) < limit:
			if len(tweets_Collection) == limit:
				break
			else:
				allTweets = []
				allTweets = api.search(q = keyword, count=100, lang= 'en')
				tweets_Collection.extend(allTweets)
	except tweepy.TweepError, e:
		if str(e) == str([{u'message': u'Rate limit exceeded', u'code': 88}]):
			time.sleep(60*5) #Sleep for 5 minutes
		elif str(e) == str([{u'message': u'Bad Authentication data.', u'code': 215}]):
			print "Enter the Correct Twitter Application Credentials"
		elif str(e) == "Not authorized.":
			print 'We are having trouble connecting to Twitter. Check Credentials'
		else:
			print e
	for tweet in tweets_Collection: 
		tweetText = tweet.text.encode('utf-8')
		tweetPolarityScore = sentimentIntensityAnalyzerObject.polarity_scores(tweetText)
		tweet._json['Sentiment'] = tweetPolarityScore	
		targetFile.write(str(tweet._json))
		targetFile.write('\n')
	targetFile.close()	


def downloadTweets(keyword,limit,consumer_key,consumer_secret,access_key,access_secret):
	get_all_tweets(keyword, int(limit), consumer_key, consumer_secret, access_key, access_secret)