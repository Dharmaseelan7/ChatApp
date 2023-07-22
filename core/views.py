from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from room.models import Room

# Create your views here.


def firstpage(request):
    return render(request, "core/firstpage.html")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("firstpage")

    else:
        form = SignUpForm()

    return render(request, "core/signup.html", {"form": form})


def createroom(request):
    if request.method == "POST":
        roomname = request.POST.get("roomname")
        Room.objects.update_or_create(name=roomname, slug=roomname)
        return redirect("rooms")
    return render(request, "room/createroom.html")
