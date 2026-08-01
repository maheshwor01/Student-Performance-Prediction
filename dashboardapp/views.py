from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from prediction.models import Prediction


@login_required
def dashboard(request):

    predictions = Prediction.objects.filter(user=request.user)

    total_predictions = predictions.count()

    latest_prediction = predictions.first()

    latest_score = latest_prediction.predicted_score if latest_prediction else 0

    if latest_score >= 80:
        performance = "Excellent"
    elif latest_score >= 60:
        performance = "Good"
    elif latest_score > 0:
        performance = "Average"
    else:
        performance = "--"

    context = {
        "total_predictions": total_predictions,
        "latest_score": latest_score,
        "performance": performance,
    }

    return render(request, "dashboard.html", context)