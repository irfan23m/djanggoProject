from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import logout, get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from tabungan.models import User, ReksaDana
from tabungan import forms
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
        # response = HttpResponseRedirect('/')
        request.session['user_name'] = user_name
        # return response
        response = HttpResponseRedirect('/')
        return response
    else:
        return render(request, 'login.html',{'message':'Akun tidak ditemukan'})

def index(request):
    user = User.objects.get(userName__exact = request.session['user_name'])
    reksa = ReksaDana.objects.all().filter(userName__exact= request.session['user_name'])
    cash = 0

    for item in reksa:
        cash += (item.price * item.unitNumber)
        
    level = cash / 1000000
    exp = cash % 1000000

    Dict = {
        'user'  : user,
        'reksa' : reksa,
        'cash'  : cash,
        'level' : level,
        'exp'   : exp,
    }
    return render(request, 'index.html', context=Dict)

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

        User.objects.create(userName=user_name, fullName=user_fullname, password='', address=user_address, dateReg=datetime.date.today())

        response = HttpResponseRedirect('/')
        request.session['user_name'] = user_name
        return response
    else:
        return render(request, 'register.html',{'message':'Username sudah digunakan'})

def update(request, key):
    user = User.objects.get(userName__exact=key)
    form = forms.newUserForm(instance=user)
    reksa = ReksaDana.objects.all().filter(userName_id=key)
    cash = 0
    
    for item in reksa:
        cash += (item.price * item.unitNumber)
    
    level = cash / 1000000
    exp = cash % 1000000

    Dict = {
            'user'  : user,
            'reksa' : reksa,
            'cash'  : cash,
            'level' : level,
            'exp'   : exp,
        }
    if request.method == 'POST':
        form = forms.newUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save(commit=True)
            #return index(request)
            return render(request, 'index.html', context=Dict)
        else:
            print("Validation Error!")
    return render(request, 'form.html',{'form':form, 'user':user})

def sell(request, key):
    reksaSell = ReksaDana.objects.get(id=key)
    reksaSell.delete()
    response = HttpResponseRedirect('/')
    return response
    
def belireksa(request, key):
    user = User.objects.get(userName__exact=key)
    Dict = {
        'user':user
    }
    return render(request, 'beli-reksa.html', context=Dict)

def do_belireksa(request):
    username = request.POST.get('username','')
    nama_reksa =  request.POST.get('reksa_name','')
    unitPrice_reksa = request.POST.get('reksa_unitPrice','')
    unitNumber_reksa = request.POST.get('reksa_unitNumber','')

    ReksaDana.objects.create(userName_id=username, name=nama_reksa, price=unitPrice_reksa, unitNumber=unitNumber_reksa)
    response = HttpResponseRedirect('/')
    return response
