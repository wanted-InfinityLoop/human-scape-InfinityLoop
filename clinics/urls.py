from django.urls import path

from clinics.views import ClinicDetailView

urlpatterns = [
    path("/<str:clinic_id>", ClinicDetailView.as_view()),
]
