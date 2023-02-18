from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index') ,# '/' means home page, views.index is calling the index function from views.py
    path('counter',views.counter,name = 'counter'),
    path('register',views.register, name = 'register'),
    path('login',views.login, name = 'login'),
    path('logout',views.logout, name='logout'),
    path('post/<str:pk>',views.post,name='post'), #here <str:pk> pk is a string variable 
]