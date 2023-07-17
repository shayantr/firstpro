from django.shortcuts import render
from django.http import *
# Create your views here.


def index(request):
    return HttpResponse("Welcome to the daily dashboard!")


def dashboard(request,name):
    return render(request,'dashboard/user.html',{
        "name": name
    })

