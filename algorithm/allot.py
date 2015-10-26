#!/usr/bin/python
from copy import deepcopy
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
		#print row			
		listofprogs.append(row)	
	#print listofprogs
	#input of students choices and checking their eligibility
	listofprogscopy = listofprogs[:]
	listofstuds = []
	filename = sys.argv[2]
	spamReader = csv.reader(open(filename))
	final = []
	for row in spamReader:
		#print row
		#print "	"			
		listofstuds.append(row)	
	listofstudscopy = deepcopy(listofstuds)
	listofstudscopy = list(reversed(sorted(listofstudscopy, key=itemgetter(3))))
	listofstuds = list(reversed(sorted(listofstuds, key=itemgetter(3))));
	#print listofstudscopy
	
	def eligible(person):
		if person[4] == 'GE':
			if float(person[3]) >= 8.00 :
				return True
			else:
				return False
		if person[4] == 'SC':
			if float(person[3]) >= 7.00 :
				return True
			else:
				return False

	for x in range(0, len(listofstudscopy)):
		
		
		if not eligible(listofstudscopy[x]) :
			listofstudscopy[x][3] = 'Ineligible'
			listofstuds[x][5] = 'Ineligible'
		listofstudscopy[x]=listofstudscopy[x][:4]
		#print listofstudscopy[x]		
#filtering the list			
	#listofstuds = filter(eligible, listofstuds);
#sorting the list based on merit
	
	


#dictionary of programs for easy access using tuple of name and cpi as key 
	diction_progs = {}
	for x in range(0, len(listofprogs)):
		diction_progs[listofprogs[x][0]] = listofprogs[x]

#	print diction_progs

#alpha and beta added

	alpha = 0.75
	beta = 1.1
	for x in range(0, len(listofprogs)):
		a = float(listofprogs[x][2])*alpha
		b = float(listofprogs[x][2])*beta
		listofprogs[x].append(int(round(a,0)))
		listofprogs[x].append(int(round(b,0)))
		listofprogs[x].append(0.0) #cpi of last alloted person
		#listofprogs[x].append(0.0) #highest cpi of  blocked persons
		listofprogs[x].append((0.0,[])) #names of highest cpi of  blocked persons
		#print listofprogs[x]
#listofprogs[x][0] prog name
#listofprogs[x][1] sanchaned strength
#listofprogs[x][2] curr_strength
#listofprogs[x][3] min lim
#listofprogs[x][4] max lim
#listofprogs[x][5] #cpi of last alloted person
#listofprogs[x][6] #highest cpi of  blocked persons
#listofprogs[x][7] #roll number of highest cpi of  blocked persons

	# print' vbb '
	# print diction_progs

#iterating based on the merit order
	def find_element_in_list(element,list_element):
        	try:
            		index_element=list_element.index(element)
            		return index_element
        	except ValueError:
            		return -1


	def vacant(br):
		#print br
		curr = diction_progs[br]
		if int(curr[2])<curr[4]:
			return True
		else:
			return False

	def sufficient(pq,y1):
		curr1 = diction_progs[pq[2]]
		if int(curr1[2])-1>=curr1[3]:
			return True
		else:
			# updating the highest cpi of  blocked persons
			curr1 = diction_progs[pq[y1]]
			#curr1[6]=max(curr1[6],pq[3])
			if curr1[6][0]==float(pq[3]) and find_element_in_list(pq[1],curr1[6][1])==-1:
				curr[6]=(curr1[6][0],curr1[6][1].append(pq[1]))
			if curr1[6][0]<float(pq[3]):
				curr[6]=(pq[3],curr1[6][1].append(pq[1]))
			return False


	def allot(p,y2,f,d):
		#f.append([p[0],p[1],p[2],b])
#updating the current strenght of the branch		
		d[p[y2]][2]=str(int(d[p[y2]][2])+1)
#updating the current strenght of the prev branch		
		d[p[2]][2]=str(int(d[p[2]][2])-1)
# updating cpi of last alloted person			
		d[p[2]][5] = p[3]
#updating current branch
		p[2]=str(p[y2])
#removing the previous blocks in this and lower branches
		for yo in range(y2, len(p)):
			if p[yo]=='':
				break
			tt=d[p[yo]]
			#print "no enthu"
			#print tt	
			if str(tt[6])==p[3]:
				ind=find_element_in_list(pq[1],tt[6][1])
				if ind!=-1:
					temp=tt[6][1]
					del temp[ind]
				if len(tt[6][0])==0:
					tt[6]=(0.0,[])	
#removing the lesser preffered coices
		#print 'emayya'
		del p[y2:]



	changes=1
	#f_prev=0
	# for x in range(0, len(listofstuds)):
	#  	print listofstuds[x]
	#  	print x
	
	while changes!=0:
		#	print changes
		changes=0
					
		for x in range(0, len(listofstuds)):
			if len(listofstuds[x])>5 and listofstuds[x][5]=='Ineligible':
				continue
			# 	print 'x '+ str(x)
			
#case1 if cpi>9
			if float(listofstuds[x][3]) >= 9.0:
				for y in range(0, len(listofstuds[x])-5):
					if listofstuds[x][y+5] == "":
						#listofstuds[x][0]=''
						break
					#print 'y '+ str(y)
				#print diction_progs[listofstuds[x][y+5]]
#if seats are vacant or last person alloted has same cpi then allot				
					if vacant(listofstuds[x][y+5]) or diction_progs[listofstuds[x][y+5]][5] == listofstuds[x][3]:
						allot(listofstuds[x],y+5,final,diction_progs)
						changes=changes+1
						#if y == 0:
						# 	#listofstuds[x][0]=''
						# 	f_prev=f_prev+1
						break;						

 			else:
 					#print listofstuds[x][3]
 					for y in range(0, len(listofstuds[x])-5):
 						if listofstuds[x][y+5] == "":
 							#listofstuds[x][0]=''
 							break
 						#print diction_progs[listofstuds[x][y+5]]
#if seats are vacant or last person alloted has same cpi then allot				
 						if sufficient(listofstuds[x],y+5):
 							if vacant(listofstuds[x][y+5])  or diction_progs[listofstuds[x][y+5]][5] == listofstuds[x][3]:
#if the seat is not blocked
 								if diction_progs[listofstuds[x][y+5]][6] < listofstuds[x][3]:
 									allot(listofstuds[x],y+5,final,diction_progs)
 									changes=changes+1
									#if y == 0:
										#listofstuds[x][0]=''
										#f_prev=f_prev+1
									break;														
 	
 	for x in range(0, len(listofstudscopy)):
		#print listofstudscopy[x]
		#print listofstuds[x]
		if listofstudscopy[x][3] =='Ineligible':
			continue
		if listofstudscopy[x][2] == listofstuds[x][2]:
			listofstudscopy[x][3] = 'Branch Unchanged'
		else:
			listofstudscopy[x][3] = listofstuds[x][2]
		listofstudscopy[x]=listofstudscopy[x][:4]
		#print listofstudscopy[x]
	listofstudscopy = list(sorted(listofstudscopy, key=itemgetter(0)))
	listofstuds = list(sorted(listofstuds, key=itemgetter(0)))
	
	for x in range(0, len(listofstudscopy)):
		print listofstuds[x]
		print listofstudscopy[x]
	
	#for x in range(0, len(listofstuds)):
		#print listofstuds[x]
		#print x
	#print len(listofstuds)
	# print len(final)
	#print list(diction_progs.values())


	#0.75 check with current branch not original (in next iterations)
	#dictionary of students
