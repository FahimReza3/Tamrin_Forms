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
    DataBase=User.objects.all()
    return render(request=request , template_name="TableData.html" , context={"DataBase" : DataBase})

def DeletUser(request , id):
    Data=User.objects.filter(id=id).first()
    Data.delete()
    return HttpResponseRedirect("/ViewUser")
