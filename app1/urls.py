from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('new',views.new,name='new'),
    path('last',views.last,name='last'),
]