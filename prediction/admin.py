from django.contrib import admin
from .models import Prediction

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'hours_studied',
        'attendance',
        'previous_scores',
        'predicted_score',
        'created_at',
    )

    list_filter = (
        'created_at',
    )

    search_fields = (
        'user__username',
    )