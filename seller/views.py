from random import random
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .models import *
from .decorator import auth_user


def update_product(req):
    pass


def delete_product(req):
    Add_product.objects.get(id = id).delete()
    return redirect('add_product')


def signup(req):
    if req.method == 'POST':
        name = req.POST['name']
        password = req.POST['password']
        email = req.POST['email']
        phone = req.POST['phone']
        address = req.POST['address']
        Seller_reg(name = name, password = password, email = email, phone = phone, address = address).save()
    return render(req, 'signup.html')


def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
   
        try:
            a = Seller_reg.objects.get(email = username, password = password)
            req.session['mysession'] = a.id
            return redirect('profile')
        except Seller_reg.DoesNotExist:
            return render(req,'login.html', {'message': 'Invalid credentials'})
    
    return render(req, 'login.html')


@auth_user
def profile(req):
    a = req.session['mysession']
    b = Seller_reg.objects.get(id = a)
    return render(req, 'profile.html', {'obj': b})


def logout(req):
    del req.session['mysession']
    return redirect('login')


def seller_details(req):
    a = Seller_reg.objects.all()
    return render(req, 'seller_details.html', {'disply': a})


def update(req, id):
    a = Seller_reg.objects.get(id = id)
    return render(req, 'update.html', {'disply': a})


def submit_update(req, id):
    if req.method == 'POST':
        name = req.POST['name']
        password = req.POST['password']
        email = req.POST['email']
        phone = req.POST['phone']
        address = req.POST['address']
        Seller_reg.objects.filter(id = id).update(name = name, password = password, email = email, phone = phone, address = address)     #filter is to get each field of the object whereas get is used to get the whole object

    return redirect('seller_details')


def delete(req, id):
    Seller_reg.objects.get(id = id).delete()
    return redirect('seller_details')

def product(req):
    a = req.session['mysession']
    if req.method == 'POST':
        name = req.POST['name']
        price = req.POST['price']
        description = req.POST['description']
        image = req.FILES['image']
        img_name = str(random()) + image.name
        file_storage = FileSystemStorage()
        file_storage.save(img_name, image)
        Product(name = name, price = price, description = description, image = img_name, seller_id_id = a).save()
        b = Product.objects.all()
        return render(req, 'product.html', {'disply': b})
    return render(req, 'product.html')


def img(req):
    a = Product.objects.all()
    return render(req, 'product.html', {'disply': a})
    