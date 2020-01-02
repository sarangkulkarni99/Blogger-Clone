"""Defines url patterns for users"""
from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'

urlpatterns = [
    #Login page
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),

    #Logout page
    path('logout/', views.logout_view, name='logout'),

    #Registration Page
    path('register/', views.register, name='register'),
]
