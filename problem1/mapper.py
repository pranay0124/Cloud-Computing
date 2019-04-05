#!/usr/bin/env python
"""mapper.py"""

import sys, json

def uniqueify(seq, idfun=None): 
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result

# input comes from STDIN (standard input)
for line in sys.stdin:
	line = line.replace("[","")
	line = line.replace("]","")
	data = line.split(",",1)
	words = data[1].split()
	for w in uniqueify(words):
        	print '%s\t%s'%(w,data[0])
	
	



