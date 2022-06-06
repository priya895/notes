from django.contrib.auth import authenticate,login,logout
# from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import HttpResponseRedirectBase
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def index(request):
    return render(request,"mynotes/index.html")
def active(request):
    return render (request, "mynotes/index.html")
def login_view(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("homepage"))
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
        note=Notes()
        note.content=request.POST["content"]
        note.Title=request.POST["Title"]
        note.save()
        # return HttpResponseRedirect(reverse("homepage"))
        try:
             w=Fnote.objects.get(user=request.user)
        except Fnote.DoesNotExist:
             w=Fnote.objects.create(user=request.user)
        p=Fnote.objects.get(user=request.user)
        p.files.add(note)
        return redirect("notes")
    else:
        return render(request,"mynotes/create.html",{
            "list":Notes.objects.all()
        })
@login_required(login_url='/login')
def fnotes(request):
    current=request.user
    try:
        instance= Fnote.objects.get(user=current)
        return render(request, "mynotes/index.html",{
            "p":instance.item.all(),
            "Mynotes": True,
        })
    except Fnote.DoesNotExist:
        return HttpResponse("<h1>No saved files in your notes!!!</h1>")





