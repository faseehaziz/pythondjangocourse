from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h2>Hi</h2>')


def login(request):
    return render(request, 'index.html')


def logout(request):
    return HttpResponse('<h1>Logout Page')  


def new(request):
    return render(request, 'new.html')


def last(request):
    return render(request, 'last.html')    
