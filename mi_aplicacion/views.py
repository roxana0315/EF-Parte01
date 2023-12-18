from django.shortcuts import render
from django.http import HttpResponse

def Paises(request):
    return render(request, 'Paises.html', {})

def RegistrarPais(request):
    return render(request, 'RegistrarPais.html', {})

def Editoriales(request):
    return render(request, 'Editoriales.html', {})

def CrearEditorial(request):
    return render(request, 'CrearEditorial.html', {})


def index(request):
    return render(request, 'index.html')  # Reemplaza 'index.html' con el nombre de tu plantilla
# mi_aplicacion/views.py

