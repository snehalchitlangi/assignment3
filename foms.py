from django import forms

class MyForm(forms.Form):
    Username=forms.CharField(label="Username",max_length=20)
    Password=forms.CharField(label="Password",max_length=10)
    PhoneNumber=forms.CharField(label="PhoneNumber",max_length=10)
    Address=forms.CharField(label="Address",max_length=20)
