import os
import setup
import CommandDumpTweets
import CommandDumpStreamingTweets
def executeCommand(command, keyword, limit,consumer_key,consumer_secret,access_key,access_secret):
	if command == 'dumpTweets':
		CommandDumpTweets.downloadTweets(keyword,limit,consumer_key,consumer_secret,access_key,access_secret)
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
	consumer_key = setup.consumer_key
	consumer_secret = setup.consumer_secret
	access_key = setup.access_key
	access_secret = setup.access_secret
	while True:
		line = raw_input("Enter Command > ")
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
			executeCommand(args[0], args[1], int(args[2]),consumer_key,consumer_secret,access_key,access_secret)
main()	