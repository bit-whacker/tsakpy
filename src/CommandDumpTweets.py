import tweepy 
import csv
import time
import sys
import json



def get_all_tweets(keyword, limit, consumer_key, consumer_secret, access_key, access_secret):
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	tweets_Collection = []
	allTweets = []
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
	return tweets_Collection