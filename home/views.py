
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def animal(request):
    return render(request , 'index.html',)

def blogs(request):
    return render(request, 'blogs.html')

def farm(request):
    return render(request, 'farm.html')

def Home(request):
    return render(request,"Home.html")

def hospital(request):
    return render(request,"hospital.html")
def login(request):
    return render(request ,"login.html")
def seller(request):
    return render(request,"seller.html")
