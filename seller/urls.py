from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('update_product/<int:id>', views.update_product, name = 'update_product'),
    path('delete_product/<int:id>', views.delete_product, name = 'delete_product'),
    path('signup', views.signup, name = 'signup'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('profile', views.profile, name = 'profile'),
    path('seller_details', views.seller_details, name = 'seller_details'),
    path('update/<int:id>', views.update, name = 'update'),
    path('submit_update/<int:id>', views.submit_update, name = 'submit_update'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('product', views.product, name = 'product')
]

