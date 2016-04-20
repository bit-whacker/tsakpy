import os
import ConfigParser
import CommandDumpTweets
import CommandDumpStreamingTweets
def executeCommand(command, keyword, limit,consumer_key,consumer_secret,access_key,access_secret):
	if command == 'dumpTweets':
		try:
			CommandDumpTweets.downloadTweets(keyword,limit,consumer_key,consumer_secret,access_key,access_secret)
		except Exception as e:
			if e.response:
				print 'error main'
				print (e.response.content)
	elif command == 'dumpStreaming':
		try:
			CommandDumpStreamingTweets.downloadStreamingTweets(keyword,limit,consumer_key,consumer_secret,access_key,access_secret)
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
		elif len(args) < 3:
			print "Enter the required 3 Arguments in Command : "
			continue
		
		else:
			print args
			executeCommand(args[0], args[1], int(args[2]),str(consumer_key),str(consumer_secret),str(access_key),str(access_secret))
