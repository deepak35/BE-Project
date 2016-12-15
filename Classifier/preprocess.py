import nltk
from nltk.corpus import stopwords
import string
import csv

#r = "It's a nice day. Let's play football today!. How are you?"
def text_preprocessing(r):
		#remove puctuation
		table = string.maketrans("", "")
		row = r.translate(table, string.punctuation)
		#Its a nice day Lets play football today How are you

		#tokenize each word
		row_words = nltk.word_tokenize(row)
		#['Its', 'a', 'nice', 'day', 'Lets', 'play', 'football', 'today', 'How', 'are', 'you']
		i = 0

		#normalize each word (convert to lower case)
		for token in row_words:
			row_words[i] = token.lower()
			i += 1

		#Remove stopwords
		row_refined = [token for token in row_words if (not token in stopwords.words('english'))]
		#['nice', 'day', 'lets', 'play', 'football', 'today']

		#Stemming
		porter = nltk.PorterStemmer()
		i = 0

		for token in row_refined:
			row_refined[i] = porter.stem(token.decode('utf-8'))
			i += 1
		#[u'nice', u'day', u'let', u'play', u'footbal', u'today']

		#Lemmatization
		lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()
		i = 0
		for token in row_refined:
			row_refined[i] = lemmatizer.lemmatize(token)
			i += 1

		r = ""
		for token in row_refined:
			r = r + token + " "
		r = r.strip(" ")

		return r.encode('utf-8')
		#return row_refined
		#[u'nice', u'day', u'let', u'play', u'footbal', u'today']
