from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    return render(request,"login page.html")

def register(request):
    return render(request,"register.html")

def register2(request):
    
       
    uname=request.POST['uname']
    fname=request.POST['fname']
    lname=request.POST['lname']
    ename=request.POST['ename']
    pname=request.POST['pname']
    rename=request.POST['rename']
    if pname == rename:
        if User.objects.filter(username=uname).exists():
            umsg = 'the username has already taken'
            return render(request,"register.html",{'umsg':umsg})

        elif User.objects.filter(email=ename).exists():
            emsg = 'the email has already taken'
            return render(request,"register.html",{'emsg':emsg})

        

            
            
        else:
            user = User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=ename,password=pname)
            user.save();
            return render(request,'success.html')


    else:

        rmsg="the password is not matching"
        return render(request,"register.html",{"rmsg":rmsg})


def login2(request):
    uname=request.POST['uname']
    pname=request.POST['pname']
    user = auth.authenticate(username=uname,password=pname)
    if user is not None:
        auth.login(request,user)
    else:
        return render(request,'login.html')    
    print(user)
    return redirect('/')
    