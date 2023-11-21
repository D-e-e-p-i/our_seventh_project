from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def java(request):
    return render(request,'java.html')

def java1(request):
    return HttpResponse('java is hugely used in industries')