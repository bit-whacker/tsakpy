import sentimentFilteredTweets
import getEntities
import spacy
from spacy.en import English
import unittest
 

class TestUM(unittest.TestCase):
	
	parser = English()
	
	def setUp(self):
		pass
	
	def test_polarityscore(self):
		actual_value = sentimentFilteredTweets.getPolarityScores("RT @ANI_news: Terrorists attack police party at Zadibal police station in Srinagar. More details awaited")
		expected_value = {'neg': 0.385, 'neu': 0.494, 'pos': 0.121, 'compound': -0.7076}
		self.assertEqual(actual_value, expected_value )
	
	def test_polarityscore1(self):
		actual_value = sentimentFilteredTweets.getPolarityScores("Congrats #RCB :) #IPL2016 #RCBvsDD #ViratKholi https://t.co/Na7G9e7Uda")
		expected_value = {'neg': 0.0, 'neu': 0.439, 'pos': 0.561, 'compound': 0.7506}
		self.assertEqual(actual_value, expected_value )
	
	def test_polarityscore2(self):
		actual_value = sentimentFilteredTweets.getPolarityScores("Pakistan denounces US drone attack as violation of sovereignty https://t.co/nP6A41WYKN")
		expected_value = {'neg': 0.568, 'neu': 0.432, 'pos': 0.0, 'compound': -0.8481}
		self.assertEqual(actual_value, expected_value )
	
	def test_sentiment(self):
		polarityscore = {'neg': 0.522, 'neu': 0.437, 'pos': 0.041, 'compound': -0.9552}
		actual_value = sentimentFilteredTweets.getSentiment(polarityscore)
		expected_value = 'negative'
		self.assertEqual(actual_value, expected_value )
	
	def test_sentiment1(self):
		polarityscore = {'neg': 0.385, 'neu': 0.494, 'pos': 0.121, 'compound': -0.7076}
		actual_value = sentimentFilteredTweets.getSentiment(polarityscore)
		expected_value = 'neutral'
		self.assertEqual(actual_value, expected_value )
	
	def test_sentiment2(self):
		polarityscore = {'neg': 0.0, 'neu': 0.439, 'pos': 0.561, 'compound': 0.7506}
		actual_value = sentimentFilteredTweets.getSentiment(polarityscore)
		expected_value = 'positive'
		self.assertEqual(actual_value, expected_value )
	
	def test_sentiment3(self):
		polarityscore = {'neg': 0.568, 'neu': 0.432, 'pos': 0.0, 'compound': -0.8481}
		actual_value = sentimentFilteredTweets.getSentiment(polarityscore)
		expected_value = 'negative'
		self.assertEqual(actual_value, expected_value )
	
	
	def test_getEntities(self):
		tweet = unicode('I wanna be a professional killer Like John Wick yeah')
		xEntities = {}
		actual_value = getEntities.getEntities(TestUM.parser,tweet,xEntities)
		expected_value = {'I': 'PRP', 'Wick': 'NNP', 'John': 'NNP', 'killer': 'NN'}
		self.assertEqual(actual_value,expected_value)
		
	def test_getEntities1(self):
		tweet = unicode('James Bond is extraordinary character')
		xEntities = {}
		actual_value = getEntities.getEntities(TestUM.parser,tweet,xEntities)
		expected_value = {'James': 'NNP', 'character': 'NN', 'Bond': 'NNP'}
		self.assertEqual(actual_value,expected_value)
	
	def test_getEntities2(self):
		tweet = unicode('OpenMinted will create a readable summary of licenses and a harmonized vocabulary for text miners - Penny Labropoulou')
		xEntities = {}
		actual_value = getEntities.getEntities(TestUM.parser,tweet,xEntities)
		expected_value = {'OpenMinted': 'NNP', 'vocabulary': 'NN', 'text': 'NN', 'Penny': 'NNP', 'summary': 'NN', 'Labropoulou': 'NNP'}
		self.assertEqual(actual_value,expected_value)
		
if __name__ == '__main__':
	unittest.main()