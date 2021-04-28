from urllib import request
from bs4 import BeautifulSoup
import nltk, re, pprint
from nltk import word_tokenize
url = "https://en.wikipedia.org/wiki/Lionel_Messi"
html = request.urlopen(url).read().decode('utf8')
raw = BeautifulSoup(html, 'html.parser').get_text()
tokens = word_tokenize(raw)
text = nltk.Text(tokens)
text.concordance('Barcelona')