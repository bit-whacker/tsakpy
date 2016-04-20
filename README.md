# tsakpy
Text Processing Tool

# Installation
Prerequisites <br/>
 1. Python 2.7.11 <br/>
 You  can download Python 2.7.11 from [here] (https://www.python.org/downloads/) <br>


# Adding Dependencies <br>
1. pip Installation
   You can get `get-pip.py` [here] (https://bootstrap.pypa.io/get-pip.py).<br>
   Open `C:\Python27` directory and paste `get-pip.py` file here. <br>
   To install pip Open cmd and run following Command. <br>
     `python get-pip.py` <br>

2. NLTK Installation <br>
   For Windows <br>
   To install NLTK Open cmd and run following command. <br>
      `pip install nltk` <br>
   and then open python shell IDLE and run the following command to download necessary Corpora. <br>
      `python -m nltk.downloader all` <br>
   For Mac or Unix <br>
   To install NLTK you can consult [Installing NLTK](http://www.nltk.org/install.html). <br>
   and for downloading necessary Corpora you can consult [Installing NLTK Data](http://www.nltk.org/data.html) <br>


####Setup

* create twitter app [prerequisites](https://github.com/project-spinoza/twitter-swiss-army-knife/wiki/Prerequisites)<br>
* edit `ConfigFile.properties` file and enter your keys e.g. <br><br>
`accessToken=[enter your access token here]`<br>
`consumerSecret=[enter your consumer secret key here]`<br>
`consumerKey=[enter your consumer key here]`<br>
`accessSecret=[enter your accessSecret key here]`<br><br>
* Run 'Installation.bat'. It will download some necessary dependencies

# Running the Application <br/>
### Running at the command line
<p>Open cmd and run the following command</p>
`python Main.py`

### Available Commands <br/>
   For running Twitter Sentiment Analysis Enter `sentiment` and then one of the following commands. <br> 
  `dumpTweets keyword limit` <br/>
  `dumpStreamingTweets keyword limit` <br>
  
  For Entity Extraction from a Given Sentence enter `entity` and then provide the Sentence.

