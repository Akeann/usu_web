from django.urls import path
from main import views

urlpatterns = [
    path("", views.home, name="home"),
    path("", views.home, name="illumina"),  # temporary
    path("", views.home, name="nanopore"),  # temporary
    path("", views.home, name="registration"),  # temporary
]
