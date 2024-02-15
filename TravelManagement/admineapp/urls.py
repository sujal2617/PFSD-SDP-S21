from django.urls import path
from . import views
urlpatterns=[
    path("TravelManagementhome",views.TravelManagementhome,name="TravelManagementhome"),
    path("loginfail",views.loginfail,name="loginfail"),
    path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),
    path("checkregistration",views.checkregistration,name="checkregistration"),
    path("checkpackages",views.checkpackages,name="checkpackages"),
    path("loadpackages",views.loadpackages,name="loadpackages"),

]