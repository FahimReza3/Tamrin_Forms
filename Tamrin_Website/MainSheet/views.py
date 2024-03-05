from django.shortcuts import render
from .models import User
from .forms import LoginForm
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def Main(request):
    return render(request=request , template_name="Main.html" , context={})
def AddUser(request):
    msg=""
    if request.method == "POST":
        forms=LoginForm(request.POST)
        data=User(FullName=forms.data["FullName"] , Email=forms.data["Email"] , Password=forms.data["Password"])
        data.save()
        msg="کاربر با موفقیت ثبت شد"
    else:
        forms=LoginForm()

    return render(request=request , template_name="SignUp.html" , context={"Form" : forms , "Message" : msg})

def ViewUser(request):
    forms=LoginForm()
    DataBase=User.objects.all()
    return render(request=request , template_name="TableData.html" , context={"DataBase" : DataBase , "Form" : forms})

def DeletUser(request , id):
    Data=User.objects.filter(id=id).first()
    Data.delete()
    return HttpResponseRedirect("/ViewUser")

def UpdateUser(request):
    if request.method == "POST":
        forms=LoginForm(request.POST)
        id=forms.data["id"]
        User1=User.objects.filter(id=id).first()
        User1.FullName=forms.data["FullName"]
        User1.Email=forms.data["Email"]
        User1.Password=forms.data["Password"]
        User1.save()
        return HttpResponseRedirect("/ViewUser")
