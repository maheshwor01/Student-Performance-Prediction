from django.db import models
from django.contrib.auth.models import User

COURSE_CHOICES = [
    ('BSc IT', 'BSc IT'),
    ('BCA', 'BCA'),
    ('BIT', 'BIT'),
    ('CSIT', 'CSIT'),
    ('BBA', 'BBA'),
    
]

YEAR_CHOICES = [
    ('1', 'First Year'),
    ('2', 'Second Year'),
    ('3', 'Third Year'),
    ('4', 'Fourth Year'),
]

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=20, choices=COURSE_CHOICES)
    year = models.CharField(max_length=5, choices=YEAR_CHOICES)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username