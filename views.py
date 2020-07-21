from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import models

# Create your views here.

def userinfo(request):
    f1=forms.MyForm()
    return render(request,"user.html",{'form':f1})


def getdata(request):
    
    if request.method=="GET":
        un=request.GET['Username']
        p=request.GET['Password']
        pno=request.GET['PhoneNumber']
        a=request.GET['Address']
        U1=models.User(Username=un,Password=p,PhoneNumber=pno,Address=a)
        U1.save()
        return render(request,"valid.html",{"Username":un,"Password":p,"PhoneNumber":pno,"Address":a})


    if request.method=="POST":
        un=request.POST['Username']
        p=request.POST['Password']
        pno=request.POST['PhoneNumber']
        a=request.POST['Address']
        return render(request,"valid.html",{"Username":un,"Password":p,"PhoneNumber":pno,"Address":a})
