from django.shortcuts import render
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from . import forms
from .models import InternshipPost, OpenSourcePost

# Create your views here.
def index_handler(request):
    return render(request, 'index.html')

def internship_handler(request):
    context = {
        'posts' : InternshipPost.objects.all()
    }
    return render(request, 'internship.html', context)

def internship_description_handler(request, id):
    context = {
        'post' : InternshipPost.objects.filter(id=id)[0]
    }
    return render(request, 'internship_description.html', context)

def open_source_handler(request):
    context = {
        'posts' : OpenSourcePost.objects.all()
    }
    return render(request, 'open_source.html', context)

def open_source_description_handler(request, id):
    context = {
        'post' : OpenSourcePost.objects.filter(id=id)[0]
    }
    return render(request, 'open_source_description.html', context)

def register_handler(request):
    return render(request, 'register.html')

class Register (CreateView):
	form_class = forms.UserCreateForm
	success_url = reverse_lazy('login')
	template_name='register.html'

def dashboard_view(request):
    if request.user.is_authenticated:
        render(request, 'dashboard.html')

def internship_post_form_view(request):
    form = forms.InternshipPostCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        'form' : form
    }
    
    return render(request, 'internship_post_form.html', context)

def open_source_post_form_view(request):
    form = forms.OpenSourcePostCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        'form' : form
    }
    return render(request, 'open_source_post_form.html', context)