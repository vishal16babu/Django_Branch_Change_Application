from django.contrib import admin
from .models import Preference,Student, Document , branchname , catname , branch_num , cat_num 
import sys
import csv
from django.utils.encoding import smart_str
from django.http import HttpResponse
from copy import deepcopy
from operator import itemgetter




def delete_data(modeladmin, request , queryset):
	for f in queryset:
		f.delete()



def export_csv(modeladmin, request, queryset):
    
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=input_options.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)	
    for obj in queryset:
		temp=[smart_str(obj.roll_number),smart_str(obj.name),smart_str(branchname(obj.present_branch)),smart_str(obj.CPI),smart_str(catname(obj.category))]
		qset= Preference.objects.filter(student=obj)
		for pref in qset:
			temp.append(smart_str(branchname(pref.branch)))
		writer.writerow(temp)
    return response
export_csv.short_description = u"Export CSV"


def import_csv(modeladmin, request, queryset):
    for fn in queryset:
		spamReader = csv.reader(open("media/"+fn.filename()))
		for row in spamReader:
			q= Student(roll_number=row[0],name=row[1],present_branch=str(branch_num(row[2])),CPI=float(row[3]),category=str(cat_num(row[4])))
			q.save()

			for x in range(5,len(row)):
				if row[x] != '' :
					r =Preference(student=q,branch=str(branch_num(row[x])))
					print str(branch_num(row[x]))
					r.save()
    return 











def export_final_allocation_csv(modeladmin, request, queryset):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=final_allocation.csv'
	min_str = {}
	max_str = {}
	curr_str = {}
	sanc_str = {}
	init_str = {}
	last_allot = {}
	last_left = {}
	blocks = {}
	alpha = 0.75
	beta = 1.1
	listofprogs = []
	filename = "./input/input_programmes.csv"
	spamReader = csv.reader(open(filename))
	for row in spamReader:
		listofprogs.append(row)
		sanc_str[row[0]] = int(row[1])
		curr_str[row[0]] = int(row[2])
		init_str[row[0]] = int(row[2])
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




	for some_student in queryset :
		listofstuds.append(student_data(some_student))

	listofstuds = list(reversed(sorted(listofstuds, key=itemgetter(3))));

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


	changes = 1
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

	for x in range(0, len(listofstuds)):
		curr = x
		if not eligible[curr]:
			curr_br[curr] = 'Ineligible'
		if curr_br[curr] == root_br[curr]:
			curr_br[curr] = 'Branch Unchanged'	
		final.append([org_roll[curr],name[curr],root_br[curr],curr_br[curr]])


	writer = csv.writer(response, csv.excel)	
	response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)	

	final = list(sorted(final, key=itemgetter(2)));
	final = list(sorted(final, key=itemgetter(1)));
	final = list(sorted(final, key=itemgetter(0)));
	for x in range(0, len(final)):	
		writer.writerow(final[x])
	return response
export_final_allocation_csv.short_description = u"Export the Final Branch Change allocation as csv"









def student_data(student):
	strin=[]
	strin.append(student.roll_number)

	strin.append(student.name)

	strin.append(branchname(student.present_branch))

	strin.append(str(student.CPI))
	strin.append(catname(student.category))

	temp=Preference.objects.filter(student=student)
	for b_n in temp:
		temp1=branchname(b_n.branch)
		strin.append(temp1)

	return strin





















class PreferenceInline(admin.StackedInline):
    model = Preference
    extra = 1

class StudentAdmin(admin.ModelAdmin):
	actions = [export_csv, export_final_allocation_csv ,delete_data]
	inlines = [PreferenceInline]

class DocumentAdmin(admin.ModelAdmin):
	actions =  [import_csv, delete_data]
	model = Document

	

admin.site.register(Student, StudentAdmin)

admin.site.register(Document, DocumentAdmin)











