
import csv
import re

with open('./datasets/ShuffledRefinedDataset.csv', 'r') as fp:
    f = csv.reader(fp)
    next(f,None)
    for row in f:
        d = row[5]
        break

#.replace('[X]+','')
print type(d)
print d
d = re.sub('[X]+','', d)
print "---"
print d
