from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from webstar.models import Tranporter, Company
from webstar.algo import CalculateVehical, CalculatePrice


# Create your views here.

def landing(request):
    return render(request,"landing.html")
    


def csignup(request):
    if request.method == 'POST':
        cname = request.POST['cname']
        cmail = request.POST['cmail']
        CGSTIN = request.POST['CGSTIN']
        cadd = request.POST['cadd']
        pass1 = request.POST['pass1']

        myuser = User.objects.create_user(cname, cmail, pass1)
        myuser.first_name = cname
        myuser.save()
        return render(request, 'clogin.html')

    return render(request, 'csignup.html')


def clogin(request):
    if request.method == 'POST':
        cloginname = request.POST['cloginname']
        cloginpass = request.POST['cloginpass']

        user = authenticate(username=cloginname, password=cloginpass)

        if user is not None:
            login(request, user)
            # messages.success(request, "Logged In Sucessfully!!")
            #return render(request, "dashc.html")
            return redirect('company dashboard')
        else:
            #messages.error(request, "Bad Credentials!!")
            return redirect('clogin')

    return render(request, "clogin.html")


def tsignup(request):
    if request.method == 'POST':
        tname = request.POST['tname']
        tmail = request.POST['tmail']
        tGSTIN = request.POST['tGSTIN']
        tadd = request.POST['tadd']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(tname, tmail, pass2)
        myuser.first_name = tname
        myuser.save()
        return render(request, 'tlogin.html')

    return render(request, 'tsignup.html')


def tlogin(request):
    if request.method == 'POST':
        cloginname = request.POST['cloginname']
        cloginpass = request.POST['cloginpass']

        user = authenticate(username=cloginname, password=cloginpass)

        if user is not None:
            login(request, user)
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "Baset.html")
        else:
            #messages.error(request, "Bad Credentials!!")
            return redirect('tlogin')

    return render(request, "tlogin.html")


def dashc(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        g_type = request.POST.get('g_type')
        src = request.POST.get('Source')
        dest = request.POST.get('Destination')
        weight = request.POST.get('weight')
        dist = request.POST.get('distance')
        company = Company(user_name=user_name, g_type=g_type,
                          src=src, dest=dest, weight=weight, dist=dist)
        company.save()
        trans = CalculateVehical(user_name)
        price = CalculatePrice(user_name)
        context = {
            'transporter': trans,
            'Price': price
        }
        return render(request, 'dashc.html', context)

    return render(request, 'dashc.html')


def dasht(request):
    return render(request, 'baset.html')


def logoutt(request):
    logout(request)
    return redirect('tlogin')


def tprofile(request):
    name = Tranporter.objects.filter(v_status="Available")

    context = {
                 'name': name,
        }

    return render(request, 'tprofile.html', context)


def addt(request):
    if request.method == "POST":
        dname = request.POST.get('dname')
        license_no = request.POST.get('license_no')
        dphone = request.POST.get('dphone')
        v_no = request.POST.get('v_no')
        v_type = request.POST.get('v_type')
        permit_wt = request.POST.get('permit_wt')
        transporter = Tranporter(dname=dname, license_no=license_no, dphone=dphone,
                                 v_no=v_no, v_type=v_type, permit_wt=permit_wt)
        transporter.save()
        return HttpResponse("submitted")
    return render(request, 'addt.html')
