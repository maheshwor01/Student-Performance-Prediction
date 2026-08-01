from django.db import models
from django.contrib.auth.models import User


class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    hours_studied = models.FloatField()
    attendance = models.FloatField()
    previous_scores = models.FloatField()
    predicted_score = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.predicted_score}"


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

    student_id = models.CharField(max_length=30, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    course = models.CharField(
        max_length=50,
        choices=COURSE_CHOICES
    )

    semester = models.IntegerField()

    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.full_name