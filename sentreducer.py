import sys
import re

file = open("final_results_vader.txt", 'w+')

day = None
cneg = 0
cpos = 0
cneu = 0
numdays = 0;

for line in sys.stdin:
	line = re.sub(r'\n', '', line)
	key, neg, pos, neu = line.split('\t')

	if key != day:
		if day is not None:
			print(day + '\t' + str(cneg/numdays) + '\t' + str(cpos/numdays) + '\t' + str(cneu/numdays))
			file.write(day + '\t' + str(cneg/numdays) + '\t' + str(cpos/numdays) + '\t' + str(cneu/numdays) + '\n')
		day = key
		cneg = 0
		cpos = 0
		cneu = 0
		numdays = 0

	cneg += float(neg)
	cpos += float(pos)
	cneu += float(neu)
	numdays += 1

print(day + '\t' + str(cneg/numdays) + '\t' + str(cpos/numdays) + '\t' + str(cneu/numdays))
file.write(day + '\t' + str(cneg/numdays) + '\t' + str(cpos/numdays) + '\t' + str(cneu/numdays) + '\n')