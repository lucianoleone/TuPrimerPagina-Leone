from django.shortcuts import render
from pisoplanta.models import Centro #importamos el modelo
# Create your views here.

#Vista del inicio de nuestra app
def home_pisoplanta(request):
    return render(request, 'homepisoplanta.html')
#vista para crear un centro de trabajo, los campos los recibimos por la URL: nombre, operacion que realiza y si esta activo o no (booleano  True/False)
def crear_centro(request, nombre, operacion, activo):
    centro = Centro(nombre=nombre, operacion=operacion, activo=activo)
    centro.save()
    return render(request, 'crear_centro.html', {'centro': centro})
#vista para listar los centros de trabajo almacenados en la base de datos
def listar_centros(request):
    centros = Centro.objects.all()
    return render(request, 'listar_centros.html', {'centros': centros})