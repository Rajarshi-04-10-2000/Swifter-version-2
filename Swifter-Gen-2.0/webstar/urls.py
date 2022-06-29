from django.contrib import admin
from django.urls import path
from webstar import views

urlpatterns = [
    
    path('', views.landing, name='landing page'),
    path('csignup', views.csignup, name='company signup'),
    path('clogin', views.clogin, name='company login'),
    path('dashc', views.dashc, name='company dashboard'),
    path('tlogin', views.tlogin, name='transporters company login'),
    path('tsignup', views.tsignup, name='transporters company signup'),
    path('dasht', views.dasht, name='trasnporter dashboard'),
    path('logoutt', views.logoutt, name='trasnporter log out'),
    path('tprofile', views.tprofile, name='trasnporter info'),
    path('addt', views.addt, name='trasnporter info loging'),
]
