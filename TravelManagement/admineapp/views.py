from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .models import Admin, Register, Packages
from .models import Admin

def TravelManagementhome(request):
    return render(request, "TravelManagementhome.html")


def loginfail(request):
    return render(request, "loginfail.html")


def loadpackages(request):
    return render(request, "Package.html")


def checkadminlogin(request):
    if request.method == "POST":
        name = request.POST["uname"]  # gets user name
        pwdd = request.POST["pwd"]
        # flag = Admin.objects.filter(username=adminuname, password=adminpwd).values()
        flag = Register.objects.filter(username=name, password=pwdd).values()
        if flag:  # flag is not empty
            if name == "sujal2624":  # here "sujal2624" is admin
                messages.info(request,
                              "This is Admin's Travel Tourism Management page")  # to send message to the next page
                return render(request, "Adminhome.html")
        if flag:
            messages.info(request, "This is User's Travel Tourism Management page")
            return render(request, "TravelManagementhome.html")
        else:
            messages.info(request, "Your credentials are not correct")
            return render(request, "loginfail.html")


def checkregistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        addr = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if pwd == cpwd:
            if Register.objects.filter(username=uname).exists():
                messages.info(request, "username already exists......")
                return render(request, "register.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request, "email already exists.....")
                return render(request, "request.html")
            else:
                user = Register.objects.create(name=name, address=addr, email=email, phno=phno, username=uname,
                                               password=pwd)
                user.save()
                messages.info(request, "user created successfully....")
                return render(request, "login.html")
        else:
            messages.info(request, "Password not matching......")
            return render(request, "register.html")


def checkpackages(request):
    # return render(request, "package.html")
    if request.method == "POST":
        tcode = request.POST["tourcode"]
        tname = request.POST["tourname"]
        tpack = request.POST["tourpackage"]
        tdesc = request.POST["desc"]
        pack = Packages.objects.create(tourcode=tcode, tourname=tname, tourpackage=tpack, desc=tdesc)
        pack.save()
        messages.info(request, "Data inserted into the Table")
        return render(request, "Package.html")

    else:
        return render(request, "Package.html")


def viewplaces(request):
    data = Packages.objects.all()  # get all objects of package class
    return render(request, "viewplaces.html", {"placesdata": data})


def checkchangepassword(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        opwd = request.POST["opwd"]
        npwd = request.POST["npwd"]
        flag = Register.objects.filter(username=uname, password=opwd).values()
        if flag:
            Register.objects.filter(username=uname, password=opwd).update(password=npwd)
            messages.info(request, "Password updated successfully")
            return render(request, "index.html")
        else:
            return render(request, "changepassword.html")
    else:
        return render(request, "changepassword.html")


def logout(request):
    messages.info(request, "Lougout")
    return render(request, "index.html")


