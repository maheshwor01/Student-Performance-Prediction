from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):

    COURSE_CHOICES = [
        ("BSc IT", "BSc IT"),
        ("BBA", "BBA"),
        ("BHM", "BHM"),
        ("BBS", "BBS"),
        ("BA", "Bachelor of Arts"),
        ("B.Tech", "Bachelor of Technology"),
        ("M.Tech", "Master of Technology"),
        ("MA", "Master of Arts"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    full_name = models.CharField(max_length=100)

    student_id = models.CharField(
        max_length=30,
        unique=True
    )

    email = models.EmailField(unique=True)

    course = models.CharField(
        max_length=50,
        choices=COURSE_CHOICES
    )

    semester = models.IntegerField()

    phone = models.CharField(max_length=15)

    address = models.TextField()

    date_of_birth = models.DateField()

    def __str__(self):
        return self.full_name