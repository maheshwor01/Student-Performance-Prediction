from django.urls import path
from . import views


urlpatterns = [

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "predict/",
        views.predict,
        name="predict"
    ),

    path(
        "history/",
        views.history,
        name="history"
    ),

    path(
        "prediction/<int:prediction_id>/",
        views.prediction_detail,
        name="prediction_detail"
    ),

    path(
        "students/",
        views.students,
        name="students"
    ),

    path(
        "course/",
        views.course,
        name="course"
    ),

    path(
        "profile/",
        views.profile,
        name="profile"
    ),

    path(
        "change-password/",
        views.change_password,
        name="change_password"
    ),

    path(
        "register/",
        views.register_student,
        name="register_student"
    ),
]