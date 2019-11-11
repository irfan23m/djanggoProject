from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect

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
