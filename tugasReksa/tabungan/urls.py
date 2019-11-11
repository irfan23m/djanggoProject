from django.urls import path
from . import views

urlpatterns = [
    path('/do_login', views.do_login)
]
