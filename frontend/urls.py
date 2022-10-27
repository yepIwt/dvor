from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.all_users, name = 'all users'),
]
