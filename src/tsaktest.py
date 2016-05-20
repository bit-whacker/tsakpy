import sentimentFilteredTweets
import getEntities
import spacy
from spacy.en import English
import unittest
 

class TestUM(unittest.TestCase):
 
	def setUp(self):
		pass
	
	def test_polarityscore(self):
		actual_value = sentimentFilteredTweets.getPolarityScores("I want to be a terrorist")
		expected_value = {'neg': 0.522, 'neu': 0.437, 'pos': 0.041, 'compound': -0.9552}
		self.assertEqual(actual_value, expected_value )
	
	def test_sentiment(self):
		polarityscore = {'neg': 0.522, 'neu': 0.437, 'pos': 0.041, 'compound': -0.9552}
		actual_value = sentimentFilteredTweets.getSentiment(polarityscore)
		expected_value = 'negative'
		self.assertEqual(actual_value, expected_value )
	
	def test_getEntities(self):
		parser = English()
		tweet = unicode('I wanna be a professional killerLike John Wick yeah')
		xEntities = {}
		actual_value = getEntities.getEntities(parser,tweet,xEntities)
		expected_value = {'I': 'PRP', 'Wick': 'NNP', 'John': 'NNP', 'killerLike': 'NN'}
		self.assertEqual(actual_value,expected_value)

if __name__ == '__main__':
	unittest.main()