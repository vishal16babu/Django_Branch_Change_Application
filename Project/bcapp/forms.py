from django import forms

from .models import Student , Preference

class PreferenceForm(forms.ModelForm):

    class Meta:
        model = Preference
        fields = ('branch',) 
         
class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('roll_number','name',)
