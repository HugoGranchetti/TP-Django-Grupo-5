from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("alta_paciente", views.alta_paciente, name="alta_paciente")
]