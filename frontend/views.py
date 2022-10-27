from django.shortcuts import render
from django.http import HttpResponse
from core.models import Profile
from django.shortcuts import render

# Create your views here.

def all_users(request):
    all = Profile.objects.all()
    return render(request, 'users/list.html', {'users': all})