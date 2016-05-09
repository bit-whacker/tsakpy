# tsakpy
Text Processing Tool

# Installation
Prerequisites <br/>
 1. Install Python 2.7.11 with pip<br/>
 You  can download and install Python 2.7.11 from [here] (https://www.python.org/downloads/) <br>

2. NLTK Installation <br>
   * **For Windows**<br>
   Open commandline and run following command. <br>
      `pip install nltk` <br>
   run the following command to download necessary Corpora. <br>
      `python -m nltk.downloader all` <br>

  * **For Mac or Unix**<br>
   To install NLTK you can consult [Installing NLTK](http://www.nltk.org/install.html). <br>
   and for downloading necessary Corpora you can consult [Installing NLTK Data](http://www.nltk.org/data.html) <br>

3. Install `spacy`<br>
  run the following command to install `spacy`<br>
  `pip install spacy`<br>

**Note**:  in windows environment if you face an issue like missing `vcvarsall.bat` during spacy installation then first download `vc_for_python` from `http://aka.ms/vcpython27` install it and set environment variable for `AppData\Local\Programs\Common\Microsoft\Visual C++ for Python\9.0` and `AppData\Local\Programs\Common\Microsoft\Visual C++ for Python\9.0\VC\bin` and then retry to install spacy as above.


####Setup

* create twitter app [prerequisites](https://github.com/project-spinoza/twitter-swiss-army-knife/wiki/Prerequisites)<br>
* edit `ConfigFile.properties` file and enter your keys e.g. <br><br>
`accessToken=[enter your access token here]`<br>
`consumerSecret=[enter your consumer secret key here]`<br>
`consumerKey=[enter your consumer key here]`<br>
`accessSecret=[enter your accessSecret key here]`<br><br>
* Run `Installation.bat`. It will download some necessary dependencies

# Running the Application <br/>
### Running at the command line
<p>Open cmd and run the following command</p>
`python Main.py`

### Available Commands <br/>
  **For running Twitter Sentiment Analysis run one of the following commands.** <br> 
  * `dumpTweets -keyword <any keyword> -sentiment <positive|negative|neutral> -limit <integer>` <br/>
  * `dumpStreaming -keyword <any keyword> -sentiment <positive|negative|neutral> -limit <integer>` <br>
  e.g. `dumpTweets -keyword iphone -sentiment positive -limit 5` <br/><br>
  
  **For Entity Extraction from a Given Sentence run one of the following command.**<br>
  * `dumpTweets -keyword <any keyword> -entity -limit <integer>` <br/>
  * `dumpStreaming -keyword <any keyword> -entity -limit <integer>` <br>
  e.g. `dumpStreaming -keyword ipad -entity -limit 4`
  

