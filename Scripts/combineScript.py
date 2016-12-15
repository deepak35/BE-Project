""" This script combines all the refined dataset (c1.....c6) {rename the datasets as per repo names}
into a single csv (merged.csv)file"""
import nltk
from nltk.corpus import stopwords
import string
import csv
import re
import shuffleData

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



name = "c"
header = True

for i in range (1,7):
	fileName = "../datasets/" + name + str(i) + ".csv"
	#header = true
	with open(fileName, 'rb') as inp, open('../datasets/merged.csv', 'a') as out:
		complaintFile = csv.reader(inp)
		writer = csv.writer(out)
		if  not header:
			next(complaintFile, None)

		for row in complaintFile :
			#modify
			if row[1] != "Virtual currency" :
				if row[1] == "Credit card":
					row[2] = "Credit card"
			#RemoveX
			row[5] = re.sub('[X]+', '', row[5])
			row[5] = re.sub('[\*]+', '', row[5])
			row[5] = re.sub('[/]+', '', row[5])
			row[5] = preprocess.text_preprocessing(row[5])

			writer.writerow(row)
	header = False

shuffleData.shuffle()
