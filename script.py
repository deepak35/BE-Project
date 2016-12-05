import sys
import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn import cluster


# for csv file
maxInt = sys.maxsize
decrement = True

while decrement:
    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True



#main program
train_set = []
with open('Bank_Complaints.csv') as fp:  #emails.csv = "file, message"
    dataset = csv.reader(fp)
    next(dataset, None)
    no_of_complaints = 100
    for complaint in dataset:
        msg = complaint[5];
        if msg:
            train_set.append(msg) #only msg
            no_of_complaints -= 1
        if no_of_complaints == 0:
            break


vectorizer = CountVectorizer(max_df=0.9, min_df=2, max_features=1000, stop_words='english')
# print vectorizer        CountVectorizer(analyzer=u'word', binary=False, decode_error=u'strict',
#                                 dtype=<type 'numpy.int64'>, encoding=u'utf-8', input=u'content',
#                                 lowercase=True, max_df=0.9, max_features=1000, min_df=2,
#                                 ngram_range=(1, 1), preprocessor=None, stop_words='english',
#                                 strip_accents=None, token_pattern=u'(?u)\\b\\w\\w+\\b',
#                                 tokenizer=None, vocabulary=None)

vectorizer.fit_transform(train_set[:99])    #train set
# print vectorizer.vocabulary_        u'identical': 475, u'know': 528, u'desk': 304, u'password': 644,
#                                     u'necessary': 606, u'like': 545, u'bulge': 158, u'payments': 648,
#                                     u'martin': 580, u'simply': 841, u'works': 989, u'rober': 767,
#                                     u'growth': 454, u'transport': 930, u'schedule': 793, u'wesley': 975,
#                                     u'loans': 556, u'actual': 87, u'extension': 388, u'getting': 442,

#print sorted(vectorizer.vocabulary_.items(), key=operator.itemgetter(1), reverse=True)
#print vectorizer.stop_words_       english

freq_smatrix = vectorizer.transform(train_set[99:])  #test set
#print "smatrix: ",freq_smatrix.todense()   [0,0,1,.....0]

#print train_set[99:]
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



#----------------Cosine Similarity----------------------------------------------

tfidf_vectorizer = TfidfVectorizer( max_df=0.9, min_df=2,
                                    max_features=1000,
                                    stop_words='english')

tfidf_matrix = tfidf_vectorizer.fit_transform(train_set[:99])
test_matrix = tfidf_vectorizer.transform(train_set[99:])
print "tfidf matrix shape: ", tfidf_matrix.shape
#(99, 1000)

cosine_values = cosine_similarity(test_matrix, tfidf_matrix)[0]
sorted_cosine_values = sorted(cosine_values)
print "cosine value: ",cosine_values
doc_id = cosine_values.tolist().index(sorted_cosine_values[-2])
print "\nTest doc:\n", train_set[99]
print "\nSimilar to doc\n", train_set[doc_id]

# [[ 0.          0.06777551  0.          0.00955164  0.          0.0170681
#    0.06168781  0.          0.05888325  0.08582036  0.0795455   0.00571346
#    0.07460965  0.07461934  0.01307257  0.          0.06504668  0.00938275
#    0.04856477  0.10158654  0.06350377  0.12199382  0.05452238  0.08776695
#    0.08523893  0.01912055  0.01910773  0.03791309  0.00581639  0.
#    0.04082069  0.01696288  0.05462218  0.          0.03254754  0.04028783
#    0.          0.0591564   0.00891618  0.11077086  0.01074648  0.03857858
#    0.0989654   0.02110569  0.00739382  0.          0.00660737  0.00323169
#    0.06753724  0.03972464  0.01680379  0.0385866   0.0948414   0.03624872
#    0.          0.04614057  0.06183129  0.03853563  0.01496242  0.03988652
#    0.03979173  0.11890341  0.          0.04686636  0.01108952  0.
#    0.08535662  0.01808327  0.03099382  0.03150305  0.01111546  0.07794462
#    0.11774116  0.          0.01846354  0.15282673  0.          0.0094232
#    0.03410244  0.01995636  0.00332809  0.03289144  0.04201339  0.01169623
#    0.          0.01168744  0.0044024   0.02800818  0.07317579  0.          0.
#    0.00814198  0.          0.03109231  0.09116843  0.2764018   0.08513576
#    0.01608237  0.0483515   1.        ]]

# Test doc:
# I checked into exercising options with Smith Barney, but Enron has some kind of
# exclusive with Paine Weber.  I am starting to exercise now, but I am going to use
# the proceeds to buy another apartment complex.    What do you think about selling
# JDSU and buying SDLI? Also can you look at EOG as a play on rising oil and gas prices.
# Thanks,Phillip
#
# Similar to doc
# Mac, Thanks for the research report on EOG.  Here are my observations:
# Gas Sales 916,000/day x 365 days = 334,340,000/year
# Estimated Gas Prices $985,721,000/334,340,000= $2.95/mcf  Actual gas prices are
# around $1.00/mcf higher and rising.    Recalc of EPS with more accurate gas
# prices:  (334,340,000 mct X $1/mcf)/116,897,000 shares outst = $2.86 additional
# EPS X 12 P/E multiple = $34 a share That is just a back of the envelope valuation
# based on gas prices.  I think crude price are undervalued by the tune of $10/share.
# Current price 37 Nat. Gas 34 Crude  10 Total  81  Can you take a look at these numbers
# and play devil's advocate?  To me this looks like the best stock to own Also can you
# send me a report on Calpine, Tosco, and SLB?Thank you, Phillip

kmeans = cluster.KMeans(max_iter=100)
kmeans.fit(tfidf_matrix)
labels = kmeans.labels_
print "labels: ", labels
# [2 2 5 6 2 7 1 2 7 3 1 1 4 4 6 0 4 2 0 1 5 3 5 3 3 6 6 4 6 6 4 4 5 6 4 4 7
#  3 3 3 6 0 0 5 5 5 5 6 2 1 2 0 5 3 2 6 0 0 2 7 0 1 2 4 2 1 7 2 4 3 5 7 1 7
#  2 7 1 2 1 5 4 2 3 7 7 2 5 2 2 7 5 7 7 7 1 3 2 2 2 3]
