from django.urls import path

from clinics import views

urlpatterns = [
    path("/list", views.ClinicListView.as_view()),
    path("/<str:clinic_id>", views.ClinicDetailView.as_view()),
]
