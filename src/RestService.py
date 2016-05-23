import os
from flask import Flask,render_template, request
from flask import json
import os.path
import spacy
from spacy.en import English
import getEntities
import CommandDumpTweets
import CommandDumpStreamingTweets
import sentimentFilteredTweets


app = Flask(__name__,static_url_path='/static')

@app.route('/')
def hello():
    return 'Welcome to Python Flask!'

@app.route('/signUp',methods=['GET','POST'])
def signUp():
    return render_template('index.html')

def executeCommand(command, keyword, type, sentiment,limit,outputFile,consumer_key,consumer_secret,access_key,access_secret):
	tweets = []
	filteredTweets = [] 
	print type
	try:
		if type == '-sentiment':
			tweets = CommandDumpTweets.get_all_tweets(keyword,limit,consumer_key,consumer_secret,access_key,access_secret)
			filteredTweets = sentimentFilteredTweets.getFilteredTweets(tweets, sentiment,outputFile)
			return filteredTweets
		elif type == '-entity' :
			print "Loading parser"
			parser = English()
			print "Parser Loaded"
			tweets = CommandDumpTweets.get_all_tweets(keyword,limit,consumer_key,consumer_secret,access_key,access_secret)
			filteredTweets = getEntities.getEntity(parser,tweets,outputFile)
			return filteredTweets
	except Exception as e:
		return e
 
	
	
@app.route('/jsonData',methods=['POST'])	
def jsonData():
	try :
		data = request.get_json(force=True)
		command = data["command"]
		if command == "dumpTweets":
			keywords = data["values"][0]["-keywords"]
			limit = data["values"][1]["-limit"]
			outputFile = data["values"][2]["-o"]
			access_secret = data["credentials"]["-accessSecret"]
			consumer_secret = data["credentials"]["-consumerSecret"]
			access_token = data["credentials"]["-accessToken"]
			consumer_key = data["credentials"]["-consumerKey"]
			sentiment = data["action"]["-sentiment"]
			entity = data["action"]["-entity"]
		
			if sentiment == "null":
				action = "-entity"
				sentiment = "No value"
				responseData = json.dumps(executeCommand(command,keywords,action,sentiment,int(limit),outputFile,str(consumer_key),str(consumer_secret),str(access_token),str(access_secret)))
			else:
				action = "-sentiment"
				responseData = executeCommand(command,keywords,action,sentiment,int(limit),outputFile,str(consumer_key),str(consumer_secret),str(access_token),str(access_secret))
			response = [{'error': 'null', 'responseData':responseData }]
			return json.dumps(response)
		else:
			response =[{'error':'invalid_command','responseData':'null'}]
			return json.dumps(response)
	except Exception as e:
		response = [{'error':e.message, 'responseData':'null'}]
		return json.dumps(response)

if __name__=="__main__":
    app.run()