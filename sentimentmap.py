import sys
import re
from datetime import datetime

for line in sys.stdin:
	# line = re.sub(r'^\W+|\W+$', '', line)
	words = re.split(r"\W+", line)

	date = datetime.strptime(words[0] + ' ' + words[1] + ' ' + words[2], '%Y %M %d').strftime('%A')

	print(date.lower() + "\t1")