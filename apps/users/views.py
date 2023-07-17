from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse
from django.http import *

from .models import *

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, 'users/user.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        passwrd = request.POST['password']
        user = authenticate(request, username=username, password=passwrd)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('users:index'))
        else:
            return render(request, 'users/login.html', {
                'massage': "invalid username or password"
            })
    return render(request, 'users/login.html', {
        'loginform': LoginForm()
    })

def logout_view(request):
    logout(request)
    return render(request,'users/login.html', {
        'massage': "LOGGED OUT"
    })

