from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from . models import Admin , Register
from .models import Admin


def TravelManagementhome(request):
    return render(request, "TravelManagementhome.html")

def loginfail(request):
     return render(request, "loginfail.html")
def checkadminlogin(request):
    if request.method == "POST":
        adminuname = request.POST["uname"]  # gets user name
        adminpwd = request.POST["pwd"]
        flag = Admin.objects.filter(username=adminuname, password=adminpwd).values()
        if flag:
            return render(request, "TravelManagementhome.html")
        else:
            return render(request,"loginfail.html")

def checkregistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        addr = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["Phno"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if pwd == cpwd:
            if Register.objects.filter(username=uname).exists():
                messages.info(request,"username already taken......")
                return render(request,"register.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request,"email already taken.....")
                return render(request,"request.html")



