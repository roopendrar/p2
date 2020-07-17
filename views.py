from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("hello world")

def home(request):
    return HttpResponse("welcome to home page")

def html_demo1(request):
    return render(request,"sample.html")

def html_demo2(request):
    return render(request,"sample2.html")