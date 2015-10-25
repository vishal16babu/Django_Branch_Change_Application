from django.shortcuts import render
def post_list(request):
    return render(request, 'bcapp/index.html', {})
# Create your views here.
