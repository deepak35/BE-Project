""" This script combines all the refined dataset (c1.....c6) {rename the datasets as per repo names}
into a single csv (merged.csv)file"""

import csv
import re
import shuffleData
import preprocess
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
