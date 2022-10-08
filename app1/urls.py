from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('index', views.index, name = 'index'),
    path('login', views.login, name = 'login'),
    path('new', views.new, name = 'new'),
    path('last', views.last, name = 'last'),
    path('grid', views.grid, name = 'grid'),
    path('bootstrap_grid', views.bootstrap_grid, name = 'bootstrap_grid'),
    path('js', views.js, name = 'js'),
    path('jsNew', views.jsNew, name = 'jsNew'),
    path('jslang', views.jslang, name = 'jslang'),
    path('jsfunc', views.jsfunc, name = 'jsfunc'),
    path('jsDom', views.jsDom, name = 'jsDom'),
    path('jsform_validation', views.jsform_validation, name = 'jsform_validation'),
    path('jquery', views.jquery, name = 'jquery'),
    path('jquery_validation', views.jquery_validation, name = 'jquery_validation'),
    path('calculator', views.calculator, name = 'calculator'),
    path('mvt', views.mvt, name = 'mvt'),
    path('mvt_viewworking', views.mvt_viewworking, name = 'mvt_viewworking'),
    path('mvt_view', views.mvt_view, name = 'mvt_view'),
    path('mvt_post_method', views.mvt_post_method, name = 'mvt_post_method'),
    path('mvt_table', views.mvt_table, name = 'mvt_table'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('update/<int:id>', views.update, name = 'update'),
    path('submit_update/<int:id>', views.submit_update, name = 'submit_update'),
    path('crud_login', views.crud_login, name = 'crud_login'),
    path('logout', views.logout, name = 'logout'),
    path('crud_userprofile', views.crud_userprofile, name = 'crud_userprofile')
]