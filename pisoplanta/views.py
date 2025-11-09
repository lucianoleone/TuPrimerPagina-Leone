from django.shortcuts import render
from pisoplanta.models import Centro
# Create your views here.
def home_pisoplanta(request):
    return render(request, 'homepisoplanta.html')

def crear_centro(request, nombre, operacion, activo):
    centro = Centro(nombre=nombre, operacion=operacion, activo=activo)
    centro.save()
    return render(request, 'crear_centro.html', {'centro': centro})

def listar_centros(request):
    centros = Centro.objects.all()
    return render(request, 'listar_centros.html', {'centros': centros})