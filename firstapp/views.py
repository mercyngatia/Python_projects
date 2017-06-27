from django.shortcuts import render
from django.http import HttpResponse
# from .models import Student

# Create your views here.
def Welcome(request):
    return HttpResponse("<p>Welcome to AkiraChix class</p>")
def Students(request):
    return HttpResponse("<p>Welcome to our class 2017, feel a home.</p>")
def Teachers(request):
    return HttpResponse("<p>Here we will show all the teachers at Akirachix.</p>")
    
    
    
    
    
    
# def Welcome(request):
#     return render(request, 'welcome_students.html')
# def  students(request):
#     return render(request, "<p>Here we will show all students</p>")
    
    