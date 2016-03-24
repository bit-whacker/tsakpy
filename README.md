# tsakpy
Sentiment Analysis Tool

# Installation
Prerequisites <br/>
 1. Python 2.7.11 <br/>
 You  can download Python 2.7.11 from [here] (https://www.python.org/downloads/) <br>


# Adding Dependencies <br>
1. Tweepy Installation <br>
   To insatll it from github, You need to clone the tweepy project to directory whose path doesn't contain blank spaces<br> 
       `git clone git://github.com/joshthecoder/tweepy.git` <br>
     Now you can run following cammands on git. <br>
      `cd tweepy` <br>
      `python setup.py install` <br>
2. NLTK Installation <br>
   For Windows
   To install NLTK Open cmd and run following command. <br>
      `pip install nltk` <br>
   and then open python shell IDLE and run the following command to download necessary Corpora. <br>
      `import nltk` <br>
      `nltk.download()` <br>


####Setup

* create twitter app [prerequisites](https://github.com/project-spinoza/twitter-swiss-army-knife/wiki/Prerequisites)<br>
* edit `ConfigFile.properties` file and enter your keys e.g. <br><br>
`accessToken=[enter your access token here]`<br>
`consumerSecret=[enter your consumer secret key here]`<br>
`consumerKey=[enter your consumer key here]`<br>
`accessSecret=[enter your accessSecret key here]`<br><br>


# Running the Application <br/>
### Running at the command line
<p>Open cmd and run the following command</p>
`python Main.py`

### Available Commands <br/>
`dumpTweets keyword limit` <br/>
`dumpStreamingTweets keyword limit` 

