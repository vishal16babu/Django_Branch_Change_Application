#!/usr/bin/python

import sys
import csv
from operator import itemgetter
if len(sys.argv) != 3:
	print 'Please pass only two argument ie.,  only the name of the  csv file'
	exit()
else :
	count = 0
	listofprogs = []
	filename = sys.argv[1]
	spamReader = csv.reader(open(filename))
	yow = []
	for row in spamReader:
		print row			
		listofprogs.append(row)	
	#print listofprogs
#input of students choices and checking their eligibility
	listofstuds = []
	filename = sys.argv[2]
	spamReader = csv.reader(open(filename))
	yow = []
	for row in spamReader:
		print row
		print "	"			
		listofstuds.append(row)	
