from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h2>Hi</h2>')

def login(request):
    return render(request,'index.html')
