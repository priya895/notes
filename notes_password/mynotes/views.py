from django.contrib.auth import authenticate,login,logout
# from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import HttpResponseRedirectBase
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from django.conf import settings
from django.core.mail import send_mail
import random
# Create your views here.
globe1=""
def index(request):
    return render(request,"mynotes/index.html")
def active(request):
    return render (request, "mynotes/index.html")
def login_view(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # current=request.user
        # temp=User.objects.filter(username=current.username)
        # request.session['globe1']=temp.email
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("homepage"))
            # try:
            #     return render(request,"mynotes/homepage.html",{
            #        'msg':user.email
            #     })
            # except User.DoesNotExist:
            #     return HttpResponse("no user!")

        else:
            return render(request, "mynotes/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request,"mynotes/login.html")
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "mynotes/register.html", {
                "message": "Passwords must match."
            })
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "mynotes/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return render(request,"mynotes/homepage.html")
    else:
        return render(request, "mynotes/register.html")
def homepage(request):
    return render(request,"mynotes/homepage.html")
def about(request):
    return render(request,"mynotes/about.html")
def contact(request):
    return render(request,"mynotes/contact.html")
@login_required(login_url='/login')
def create(request):
    if request.method== "POST":
        note= Notes()
        note.content=request.POST["content"]
        note.Title=request.POST["Title"]
        note.owner= request.user
        note.save()
        return redirect(fnotes)
    else:
        return render(request,"mynotes/create.html",{
            "list":Notes.objects.all()
        })
@login_required(login_url='/nlogin')
def fnotes(request):
    current=request.user
    try:
        return render(request, "mynotes/notes.html",{
            # "p":Notes.objects.filter(user=current),
            # "data":Notes.objects.all().values(),
            "p":Notes.objects.filter(owner=current).all(),
            "wishlist": True,
        })
    except Notes.DoesNotExist:
        return HttpResponse("No saved files in your notes!!!")
@login_required(login_url='/login')
def fshow(request,id):
    current=request.user
    return render(request, "mynotes/show.html",{
            "p":Notes.objects.filter(owner=current).all(),
            "pi":Notes.objects.filter(id=id),
            "wishlist": True,
    })
@login_required(login_url='/login')
def pcreate(request):
    if request.method== "POST":
        note= Fpass()
        note.ftitle=request.POST["title"]
        note.fpass=request.POST["password"]
        note.fuser= request.user
        note.save()
        return redirect(fpasswords)
    else:
        return render(request,"mynotes/pcreate.html",{
            "list":Notes.objects.all()
        })
@login_required(login_url='/plogin')
def fpasswords(request):
    current=request.user
    try:
        return render(request, "mynotes/passwords.html",{
            "p":Fpass.objects.filter(fuser=current).all(),
            "Fwish": True,
        })
    except Notes.DoesNotExist:
        return HttpResponse("No saved passwords in your notes!!!")

@login_required(login_url='/login')
def nlogin(request):
    # ok=globe1
    current=request.user
    # print(ok)
    global r
    r=random.randrange(1,10000,3)
    send_mail(
        'hello',
        str(r),
        settings.EMAIL_HOST_USER,
        [current.email, ],
    )
    return render(request,"mynotes/smail.html") 

@login_required (login_url = '/login')
def blogin(request):
    if request.method=='POST':
        # k=p()
        passw=request.POST['fpass']
        if passw==str(r):
            return redirect(fnotes)
        else:
            return HttpResponse(r)
    return render(request,"mynotes/homepage.html") 
