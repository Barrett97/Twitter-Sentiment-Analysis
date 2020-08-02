# Takes cleaned.csv as input and processes the file as day of the week and sentimental value
# for the corresponding tweet
# Outputs vader.txt which can then be mapped and reduced by sentmap.py - sentreducer.py

import sys
import re
import csv
import datetime as d
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA


reader = csv.reader(sys.stdin)
sia = SIA()
results = []
f = open("vader.txt", "w+")

for row in reader:
    tweet = row[1]
    row = row[0].split(" ")
    rowdate = row[0].split("-")

    year = rowdate[0]
    month = rowdate[1]
    day = rowdate[2]

    ans = d.date(int(year), int(month), int(day))

    pol_score = sia.polarity_scores(tweet)
    pol_score['headline'] = tweet
    results.append(pol_score)

    f.write(ans.strftime("%A") + '\t' + str(pol_score['neg']) + '\t' + str(pol_score['pos']) + '\t' + str(pol_score['neu']) + '\n')