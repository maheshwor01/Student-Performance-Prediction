from django.shortcuts import render, redirect
from .models import Student


def students(request):

    if request.method == "POST":

        Student.objects.create(
            full_name=request.POST.get("full_name"),
            student_id=request.POST.get("student_id"),
            email=request.POST.get("email"),
            course=request.POST.get("course"),
            semester=request.POST.get("semester"),
            phone=request.POST.get("phone"),
            address=request.POST.get("address"),
            date_of_birth=request.POST.get("date_of_birth"),
        )

        return redirect("student")

    all_student = Student.objects.all()

    return render(request, "student.html", {
        "student": all_student
    })