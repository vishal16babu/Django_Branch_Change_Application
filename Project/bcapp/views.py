from django.shortcuts import render , get_object_or_404
from .models import Student , User
from .models import Preference
from .forms import StudentForm , PreferenceForm , UserForm
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import redirect



def post_list(request):
	students = Student.objects.all()
	prefers = Preference.objects.all()
	return render(request, 'bcapp/index1.html', {'students' : students , 'prefers' : prefers})

def post_detail(request , pk):
	post = get_object_or_404(Student , pk = pk)
	return render(request, 'bcapp/index2.html', {'student' : post })

def post_new(request, pk):
	student = get_object_or_404(Student, pk=pk)
	if request.method == "POST":
		form = StudentForm(request.POST, instance=student)
		if form.is_valid():
			student = form.save(commit=False)
			student.save()
			return redirect('bcapp.views.post_detail', pk=student.pk)
	else:
		form = StudentForm(instance=student)
		form2 = PreferenceForm()
	return render(request, 'bcapp/index3.html', {'form': form})

def account_created(request):
	return render(request, 'bcapp/index4.html',{})

def details(request, pk):

	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid() :
			user = form.save(commit=False)
			user.login = User.objects.get(pk=pk)
			user.save()
			return redirect('bcapp.views.account_created')
	else:
		form = StudentForm()
		
	return render(request, 'bcapp/index3.html', {'form': form})	



def login(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid() :
			user = form.save(commit=False)
			q_set = Student.objects.filter(login__username=user.username )
			for stud in q_set :
				if stud.login.password == user.password :
					return redirect('bcapp.views.preference', pk=stud.pk)
					break
			return redirect('bcapp.views.login')

			
	else:
		form = UserForm()
		
	return render(request, 'bcapp/index3.html', {'form': form})


def create_account(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid() :
			user = form.save(commit=False)
			u = User(username=user.username , password = user.password)
			return redirect( 'bcapp.views.details' , pk=u.pk )
	else:
		form = UserForm()
		
	return render(request, 'bcapp/index3.html', {'form': form})







def preference(request , pk):
	student = Student.objects.get(pk=pk)
	return render(request, 'bcapp/index2.html', {'student': student})	



