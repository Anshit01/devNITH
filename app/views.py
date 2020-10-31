from django.shortcuts import render
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from . import forms

# Create your views here.
def index_handler(request):
    return render(request, 'index.html')

def internship_handler(request):
    return render(request, 'internship.html')

def open_source_handler(request):
    return render(request, 'open_source.html')

class Register (CreateView):
	form_class = forms.UserCreateForm
	success_url = reverse_lazy('login')
	template_name='register.html'

