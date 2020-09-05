from django.shortcuts import render, HttpResponse, redirect
from  .forms import DocenteForm


def docentes(request, plantilla="docentes.html"):
    return render(request, plantilla, {'docentes': docentes})
