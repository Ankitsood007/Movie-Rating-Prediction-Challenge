from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import sys

tokenizer = RegexpTokenizer(r'\w+')
englishstopwords = set(stopwords.words('english'))
ps = PorterStemmer()

def stemmedreview(review):
    review = review.lower()
    review = review.replace("<br /><br />"," ")
    #tokenization
    tokens = tokenizer.tokenize(review)
    #Removing Stopwords
    filteredtokens = [token for token in tokens if token not in englishstopwords]
    #stemmed tokens
    stemmedtokens = [ps.stem(token) for token in filteredtokens]
    cleanedreview = ' '.join(stemmedtokens)
    return cleanedreview 