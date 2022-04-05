from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('new',views.new,name='new'),
    path('last',views.last,name='last'),
    path('grid',views.grid,name='grid'),
    path('bootstrap_grid',views.bootstrap_grid,name='bootstrap_grid'),
    path('js',views.js,name='js'),
    path('jsNew',views.jsNew,name='jsNew'),
    path('jslang',views.jslang,name='jslang'),
]