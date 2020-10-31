from django.shortcuts import render

# Create your views here.
def index_handler(request):
    return render(request, 'index.html')

def internship_handler(request):
    return render(request, 'internship.html')

def open_source_handler(request):
    return render(request, 'open_source.html')

def register_handler(request):
    return render(request, 'register.html')
