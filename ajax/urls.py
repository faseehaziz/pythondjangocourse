from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('registration', views.registration, name = 'registration'),
    path('insert', views.insert, name = 'insert'),
    path('display', views.display, name = 'display'),
    path('delete', views.delete, name = 'delete'),
    path('update', views.update, name = 'update'),
    path('submit_update', views.submit_update, name = 'submit_update')
]
