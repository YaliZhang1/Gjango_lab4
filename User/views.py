from django.shortcuts import render
from django.http import HttpResponse
from faker import Faker
from .models import User
# Create your views here.

def user(request):
   users = User.objects.all() 
   return render(request,'home.html',{'users': users})



     

