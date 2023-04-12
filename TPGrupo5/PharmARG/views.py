from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        "user_name": "Hugo",
        "user_lastname": "Granchetti",
    }
    return render(request, "PharmARG/index.html", context)


def alta_paciente(request):

    context = {}

    return render(request, "PharmARG/alta_paciente.html", context)


def editar_paciente(request):

    context = {}

    return render(request, "PharmARG/editar_paciente.html", context)


def consultas(request):

    context = {}

    return render(request, "PharmARG/consultas.html", context)