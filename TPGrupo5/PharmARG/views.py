from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    context = {
        "nombre_usuario": "Hugo",
        "apellido_usuario": "Granchetti",
    }

    return render(request, "PharmARG/index.html", context)


def alta_paciente(request):

    context = {}

    return render(request, "PharmARG/alta_paciente.html", context)


def editar_paciente(request):

    context = {}

    return render(request, "PharmARG/editar_paciente.html", context)


def consultas(request):

    listado_pacientes = [
        {
        "nombre_paciente": "Juan",
        "apellido_paciente": "Pérez",
        "edad_paciente": 53,
        "pats_paciente": "Hipertensión Arterial",
        "meds_paciente": "Enalapril",
        "presc_pend_paciente": 1
        },
        {
        "nombre_paciente": "Martín",
        "apellido_paciente": "González",
        "edad_paciente": 64,
        "pats_paciente": "Insuficiencia Cardíaca",
        "meds_paciente": "Carvedilol",
        "presc_pend_paciente": 2
        },
    ]

    context = {
        "listado_pacientes": listado_pacientes
    }

    return render(request, "PharmARG/consultas.html", context)