from django.contrib import admin
from .models import Preference,Student, Document , branchname , catname , branch_num , cat_num
import sys
import csv
from django.utils.encoding import smart_str
from django.http import HttpResponse


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
		spamReader = csv.reader(open(fn.filename()))
		for row in spamReader:
			q= Student(roll_number=row[0],name=row[1],present_branch=str(branch_num(row[2])),CPI=float(row[3]),category=str(cat_num(row[4])))
			q.save()

			for x in range(5,len(row)):
				if row[x] != '' :
					r =Preference(student=q,branch=str(branch_num(row[x])))
					print str(branch_num(row[x]))
					r.save()
    return 


def import_final_csv(modeladmin, request, queryset):
    for fn in queryset:
		spamReader = csv.reader(open("./output/allotment.csv"))
		for row in spamReader:
			fn.roll_number = row[0]
			fn.name = row[1]
			fn.present_branch = row[3]

		
    return 
import_csv.short_description = u"Import Data from CSV"

class PreferenceInline(admin.StackedInline):
    model = Preference
    extra = 1

class StudentAdmin(admin.ModelAdmin):
	actions = [export_csv, delete_data]
	inlines = [PreferenceInline]

class DocumentAdmin(admin.ModelAdmin):
	actions =  [import_csv, delete_data]
	model = Document

	

admin.site.register(Student, StudentAdmin)

admin.site.register(Document, DocumentAdmin)