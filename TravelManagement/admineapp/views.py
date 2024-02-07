from django.http import HttpResponse
from django.shortcuts import render

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