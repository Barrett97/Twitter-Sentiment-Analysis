# Cleans all.csv which holds tweets and their time
# Outputs cleaned.csv for further preprocessing by vader.py or nonvader.py

import sys
import re
import csv
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

reader = csv.reader(sys.stdin)
stop_words = set(stopwords.words('english'))

f = open("cleaned.csv", "w+")

def main():
	for row in reader:
		tweet = row[1]
		tweet = re.sub(r'(https(.)*)|(@[A-Za-z0-9-_]+)|\'|\"|\.|\/|\\|(#[A-Za-z0-9-_]+)', '', tweet)
		tweet = re.sub(r'-', ' ', tweet)
		tweet = re.sub(r'^\W+|\W+$|', '', tweet)
		words = re.split(r"\W+", tweet)
		tokenized_row = word_tokenize(tweet)
		cleaned = [token for token in tokenized_row if token not in stop_words and len(token) != 1]
		f.write(row[0] + ',' + list_to_string(cleaned))
		

def list_to_string(list_data):
	result = ''
	for data in list_data:
		result += data.lower() + ' '
	return result + '\n'

main()