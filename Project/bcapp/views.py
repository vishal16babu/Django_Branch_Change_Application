from django.shortcuts import render , get_object_or_404
from .models import Student
from .models import Preference
from .forms import StudentForm , PreferenceForm
from django.forms.formsets import formset_factory


def post_list(request):
	students = Student.objects.all()
	prefers = Preference.objects.all()
	return render(request, 'bcapp/index1.html', {'students' : students , 'prefers' : prefers})

def post_detail(request , pk):
	post = get_object_or_404(Student , pk = pk)
	return render(request, 'bcapp/index2.html', {'student' : post })

def post_new(request , num):
	form =  StudentForm 
	form2 = PreferenceForm 
	ArticleFormSet = formset_factory(PreferenceForm, extra=int(num))	

	return render(request, 'bcapp/index3.html', {'form': form , 'form2' : form2 , 'ArticleFormSet' : ArticleFormSet})
# Create your views here.
