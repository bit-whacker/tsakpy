import tweepy 
import csv
import time
import sys
import json
import nltk
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
	targetFile = open('%s_tweets.txt' % keyword, 'a')			#File Opened in Append Mode
	tweets_Collection = []
	try:
		tweets_Collection = api.search(q = keyword, count=limit)
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
		if tweet.lang == 'en':
			tweetPolarityScore = sentimentIntensityAnalyzerObject.polarity_scores(tweetText)
			tweet._json['Sentiment'] = tweetPolarityScore
			
			targetFile.write(str(tweet._json))
			targetFile.write('\n')
	targetFile.close()	


def downloadTweets(keyword,limit,consumer_key,consumer_secret,access_key,access_secret):
	get_all_tweets(keyword, int(limit), consumer_key, consumer_secret, access_key, access_secret)