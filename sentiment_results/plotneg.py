import os.path, sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np
import re

# Gets the filename from the command line
filename = sys.argv[1]

# Opens the file with the read parameter
f = open(filename,'r')

fig = plt.figure()

ax1 = fig.add_subplot(1,1,1)

days = {}
for line in f:
    values = line.split("\t")
    values[1] = re.sub(r'\n','',values[1])
    # print(values)
    days[values[0]] = float(values[1])*100

ax1.bar(days.keys(),days.values(),color=['red'])
plt.title('Sentiment Analysis Via Vader - Negative (-)')
plt.xlabel('Days of the Week')
plt.ylabel('User\'s Proportions (%)')
plt.ylim(26, 34) # vader
# plt.ylim(49, 57)
plt.show()