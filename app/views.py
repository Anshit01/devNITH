from django.shortcuts import render

# Create your views here.
def index_handler(request):
    return render(request, 'index.html')

def internship_handler(request):
    return render(request, 'internship.html')

def internship_description_handler(request, id):
    context = {
        "id" : id
    }
    return render(request, 'internship_description.html', context)

def open_source_handler(request):
    return render(request, 'open_source.html')

def open_source_description_handler(request, id):
    context = {
        "id" : id
    }
    return render(request, 'open_source_description.html', context)

def register_handler(request):
    return render(request, 'register.html')
