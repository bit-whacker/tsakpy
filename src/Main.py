import entityMain
import sentimentMain
import os

def main():
	while True:
		line = raw_input("Enter 'sentiment' for sentiment Analysis &&  'entity' for Entity extraction:")
		if line == "exit":
			print "Good Bye"
			break
		elif line == "entity":
			entityMain.main()
		elif line == "sentiment":
			sentimentMain.main()
		else:
			print "Enter valid command"
			
main()