import requests
from bs4 import BeautifulSoup
import random

def scrapWikiArticle(url):
    response = requests.get(url)
    
    soup = BeautifulSoup(response.content,'html.parser')
    title = soup.find(id='firstHeading')
    print(title.text)


search_articles = ['light', 'astronomy', 'fossils',
                   'android', 'plants', 'animals', 'ocean', 'oxygen']
for keyword in search_articles:
    
    scrapWikiArticle('https://en.wikipedia.org/wiki/'+keyword)