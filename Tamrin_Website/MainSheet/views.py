from django.shortcuts import render
from .models import User
from .forms import LoginForm
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def Main(request):
    return render(request=request , template_name="Main.html" , context={})
def AddUser(request):
    if request.method == "POST":
        forms=LoginForm(request.POST)
        data=User(FullName=forms.data["FullName"] , Email=forms.data["Email"] , Password=forms.data["Password"])
        data.save()
        return HttpResponse("کاربر ثبت شد")

    else:
        forms=LoginForm()

    return render(request=request , template_name="SignUp.html" , context={"Form" : forms})
