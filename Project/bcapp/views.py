from django.shortcuts import render , get_object_or_404
from .models import Student , User , branchname , catname
from .models import Preference
from .forms import StudentForm , PreferenceForm , UserForm , IndexForm
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from .models import Document


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
@login_required
def account_created(request):
	return render(request, 'bcapp/index4.html',{})
	
@login_required
def details(request, pk):

	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid() :
			user = form.save(commit=False)
			user.login = User.objects.get(pk=pk)
			user.save()
			return redirect('bcapp.views.account_created')
	else:
		form = StudentForm()
		
	return render(request, 'bcapp/index6.html', {'form': form})	


@login_required
def login(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid() :
			user = form.save(commit=False)
			q_set = Student.objects.filter(login__username=user.username )
			for stud in q_set :
				if stud.login.password == user.password :
					return redirect('preference', pk=stud.pk)
					break
			return redirect('bcapp.views.login')

			
	else:
		form = UserForm()
		
	return render(request, 'bcapp/index1.html', {'form': form})

@login_required
def create_account(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid() :
			user = form.save(commit=False)
			u = User(username=user.username , password = user.password)
			u.save()
			return redirect( 'details' , pk=u.pk )
	else:
		form = UserForm()
		
	return render(request, 'bcapp/index5.html', {'form': form})






@login_required
def preference(request , pk):
	student = Student.objects.get(pk=pk)
	branch = branchname(student.present_branch)
	cat = catname(student.category)
	prefers = Preference.objects.filter(student=student)
	if request.method == "POST":
		form = PreferenceForm(request.POST)
		if form.is_valid() :
			brranch = form.save(commit=False)
			b = Preference(student=student , branch = int(brranch.branch)) 
			b.save()
			return redirect( 'preference' , pk=pk )
		else:
			form2 = IndexForm(request.POST)
			if form2.is_valid() :
				ind = form2.save(commit=False)
				if int(ind.index)  <= len(prefers) :
					b = prefers[int(ind.index)-1] 
					b.delete()
				return redirect( 'preference' , pk=pk )
	else:		

		form = PreferenceForm()
		form2 = IndexForm()
	return render(request, 'bcapp/index7.html', {'student': student , 'branch': branch , 'cat': cat , 'prefers': prefers , 'form' : form , 'form2': form2 })	



