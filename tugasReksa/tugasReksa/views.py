from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import logout, get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from tabungan.models import User, ReksaDana
import datetime

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def do_login(request):
    user_name = request.POST.get('user_name','')
    user_password = request.POST.get('user_password','')

    user = auth.authenticate(request, username=user_name, password=user_password)

    if user is not None:
        auth.login(request, user)
        response = HttpResponseRedirect('/')
        request.session['user_name'] = user_name
        return response
    else:
        return HttpResponse("akun tidak ada")

def do_logout(request):
    logout(request)
    response = HttpResponseRedirect('/login')
    return response

def do_register(request):
    user_name = request.POST.get('user_name','')
    user_password = request.POST.get('user_password','')
    user_fullname = request.POST.get('user_fullname','')
    user_address = request.POST.get('user_address','')

    user = auth.authenticate(request, username=user_name, password=user_password)

    if user is None:
        user = get_user_model().objects.create_user(username=user_name, password=user_password, email='')

        if user is not None:
            user.is_staff = True
            user.is_active = True
            user.save()

        User.objects.create(userName=user_name, fullName=user_fullname, password='', address=user_address, dateReg=datetime.date.today(), exp=0, level=0)

        response = HttpResponseRedirect('/')
        request.session['user_name'] = user_name
        return response
    else:
        return HttpResponse("akun sudah ada")
