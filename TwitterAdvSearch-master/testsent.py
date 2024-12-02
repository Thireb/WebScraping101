import nltk
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer
import json

with open('test.json', 'r') as lo:
    dat = json.load(lo)

may = list()

may.append(dat['content'])

for ob in may:
    scr = SentimentIntensityAnalyzer().polarity_scores(str(ob))
    print(scr)
