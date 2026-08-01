from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .models import StudentProfile


def home(request):
    return render(request, "home.html")


def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():

            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            profile = form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})


def user_login(request):
    return render(request, "registration/login.html")


def user_logout(request):
    logout(request)
    return redirect('home')