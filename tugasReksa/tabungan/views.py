from django.shortcuts import render
from django.contrib import auth

def do_login(request):
    user_name = request.POST.get('user_name','')
    user_password = request.POST.get('user_password','')

    user = auth.authenticate(request, username=user_name, password=user_password)

    if user is not None:
        auth.login(request, user)
        response = HttpResponseRedirect('/index')
        response.set_cookie('user_name', user_name, 3600)
        return response
    else:
        error_json = {'error_message': 'Username or password is not correct.'}
        return render(request, '/login', error_json)
