from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('registration', views.registration, name = 'registration'),
    path('display', views.display, name  = 'display'),
    path('delete/<int:id>', views.delete, name = 'delete')
]