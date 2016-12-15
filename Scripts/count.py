"""This script is for counting number of distinct 
issues, product and sub products"""

import csv
import seaborn as sns
productDict = {}
subProductDict = {}
issueDict = {}
productList = {}
subProductList = {}

with open ('../datasets/ShuffledRefinedDataset.csv', 'rb') as fp:
	dataset = csv.reader(fp)
	next(dataset, None)
	#sns.countplot(y='Product',data=dataset)
	for row in dataset :
		product = row[1]
		subProduct = row[2]
		issue = row[3]

		#counting frequency of product, sub-product, issues
		if issue not in issueDict :
			issueDict[issue] = 1

		else :
			issueDict[issue] += 1


		if product not in productDict:
			productDict[product] = 1

		else :
			productDict[product] += 1

		if subProduct not in subProductDict:
			subProductDict[subProduct] = 1

		else :
			subProductDict[subProduct] += 1

		#building the heirarchy
		if product not in productList:
			productList[product] = {}
			productList[product][subProduct] = {}
			productList[product][subProduct][issue] = 1

		else :
			if subProduct not in productList[product] :
				productList[product][subProduct] = {}
				productList[product][subProduct][issue] = 1

			else :

				if issue not in productList[product][subProduct] :
					productList[product][subProduct][issue] = 1

				else :
					productList[product][subProduct][issue] += 1


print "-------------------PRODUCTS-----------------------"
for product in productDict:
	print product + " : " + str(productDict[product])

print "-------------------SUB-PRODUCTS-----------------------"

count = 0
for subProduct in subProductDict:
	print subProduct + " : " + str(subProductDict[subProduct])
	count += 1
print "No of sub-products : " + str(count)


print "-------------------ISSUES-----------------------"

count = 0
for issue in issueDict:
	print issue + " : " + str(issueDict[issue])
	count += 1
print "No of issues : " + str(count)


for product in productList :
	print "\n\n---" + product + " : " + str(productDict[product])+"----------"
	
	for subProduct in productList[product]:
		print "-------*****    " +subProduct + " : " + str(subProductDict[subProduct]) + "-------*****------\n" 

		for issue in productList[product][subProduct]:
			print "-------*****@@@@      " + issue + " : " + str(productList[product][subProduct][issue])
		print "\n"

	print "\n"

