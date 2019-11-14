"""tugasReksa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_required(views.index), name='index'),
    path('login/',views.login),
    path('register/',views.register),
    path('belireksa/<str:key>', login_required(views.belireksa), name='beli'),
    path('do_login/', views.do_login),
    path('do_logout/', views.do_logout),
    path('do_register/', views.do_register),
    path('do_belireksa/', views.do_belireksa),
    path('update/<str:key>', login_required(views.update), name='update'),
    path('sell/<str:key>', views.sell, name='sell'),
]
