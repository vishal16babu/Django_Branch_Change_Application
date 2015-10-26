from django.shortcuts import render , get_object_or_404
from .models import Student
from .models import Preference
def post_list(request):
	students = Student.objects.all()
	prefers = Preference.objects.all()
	return render(request, 'bcapp/index1.html', {'students' : students , 'prefers' : prefers})

def post_detail(request , pk):
	post = get_object_or_404(Student , pk = pk)
	return render(request, 'bcapp/index2.html', {'student' : post })
# Create your views here.
