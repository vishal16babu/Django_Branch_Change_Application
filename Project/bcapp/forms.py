from django import forms

from .models import Student , Preference 
from .models import User
class PreferenceForm(forms.ModelForm):

    class Meta:
        model = Preference
        fields = ('branch',) 
         
class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('roll_number','name','present_branch','CPI','category',)


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username','password',)
		widgets = {'password': forms.PasswordInput(),}



		
