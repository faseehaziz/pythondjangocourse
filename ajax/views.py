from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render, redirect
from ajax.models import Registration


def registration(req):
    return render(req, 'registration.html')

@csrf_exempt
def insert(req):
    a = req.POST['a1']
    b = req.POST['a2']
    c = req.POST['a3']
    d = req.POST['a4']
    e = req.POST['a5']
    Registration(name = a, password = b, email = c, phone = d, address = e).save()
    return JsonResponse({'message': 'Data Inserted'})

def display(req):
    a = Registration.objects.all()
    b = [{'id': i.id, 'name': i.name, 'password': i.password, 'email': i.email, 'phone': i.phone, 'address': i.address }for i in a]
    return JsonResponse({'key': b})

@csrf_exempt
def delete(req):
    a = req.POST['a']
    Registration.objects.get(id = a).delete()
    return JsonResponse({'message': 'Data deleted'})

@csrf_exempt
def update(req):
    a = req.POST['a']
    b = Registration.objects.get(id = a)
    c = [{'id': b.id, 'name': b.name, 'password': b.password, 'email': b.email, 'phone': b.phone, 'address': b.address}]
    return JsonResponse({'key2': c})

@csrf_exempt
def submit_update(req):
    a1 = req.POST['a']
    a = req.POST['b1']
    b = req.POST['b2']
    c = req.POST['b3']
    d = req.POST['b4']
    e = req.POST['b5']
    Registration.objects.filter(id = a1).update(name = a, password = b, email = c, phone = d, address = e)
    return JsonResponse({'message': 'Data updated'})
    