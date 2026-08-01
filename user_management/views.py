from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.db import transaction

from prediction.models import Student


def home(request):
    return render(request, "home.html")


# ===========================
# Student Registration
# ===========================
def register(request):

    if request.method == "POST":

        username = request.POST.get("username", "").strip()
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        email = request.POST.get("email", "").strip()

        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        student_id = request.POST.get("student_id", "").strip()
        course = request.POST.get("course")
        semester = request.POST.get("semester")
        phone = request.POST.get("phone", "")
        address = request.POST.get("address", "")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("register")

        if Student.objects.filter(student_id=student_id).exists():
            messages.error(request, "Student ID already exists.")
            return redirect("register")

        try:
            with transaction.atomic():

                user = User.objects.create_user(
                    username=username,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                )

                Student.objects.create(
                    user=user,
                    student_id=student_id,
                    full_name=f"{first_name} {last_name}",
                    email=email,
                    course=course,
                    semester=int(semester),
                    phone=phone,
                    address=address,
                )

            messages.success(request, "Registration Successful.")
            return redirect("login")

        except Exception as e:
            messages.error(request, str(e))
            return redirect("register")

    return render(request, "register.html")


# ===========================
# Login
# ===========================
def login_user(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect("dashboard")

        messages.error(request, "Invalid username or password.")

    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


# ===========================
# Logout
# ===========================
def logout_user(request):
    logout(request)
    return redirect("home")