import os
import os.path
import ConfigParser
import spacy
from spacy.en import English
import getEntities
import CommandDumpTweets
import CommandDumpStreamingTweets
import sentimentFilteredTweets

def executeCommand(command, keyword, type, sentiment,limit,consumer_key,consumer_secret,access_key,access_secret):
	tweets = []
	filteredTweets = [] 
	if command == 'dumpTweets':
		try:
			if type == '-sentiment':
				tweets = CommandDumpTweets.get_all_tweets(keyword,limit,consumer_key,consumer_secret,access_key,access_secret)
				filteredTweets = sentimentFilteredTweets.getFilteredTweets(tweets, sentiment,keyword)
			elif type == '-entity' :
				print "Loading parser"
				parser = English()
				print "Parser Loaded"
				tweets = CommandDumpTweets.get_all_tweets(keyword,limit,consumer_key,consumer_secret,access_key,access_secret)
				filteredTweets = getEntities.getEntity(parser,tweets,keyword)
				print len(tweets)
				print len(filteredTweets)
		except Exception as e:
			print e
	elif command == 'dumpStreaming':
		try:
			if type == '-sentiment': 
				tweets = CommandDumpStreamingTweets.downloadStreamingTweets(keyword,limit,consumer_key,consumer_secret,access_key,access_secret)
				filteredTweets = sentimentFilteredTweets.getFilteredTweets(tweets, sentiment,keyword)
			elif type == '-entity':
				print "Loading parser"
				parser = English()
				print "Parser Loaded"
				tweets = CommandDumpTweets.get_all_tweets(keyword,limit,consumer_key,consumer_secret,access_key,access_secret)
				filteredTweets = getEntities.getEntity(parser,tweets,keyword)
				print len(tweets)
				print len(filteredTweets)
		except Exception as e:
			if e.response:
				print 'error main'
				print (e.response.content)
	else:
		print "Enter Valid Command : dumpTweets or dumpStreaming Are valid Commands"
	
	
def main():	
	config = ConfigParser.RawConfigParser()
	config.readfp(open('ConfigFile.properties'))
	consumer_key = config.get('Credentials','consumer_key')
	consumer_secret = config.get('Credentials','consumer_secret')
	access_key = config.get('Credentials','access_key')
	access_secret = config.get('Credentials','access_secret')
	while True:
		line = raw_input("Enter Command :")
		args = []
		args = line.split(' ')
		if  args[0] == 'exit':
			print 'Good Bye'
			break
		elif len(args) < 7:
			executeCommand(args[0], args[2], args[3], "No value", int(args[5]),str(consumer_key),str(consumer_secret),str(access_key),str(access_secret))
			print args
		else:
			print args
			executeCommand(args[0], args[2], args[3], args[4], int(args[6]),str(consumer_key),str(consumer_secret),str(access_key),str(access_secret))

			
			
main()