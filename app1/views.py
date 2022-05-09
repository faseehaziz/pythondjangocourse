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


def grid(request):
    return render(request, 'grid.html')  


def bootstrap_grid(request):
    return render(request, 'bootstrap_grid.html')


def js(request):
    return render(request,'js.html')

 
def jsNew(request):
    return render(request,'jsNew.html')


def jslang(request):
    return render(request,'jslang.html')


def jsfunc(request):
    return render(request,'jsfunc.html')


def jsDom(request):
    return render(request,'jsDom.html')


def jsform_validation(request):
    return render(request,'jsform_validation.html')


def jquery(request):
    return render(request,'jquery.html')


def jquery_validation(request):
    return render(request,'jquery_validation.html')


def calculator(request):
    return render(request,'calculator.html')