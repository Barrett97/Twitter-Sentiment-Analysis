import sys
import re
from datetime import datetime

for line in sys.stdin:
	line = re.sub(r'\n', '', line)
	words = line.split('\t')

	print(words[0]+ "\t" + words[1] + "\t" + words[2] + "\t" + words[3])