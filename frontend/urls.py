from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'frontend'

urlpatterns = [
	path('all/', views.all_users, name = 'all_users'),
	path('<str:username>', views.user, name='user'),
	path('r/', views.registration, name = 'registration'),
	path('r/comp/', views.complete_registration, name = 'complete')
]
