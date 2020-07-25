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


def getstemmeddocument(inputfile,outputfile):

    out = open(outputfile,'w',encoding='utf8')

    with open(inputfile,encoding='utf8') as f:
        reviews = f.readlines()
        
    for review in reviews:
        cleanedreview = stemmedreview(review)
        print((cleanedreview),file=out)

    out.close()


#Read commmand line arguements

inputfile  = sys.argv[1]
outputfile = sys.argv[2]

getstemmeddocument(inputfile,outputfile)