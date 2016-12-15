import sys
import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn import cluster
import preprocess


#main program
data = []
classes = []
X = []
test_set = []

with open('../datasets/ShuffledRefinedDataset.csv', 'rb') as fp:
    dataset = csv.reader(fp)
    next(dataset, None)
    for complaint in dataset:
        data.append(complaint[5])
        classes.append(complaint[1])

test_set = data[:850]
test_class = classes[:850]
X = data[850:]
Y = classes[850:]

tfidf_vectorizer = TfidfVectorizer( max_df=0.7, min_df=.001,
                                    max_features=1200,
                                    stop_words='english')

train_matrix = tfidf_vectorizer.fit_transform(X)
test_matrix = tfidf_vectorizer.transform(test_set)

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=5)
neigh.fit(train_matrix, Y)

predicted_classes = neigh.predict(test_matrix)
# count = 0
# for prediction,real in zip(predicted_classes, test_class) :
# 	if prediction == real:
# 		count += 1

#print "\n Correct predictions : " + str(count)
print "kNN score : ",neigh.score(test_matrix, test_class)




#---------------BASICS------------------------------------------------------------------------------
#vectorizer = CountVectorizer(max_df=0.9, min_df=2, max_features=1000, stop_words='english')
#vectorizer.fit_transform(X[:99])    #train set
# print vectorizer.vocabulary_        u'identical': 475, u'know': 528, u'desk': 304, u'password': 644,
#                                     u'necessary': 606, u'like': 545, u'bulge': 158, u'payments': 648,
#                                     u'martin': 580, u'simply': 841, u'works': 989, u'rober': 767,
#                                     u'growth': 454, u'transport': 930, u'schedule': 793, u'wesley': 975,
#                                     u'loans': 556, u'actual': 87, u'extension': 388, u'getting': 442,

#freq_smatrix = vectorizer.transform(X[99:])  #test set
#print X[99:]
#print freq_smatrix
# ['I checked into exercising options with Smith Barney, but Enron has some kind of exclusive with
# Paine Weber.  I am starting to exercise now, but I am going to use the proceeds to buy another
# apartment complex.    What do you think about selling JDSU and buying SDLI? Also can you look at
# EOG as a play on rising oil and gas prices.Thanks,Phillip']

#(docNO, id_in_vocabulary)   freq   word(not in actual output!)
#   (0, 342)	1  Enron
#   (0, 435)	1  going
#   (0, 557)	1  look
#   (0, 635)	1  options
#   (0, 663)	1  Phillip
#   (0, 692)	1  prices
#   (0, 698)	1  proceeds
#   (0, 813)	1  selling
#   (0, 846)	1  Smith
#   (0, 873)	1  starting
#   (0, 902)	1  Thanks
#   (0, 909)	1  think
#   (0, 953)	1  use

#tfidf = TfidfTransformer(norm="l2")
#tfidf.fit_transform(freq_smatrix)
#print "tfidf: ", tfidf.idf_
# [ 1.69314718  1.69314718  1.69314718  1.          1.69314718  1.69314718
#   1.          1.69314718  1.69314718  1.          1.69314718  1.69314718
#   1.69314718  1.69314718  1.69314718  1.69314718  1.69314718  1.69314718
#   1.69314718  1.69314718  1.69314718  1.69314718  1.69314718....1.6914718 ]

#-----------------------------X---------------------------------------------------------------------
