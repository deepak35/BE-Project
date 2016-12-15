"""Naive Bayes Classifier using python libraries"""


import sys
import csv
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn import metrics
import numpy as np
import preprocess


test = []
actual = []
X = []
Y = []
with open ('../datasets/ShuffledRefinedDataset.csv', 'rb') as fp:
	dataset = csv.reader(fp)
	next(dataset,None)
	i = 0
	for row in dataset:
		if i<1000:
			test.append(row[5])
			actual.append(row[1])

		else:
			X.append(row[5])
			Y.append(row[1])

		i += 1


count_vect = CountVectorizer(max_df=0.7, min_df=0.001, max_features=1200, stop_words='english')
XTrainCounts = count_vect.fit_transform(X)
#
# #tf_transformer = TfidfTransformer(use_idf=False).fit(XTrainCounts)
# #XTrainTf = tf_transformer.transform(XTrainCounts)
#
tfidf_transformer = TfidfTransformer()
XTrainTfidf = tfidf_transformer.fit_transform(XTrainCounts)
#
# # Multinomial Naive Bayes Classifier
clf = MultinomialNB().fit(XTrainTfidf,Y)
#
testCounts = count_vect.transform(test)
testTfidf = tfidf_transformer.transform(testCounts)
#
predicted = clf.predict(testTfidf)
# #print "Naive Bayes score : ",clf.score(testTfidf,actual)
#
# count = 0
# for prediction,real in zip(predicted,actual) :
# 	if prediction == real:
# 		count += 1
# 	print prediction + "		" + real
# #
# print "\n Correct predictions : " + str(count)
print "Naive Bayes score : ",clf.score(testTfidf,actual)
#accuracy = count / len(test)
#print "\n accuracy : " + str(accuracy)
#accuracy = np.mean(predicted == Y)
#print "\n Naive Bayes accuracy : " + str(np.mean(predicted == Y))

#print (metrics.classification_report(actual, predicted, target_names = actual))
