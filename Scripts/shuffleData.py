"""This script shuffles the dataset (the one without X and *)"""

import csv
import random

def shuffle():
		with open('../datasets/merged.csv', 'rb') as inp, open('../datasets/ShuffledRefinedDataset.csv', 'wb') as out:
				data = csv.reader(inp)
				datalist = list(data)
				print "len: ", len(datalist)
				writer = csv.writer(out)
				writer.writerow(datalist[0])
				#print datalist[1]
				i = len(datalist)
				visited = [False] * i
				while i > 0 :
						num = random.randint(1,len(datalist))
						if not visited[num-1] :
								writer.writerow(datalist[num-1])
								visited[num-1] = True
								i -= 1
#shuffle()
#ShuffledRefinedDataset is the dataset which we will work on
