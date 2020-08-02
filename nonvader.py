# Uses a mental health dictionary to map terms to a polarity
# Takes cleaned.csv as input and maps key value pairs for
# day of the week and corresponding sentimental value for the tweet
# Outputs nonvader.txt which can then be mapped nad reduced

import sys
import re
import csv
import datetime as d

dictionary = {}

with open('nonvaderdict.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
    	dictionary[row[0]] = row[1]

# print(dictionary)

reader = csv.reader(sys.stdin)
f = open("nonvader.txt", "w+")

for row in reader:
	wordcount = 0
	pos = 0
	neg = 0
	neu = 0
	tweet = row[1]
	tweet = row[1].split(" ")
	row = row[0].split(" ")
	for word in tweet:
		if (word in dictionary):
			if (dictionary.get(word) == 'positive'):
				pos += 1
				wordcount += 1
			elif (dictionary.get(word) == 'negative'):
				neg += 1
				wordcount += 1
			else:
				neu += 1
				wordcount += 1

	if (wordcount != 0):
		pos = pos/wordcount
		neg = neg/wordcount
		neu = neu/wordcount

	rowdate = row[0].split("-")

	year = rowdate[0]
	month = rowdate[1]
	day = rowdate[2]

	ans = d.date(int(year), int(month), int(day))

	f.write(ans.strftime("%A") + '\t' + str(neg) + '\t'  + str(pos) + '\t'  + str(neu) + '\n')