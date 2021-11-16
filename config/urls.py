from django.urls import path, include

urlpatterns = [
    path("clinics", include("clinics.urls")),
]
