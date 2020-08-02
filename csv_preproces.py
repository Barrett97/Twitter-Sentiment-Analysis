import sys
import re
import csv
import datetime as d

reader = csv.reader(sys.stdin)

for row in reader:
	tweet = row[1]
	row = row[0].split(" ")
	rowdate = row[0].split("-")

	year = rowdate[0]
	month = rowdate[1]
	day = rowdate[2]

	ans = d.date(int(year), int(month), int(day))

	print(ans.strftime("%A"), end=' ')
	print(rowtweet)
	