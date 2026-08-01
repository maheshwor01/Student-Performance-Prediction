from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import transaction

from .models import Prediction, Student


# =========================================================
# DASHBOARD
# =========================================================

@login_required
def dashboard(request):

    predictions = Prediction.objects.filter(
        user=request.user
    ).order_by("-created_at")

    latest_prediction = predictions.first()

    if latest_prediction:
        latest_score = float(
            latest_prediction.predicted_score or 0
        )
    else:
        latest_score = 0.0

    # Keep score between 0 and 100
    latest_score = max(
        0.0,
        min(latest_score, 100.0)
    )

    # Performance category
    if latest_score >= 80:
        performance = "Excellent"

    elif latest_score >= 60:
        performance = "Good"

    elif latest_score >= 40:
        performance = "Average"

    else:
        performance = "Poor"

    context = {
        "total_predictions": predictions.count(),
        "latest_score": latest_score,
        "performance": performance,
        "total_students": Student.objects.count(),
    }

    return render(
        request,
        "dashboard.html",
        context
    )


# =========================================================
# PREDICTION
# =========================================================

@login_required
def predict(request):

    prediction = None

    if request.method == "POST":

        try:

            # =================================================
            # GET VALUES FROM FORM
            # =================================================

            attendance_value = request.POST.get(
                "Attendance",
                ""
            ).strip()

            hours_value = request.POST.get(
                "Hours_Studied",
                ""
            ).strip()

            previous_value = request.POST.get(
                "Previous_Scores",
                ""
            ).strip()

            # These two fields are accepted from your form.
            # They are not stored because your current
            # Prediction model does not contain these fields.

            assignments_value = request.POST.get(
                "Assignments_Submitted",
                "0"
            ).strip()

            extracurricular_value = request.POST.get(
                "Extracurricular",
                "0"
            ).strip()


            # =================================================
            # CHECK REQUIRED FIELDS
            # =================================================

            if (
                not attendance_value
                or not hours_value
                or not previous_value
            ):

                messages.error(
                    request,
                    "Please fill in all required prediction fields."
                )

                return render(
                    request,
                    "predict.html",
                    {
                        "prediction": None
                    }
                )


            # =================================================
            # CONVERT VALUES
            # =================================================

            attendance = float(
                attendance_value
            )

            hours = float(
                hours_value
            )

            previous = float(
                previous_value
            )

            assignments = int(
                assignments_value or 0
            )

            extracurricular = int(
                extracurricular_value or 0
            )


            # =================================================
            # VALIDATION
            # =================================================

            if hours < 0:

                messages.error(
                    request,
                    "Study hours cannot be negative."
                )

                return render(
                    request,
                    "predict.html",
                    {
                        "prediction": None
                    }
                )


            if attendance < 0 or attendance > 100:

                messages.error(
                    request,
                    "Attendance must be between 0 and 100."
                )

                return render(
                    request,
                    "predict.html",
                    {
                        "prediction": None
                    }
                )


            if previous < 0 or previous > 100:

                messages.error(
                    request,
                    "Previous score must be between 0 and 100."
                )

                return render(
                    request,
                    "predict.html",
                    {
                        "prediction": None
                    }
                )


            if assignments < 0:

                messages.error(
                    request,
                    "Assignments cannot be negative."
                )

                return render(
                    request,
                    "predict.html",
                    {
                        "prediction": None
                    }
                )


            if extracurricular not in [0, 1]:

                messages.error(
                    request,
                    "Extracurricular must be either 0 or 1."
                )

                return render(
                    request,
                    "predict.html",
                    {
                        "prediction": None
                    }
                )


            # =================================================
            # CALCULATE PREDICTED SCORE
            # =================================================

            prediction = (
                hours +
                attendance +
                previous
            ) / 3


            # Keep score between 0 and 100

            prediction = max(
                0.0,
                min(prediction, 100.0)
            )


            # =================================================
            # SAVE PREDICTION
            # =================================================

            Prediction.objects.create(

                user=request.user,

                hours_studied=hours,

                attendance=attendance,

                previous_scores=previous,

                predicted_score=prediction,

            )


            # =================================================
            # SUCCESS MESSAGE
            # =================================================

            messages.success(
                request,
                "Prediction created successfully."
            )


        except (ValueError, TypeError):

            messages.error(
                request,
                "Please enter valid numeric values."
            )

            prediction = None


    # =================================================
    # SHOW PAGE
    # =================================================

    return render(
        request,
        "predict.html",
        {
            "prediction": prediction
        }
    )


# =========================================================
# PREDICTION HISTORY
# =========================================================

@login_required
def history(request):

    predictions = Prediction.objects.filter(
        user=request.user
    ).order_by("-created_at")

    history_data = []


    for prediction in predictions:

        # =================================================
        # GET STUDENT
        # =================================================

        student = Student.objects.filter(
            user=prediction.user
        ).first()


        if student:

            student_name = student.full_name

            roll_number = student.student_id

            course = student.course

            year = student.semester

        else:

            student_name = prediction.user.get_full_name()

            if not student_name:

                student_name = prediction.user.username

            roll_number = "N/A"

            course = "N/A"

            year = "N/A"


        # =================================================
        # PREDICTED SCORE
        # =================================================

        score = float(
            prediction.predicted_score or 0
        )

        score = max(
            0.0,
            min(score, 100.0)
        )


        # =================================================
        # PROBABILITY
        # =================================================

        probability = score / 100


        # =================================================
        # PREDICTED GRADE
        # =================================================

        if score >= 40:

            predicted_grade = "Pass"

        else:

            predicted_grade = "Fail"


        # =================================================
        # ADD TO HISTORY
        # =================================================

        history_data.append({

            "id": prediction.id,

            "student_name": student_name,

            "roll_number": roll_number,

            "course": course,

            "year": year,

            "created_at": prediction.created_at,

            "hours_studied": prediction.hours_studied,

            "attendance": prediction.attendance,

            "previous_scores": prediction.previous_scores,

            "predicted_score": score,

            "predicted_grade": predicted_grade,

            "probability": probability,

        })


    return render(
        request,
        "history.html",
        {
            "history_data": history_data
        }
    )


# =========================================================
# PREDICTION DETAIL
# =========================================================

@login_required
def prediction_detail(
    request,
    prediction_id
):

    prediction = get_object_or_404(
        Prediction,
        id=prediction_id,
        user=request.user
    )


    # =================================================
    # GET STUDENT
    # =================================================

    student = Student.objects.filter(
        user=prediction.user
    ).first()


    if student:

        student_name = student.full_name

        roll_number = student.student_id

        course = student.course

        year = student.semester

    else:

        student_name = prediction.user.get_full_name()

        if not student_name:

            student_name = prediction.user.username

        roll_number = "N/A"

        course = "N/A"

        year = "N/A"


    # =================================================
    # SCORE
    # =================================================

    score = float(
        prediction.predicted_score or 0
    )

    score = max(
        0.0,
        min(score, 100.0)
    )


    # =================================================
    # PROBABILITY
    # =================================================

    probability = score / 100


    # =================================================
    # GRADE
    # =================================================

    if score >= 40:

        predicted_grade = "Pass"

    else:

        predicted_grade = "Fail"


    # =================================================
    # CONTEXT
    # =================================================

    context = {

        "prediction": prediction,

        "student_name": student_name,

        "roll_number": roll_number,

        "course": course,

        "year": year,

        "predicted_score": score,

        "predicted_grade": predicted_grade,

        "probability": probability,

        "created_at": prediction.created_at,

    }


    return render(
        request,
        "prediction_detail.html",
        context
    )


# =========================================================
# STUDENTS
# =========================================================

@login_required
def students(request):

    students_list = Student.objects.all().order_by(
        "student_id"
    )

    return render(
        request,
        "student.html",
        {
            "students": students_list
        }
    )


# =========================================================
# COURSE
# =========================================================

@login_required
def course(request):

    return render(
        request,
        "course.html"
    )


# =========================================================
# PROFILE
# =========================================================

@login_required
def profile(request):

    return render(
        request,
        "profile.html"
    )


# =========================================================
# CHANGE PASSWORD
# =========================================================

@login_required
def change_password(request):

    return render(
        request,
        "change_password.html"
    )


# =========================================================
# STUDENT REGISTRATION
# =========================================================

def register_student(request):

    if request.method == "POST":

        # =================================================
        # GET USER INFORMATION
        # =================================================

        username = request.POST.get(
            "username",
            ""
        ).strip()

        first_name = request.POST.get(
            "first_name",
            ""
        ).strip()

        last_name = request.POST.get(
            "last_name",
            ""
        ).strip()

        email = request.POST.get(
            "email",
            ""
        ).strip()

        password = request.POST.get(
            "password",
            ""
        )

        confirm_password = request.POST.get(
            "confirm_password",
            ""
        )


        # =================================================
        # GET STUDENT INFORMATION
        # =================================================

        student_id = request.POST.get(
            "student_id",
            ""
        ).strip()

        course = request.POST.get(
            "course",
            ""
        ).strip()

        semester = request.POST.get(
            "semester",
            ""
        ).strip()

        phone = request.POST.get(
            "phone",
            ""
        ).strip()

        address = request.POST.get(
            "address",
            ""
        ).strip()


        # =================================================
        # REQUIRED FIELD VALIDATION
        # =================================================

        if not username:

            messages.error(
                request,
                "Username is required."
            )

            return redirect(
                "register_student"
            )


        if not email:

            messages.error(
                request,
                "Email is required."
            )

            return redirect(
                "register_student"
            )


        if not password:

            messages.error(
                request,
                "Password is required."
            )

            return redirect(
                "register_student"
            )


        if not student_id:

            messages.error(
                request,
                "Student ID is required."
            )

            return redirect(
                "register_student"
            )


        # =================================================
        # PASSWORD VALIDATION
        # =================================================

        if password != confirm_password:

            messages.error(
                request,
                "Passwords do not match."
            )

            return redirect(
                "register_student"
            )


        # =================================================
        # USERNAME VALIDATION
        # =================================================

        if User.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                "Username already exists."
            )

            return redirect(
                "register_student"
            )


        # =================================================
        # EMAIL VALIDATION
        # =================================================

        if User.objects.filter(
            email=email
        ).exists():

            messages.error(
                request,
                "Email already exists."
            )

            return redirect(
                "register_student"
            )


        # =================================================
        # STUDENT ID VALIDATION
        # =================================================

        if Student.objects.filter(
            student_id=student_id
        ).exists():

            messages.error(
                request,
                "Student ID already exists."
            )

            return redirect(
                "register_student"
            )


        # =================================================
        # CREATE USER + STUDENT
        # =================================================

        try:

            semester_number = int(
                semester
            )


            with transaction.atomic():

                # -----------------------------------------
                # Create Django User
                # -----------------------------------------

                user = User.objects.create_user(

                    username=username,

                    password=password,

                    email=email,

                    first_name=first_name,

                    last_name=last_name,

                )


                # -----------------------------------------
                # Create Student
                # -----------------------------------------

                Student.objects.create(

                    user=user,

                    student_id=student_id,

                    full_name=(
                        f"{first_name} {last_name}"
                    ).strip(),

                    email=email,

                    course=course,

                    semester=semester_number,

                    phone=phone,

                    address=address,

                )


            messages.success(
                request,
                "Student Registered Successfully."
            )

            return redirect(
                "login"
            )


        except ValueError:

            messages.error(
                request,
                "Semester must be a valid number."
            )

            return redirect(
                "register_student"
            )


        except Exception as e:

            print(
                "REGISTRATION ERROR:",
                e
            )

            messages.error(
                request,
                "Registration failed. Please try again."
            )

            return redirect(
                "register_student"
            )


    # =================================================
    # GET REQUEST
    # =================================================

    return render(
        request,
        "register.html"
    )