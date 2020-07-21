from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.userinfo,name="userinfo"),
    path('check',views.getdata,name="getdata"),


]
