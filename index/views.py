from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Customize,Checkout
from django.conf import settings 
from django.views.generic.base import TemplateView
from . import models



def home(request):

        return render(request,'index.html')

def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                 return redirect("/")
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')    
def register(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'Password not matching..')    
            return redirect('register')
        return redirect('/')
        
    else:
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def aboutus(request):
    return render(request,'aboutus.html')
def plans(request):
    return render(request,'plans.html')

@login_required(login_url="login")
def checkout(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
        
     return render(request,'checkout.html')
@login_required(login_url="login")
def ballondeco(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
        
     return render(request,'ballondeco.html')
@login_required(login_url="login")
def birthdaycard(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
     return render(request,'birthdaycard.html')
@login_required(login_url="login")
def picnic(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
     return render(request,'picnic.html')
@login_required(login_url="login")
def miniroadtrip(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
     return render(request,'miniroadtrip.html')
@login_required(login_url="login")
def visitingamu(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
     return render(request,'visitingamu.html')
@login_required(login_url="login")
def showincity(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
     return render(request,'showincity.html')
@login_required(login_url="login")
def photoshoot(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
     return render(request,'photoshoot.html')
@login_required(login_url="login")
def surprising(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
     return render(request,'surprising.html')
@login_required(login_url="login")
def aroyaldinner(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
     return render(request,'aroyaldinner.html')
@login_required(login_url="login")
def dinnerondunes(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
     return render(request,'dinnerondunes.html')
@login_required(login_url="login")
def dineronterace(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
     return render(request,'dineronterace.html')
@login_required(login_url="login")
def privatemovie(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
     return render(request,'privatemovie.html')
@login_required(login_url="login")
def bigcute(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
     return render(request,'bigcute.html')
@login_required(login_url="login")
def bouqet(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
     return render(request,'bouqet.html')
@login_required(login_url="login")
def surprisebox(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
     return render(request,'surprisebox.html')
@login_required(login_url="login")
def heartcollege(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
     return render(request,'heartcollege.html')
@login_required(login_url="login")
def bir(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
     return render(request,'bir.html')
@login_required(login_url="login")
def clipapic(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
     return render(request,'clipapic.html')
@login_required(login_url="login")
def comicart(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
     return render(request,'comicart.html')
@login_required(login_url="login")
def ecomic(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
     return render(request,'ecomic.html')
@login_required(login_url="login")
def memories(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
     return render(request,'memories.html')
@login_required(login_url="login")
def artframe(request):
     if request.method=='POST':
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        c=Checkout(date=date,time=time)
        c.save()    
     return render(request,'artframe.html')


def plans(request):
    return render (request,"plans.html",{'price' : 500})
    return render (request,"plans.html",{'price1' : 700})

@login_required(login_url="login")
def customize(request):
    if request.method=='POST':
        ordername=request.POST.get('ordername','')
        orderdate=request.POST.get('orderdate','')
        changes=request.POST.get('changes','')
        phno=request.POST.get('phno','')
        cust=Customize(ordername=ordername,orderdate=orderdate,changes=changes,phno=phno)
        cust.save()    
        return redirect('home')

    return render(request,'customize.html')


    

 
 