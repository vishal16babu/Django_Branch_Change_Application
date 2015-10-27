from django.contrib import admin
from .models import Preference,Student, Document

class PreferenceInline(admin.StackedInline):
    model = Preference
    extra = 1
class StudentAdmin(admin.ModelAdmin):

    inlines = [PreferenceInline]   




admin.site.register(Student, StudentAdmin)

admin.site.register(Document)