from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('user_management.urls')),
    path('dashboard/', include('dashboardapp.urls')),
    path('prediction/', include('prediction.urls')),
]