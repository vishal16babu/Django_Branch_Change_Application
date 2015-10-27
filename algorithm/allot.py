#!/usr/bin/python
from copy import deepcopy
import sys
import csv
from operator import itemgetter
if len(sys.argv) != 3:
	print 'Please pass only two argument ie.,  only the name of the  csv file'
	exit()
else :
	#dictionaries of programs for easy access using name of branch as key 
	min_str = {}
	max_str = {}
	curr_str = {}
	sanc_str = {}
	last_allot = {}
	last_left = {}
	blocks = {}
	alpha = 0.75
	beta = 1.1
	listofprogs = []
	filename = sys.argv[1]
	spamReader = csv.reader(open(filename))
	for row in spamReader:
		sanc_str[row[0]] = int(row[1])
		curr_str[row[0]] = int(row[2])
		min_str[row[0]] = int((float(row[1])*alpha)+0.5)
		max_str[row[0]] = int((float(row[1])*beta)+0.5)
		last_allot[row[0]] = '0'
		last_left[row[0]] = '0'
		blocks[row[0]] = []
		blocks[row[0]].append(['0',0.0])

	listofstuds = []	
	#input of students choices and checking their eligibility
	#dictionaries of students for easy access using roll numbers as keys 
	name = {}
	org_roll = {}
	cpi = {}
	root_br = {}
	curr_br = {}
	prefs = {}
	eligible = {}

	def eligible_f(person):
		return (person[4] == 'GE' and float(person[3]) >= 8.00) or (person[4] == 'SC' and float(person[3]) >= 7.00)

	filename = sys.argv[2]
	spamReader = csv.reader(open(filename))
	x = 1 
	for yow in spamReader:
		listofstuds.append(yow)


	listofstuds = list(reversed(sorted(listofstuds, key=itemgetter(3))));
	#print len(listofstuds)


	for x in range(0, len(listofstuds)):
		row = listofstuds[x]
	#	print row
		org_roll[x] = row[0]
		row[0] = x
		listofstuds[x][0] = x
		name[row[0]] = row[1]
		cpi[row[0]] = row[3]
		root_br[row[0]] = row[2]
		curr_br[row[0]] = row[2]
		prefs[row[0]] = row[5:]
		eligible[row[0]] = eligible_f(row)

	
#function defs 
	def vacant(br):
		return (max_str[br]-curr_str[br])>0

	def sufficient(br):
		return (curr_str[br]-min_str[br])>0	

	def rem_blocks(roll,br):
		item = [roll,cpi[roll]]
		if item in blocks[br]:
			blocks[br].remove(item)
     	#blocks[br] = list(reversed(sorted(blocks[br], key=itemgetter(1)))

	def update_blocks(roll,br):
		item = [roll,cpi[roll]]
		#print blocks[br]
		if item not in blocks[br]:
			blocks[br].append(item)
     		blocks[br] = list(reversed(sorted(blocks[br], key=itemgetter(1))))

	def allot(roll_no,pref_no):
		new_br = prefs[roll_no][pref_no]
		old_br = curr_br[roll_no]
		curr_str[old_br] = curr_str[old_br]-1
		last_left[old_br] = roll_no
		curr_str[new_br] = curr_str[new_br]+1
		last_allot[new_br] = roll_no
		for x in range(pref_no, len(prefs[roll_no])):
			if prefs[roll_no][x] == '':
					break			
			rem_blocks(roll_no,prefs[roll_no][x])
		prefs[roll_no] = prefs[roll_no][:pref_no]
		curr_br[roll_no] = new_br	
#allot
#rem_blocks
#update_blocks
	#print cpi
	changes = 1
	#print eligible
	while not changes == 0:
		changes = 0
		for x in range(0, len(listofstuds)):
			#print len(listofstuds)
			curr = x
			if not eligible[curr]:
				continue
			for y in range(0, len(prefs[curr])):
				b_fr = curr_br[curr]
				b_to = prefs[curr][y]
				if b_to == '':
					break			
				if cpi[curr] >= 9.0:
					if vacant(b_to):
						allot(curr,y)
						changes = changes+1
						break
					else:
						if cpi[last_allot[b_to]] == cpi[curr]:
							allot(curr,y)
							changes = changes+1
							break
						else:
							update_blocks(curr,b_to)
				else:
					if vacant(b_to):
						if cpi[blocks[b2][0]] <= cpi[curr]:
							if sufficient(b_fr):
								allot(curr,y)
								changes = changes+1
								break
							else:
								if cpi[last_left[b_fr]] == cpi[curr]:
									allot(curr,y)
									changes = changes+1
									break
								else:	
									update_blocks(curr,b_to)
						else:
							update_blocks(curr,b_to)
	
	final = []
	#print org_roll
	for x in range(0, len(listofstuds)):
		curr = x
		if not eligible[curr]:
			curr_br[curr] = 'Ineligible'
		if curr_br[curr] == root_br[curr]:
			curr_br[curr] = 'Branch Unchanged'	
		final.append([org_roll[curr],name[curr],root_br[curr],curr_br[curr]])
	
	#final = list(sorted(final, key=itemgetter(2)));
	#final = list(sorted(final, key=itemgetter(1)));
	final = list(sorted(final, key=itemgetter(0)));
	for x in range(0, len(final)):
		print final[x]
		#print x