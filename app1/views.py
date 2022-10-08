from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

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
    return render(request, 'js.html')

 
def jsNew(request):
    return render(request, 'jsNew.html')


def jslang(request):
    return render(request, 'jslang.html')


def jsfunc(request):
    return render(request, 'jsfunc.html')


def jsDom(request):
    return render(request, 'jsDom.html')


def jsform_validation(request):
    return render(request, 'jsform_validation.html')


def jquery(request):
    return render(request, 'jquery.html')


def jquery_validation(request):
    return render(request, 'jquery_validation.html')


def calculator(request):
    return render(request, 'calculator.html')


def mvt(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        # a = Registration(name = name, password = password, email = email, phone = phone, address = address)
        # a.save()
        Registration(name = name, password = password, email = email, phone = phone, address = address).save()
    return render(request, 'mvt.html')


def mvt_view(req):
    return render(req, 'mvt_viewworking.html')


def mvt_viewworking(request):
    a = int(request.GET['num1'])
    b = int(request.GET['num2'])
    c = a + b
    return render(request, 'mvt_viewworking.html', {'result': c})


def mvt_post_method(req):
    if req.method == 'POST':
        a = int(req.POST['num1'])
        b = int(req.POST['num2'])
        c = a + b
        return render(req, 'mvt_post_method.html', {'result': c})

    return render(req, 'mvt_post_method.html')


def mvt_table(req):
    a = Registration.objects.all()
    return render(req, 'mvt_table.html', {'disply': a})


def delete(req, id):
    # print(id)
    Registration.objects.get(id = id).delete()
    return redirect('mvt_table')


def update(req, id):
    a = Registration.objects.get(id = id)
    # print(a)
    return render(req, 'mvt_table_update.html', {'disply': a})


def submit_update(req, id):
    if req.method == 'POST':
        name = req.POST['name']
        password = req.POST['password']
        email = req.POST['email']
        phone = req.POST['phone']
        address = req.POST['address']
        Registration.objects.filter(id = id).update(name = name, password = password, email = email, phone = phone, address = address)     #filter is to get each field of the object whereas get is used to get the whole object

    return redirect('mvt_table')


def crud_login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        
        '''a = Registration.objects.get(email = username)
        if a.email == username and a.password == password:
            return redirect('mvt_table')'''
   
        try:
            a = Registration.objects.get(email = username, password = password)
            req.session['mysession'] = a.id
            return redirect('mvt_table')
        except Registration.DoesNotExist:
            # return redirect('crud_login')
            return render(req,'crud_login.html', {'message': 'Invalid credentials'})
    
    return render(req, 'crud_login.html')


def logout(req):
    del req.session['mysession']
    return redirect('crud_login')


def crud_userprofile(req):
    a = req.session['mysession']
    b = Registration.objects.get(id = a)
    return render(req, 'crud_userprofile.html', {'obj': b})
