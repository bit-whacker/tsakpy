#Import the necessary methods from tweepy library
import tweepy
import sys
import csv
import json
import nltk
import os
import os.path
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
	num_tweets = 0
	def __init__(self, api=None):
            super(StdOutListener, self).__init__()
            
            self.keyword = ''
            self.rateLimit = 0
			
	def on_status(self, status):
			targetFile = open(self.keyword+".txt", 'a')
			sentimentIntensityAnalyzerObject = SentimentIntensityAnalyzer()
			tweet = status.text.encode('utf-8')
			if status.lang == 'en':
				StdOutListener.num_tweets += 1
				if StdOutListener.num_tweets > self.rateLimit:				
					targetFile.close()
					StdOutListener.num_tweets = 0
					return False
			tweetPolarityScore = sentimentIntensityAnalyzerObject.polarity_scores(tweet)
			status._json['Sentiment'] = tweetPolarityScore
			targetFile.write(str(status._json))
			targetFile.write('\n')
			return True	
	
	def on_error(self, status):
			if status == 401:
				print "Enter Correct Twitter Application Credentials"
				sys.exit(0)
			elif str(status) == "Not authorized.":
				print 'We are having trouble connecting to Twitter. Check Credentials'
			elif str(status) == str([{u'message': u'Bad Authentication data.', u'code': 215}]):
				print "Enter the Correct Twitter Application Credentials"
			elif str(status) == str([{u'message': u'Rate limit exceeded', u'code': 88}]):
				time.sleep(60*5) #Sleep for 5 minutes
			else:
				print status


def downloadStreamingTweets(keyword, limit,consumer_key,consumer_secret,access_token,access_token_secret):
		listenerObject = StdOutListener()
		listenerObject.rateLimit  = int(limit)
		listenerObject.keyword = keyword
		auth = OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		stream = Stream(auth, listenerObject)
			#This line filter Twitter Streams to capture data by the keywords: 'keyword'
		
		stream.filter(track=[keyword])#Import the necessary methods from tweepy library