from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def animal(request):
    return render(request , 'index.html',)
