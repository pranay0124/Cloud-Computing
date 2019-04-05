#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = []
word = None

# input comes from STDIN
for line in sys.stdin:    
# remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, li = line.split('\t', 1)
    #print word + ",," + li
    if current_word == word:
        if li not in current_count:
            current_count.append(li)
    else:
        if current_word:
            # write result to STDOUT
            print '%s\t%s' % (current_word, current_count)
	current_count=[]
        if li not in current_count:
            current_count.append(li)
        current_word = word    

   
