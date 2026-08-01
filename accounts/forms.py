from django import forms
from django.contrib.auth.models import User
from .models import StudentProfile

class RegisterForm(forms.ModelForm):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = StudentProfile

        fields = [
            'roll_number',
            'course',
            'year',
            'contact',
            'address',
            'profile_picture'
        ]

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data