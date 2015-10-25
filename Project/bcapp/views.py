from django.shortcuts import render
from .models import Student
from .models import Preference
def post_list(request):
	students = Student.objects.get(pk=2)
	prefers = Preference.objects.filter(student=students)
	return render(request, 'bcapp/index.html', {'students' : prefers})
# Create your views here.
