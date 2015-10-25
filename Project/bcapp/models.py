from django.db import models
from django.utils import timezone
import sys
import csv
from django import forms
from django.utils import html

listofprogs = []
filename = "./input/input_programmes.csv"
spamReader = csv.reader(open(filename))
for row in spamReader:          
    listofprogs.append(row) 
BRANCH_CHOICES = [(str(x+1),listofprogs[x][0]) for x in range(0,len(listofprogs))]

class Student(models.Model):
    
    CAT_CHOICES    = ((str(1), "GE"),(str(2), "OBC"),(str(3),"SC"),(str(4),"ST"),(str(5),"PwD"),)
    roll_number    = models.IntegerField(default=150050049)
    name	       = models.CharField(max_length=200)
    present_branch = models.CharField(max_length=9,choices=BRANCH_CHOICES,default=str(1))
    CPI		       = models.DecimalField(max_digits=3,decimal_places=2)
    category       = models.CharField(max_length=9,choices=CAT_CHOICES,default=str(1))

    def __str__(self):
        return str(self.roll_number)

class Preference(models.Model):
    student = models.ForeignKey(Student)
    branch = models.CharField(max_length=9,choices=BRANCH_CHOICES,default=str(1))
    
    #created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)

    #def publish(self):
        #self.published_date = timezone.now()
        #self.save()
    def __str__(self):              # __unicode__ on Python 2
        return listofprogs[int(self.branch)][0]

    
