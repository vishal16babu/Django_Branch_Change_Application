from django.contrib import admin
from .models import Preference,Person

class PreferenceInline(admin.StackedInline):
    model = Preference
    extra = 1
class PersonAdmin(admin.ModelAdmin):

    inlines = [PreferenceInline]   



admin.site.register(Person, PersonAdmin)

