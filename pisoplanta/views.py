from django.shortcuts import render, redirect
from pisoplanta.models import Centro #importamos el modelo
from pisoplanta.form import CrearCentro #importamos el formulario creado
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  DeleteView, UpdateView
from django.urls import reverse_lazy
# Create your views here.

#Vista del inicio de nuestra app
def home_pisoplanta(request):
    return render(request, 'homepisoplanta.html')
#vista para crear un centro de trabajo, los campos los recibimos por la URL: nombre, operacion que realiza y si esta activo o no (booleano  True/False)
@login_required
def crear_centro(request):

    centro = None
    if request.method == 'POST':
        formulario = CrearCentro(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            centro = Centro(nombre=info.get('nombre'), operacion=info.get('operacion'), activo=info.get('activo'), imagen=info.get('imagen')) 
            centro.save()
            return redirect('listar_centros')
    else:
        formulario = CrearCentro()
    
    return render(request, 'crear_centro.html', {'formulario': formulario}) 
            
    
#vista para listar los centros de trabajo almacenados en la base de datos
def listar_centros(request):
    centros = Centro.objects.all()
    return render(request, 'listar_centros.html', {'centros': centros})

class EditarCentro(LoginRequiredMixin, UpdateView):
    model = Centro
    fields = ['nombre', 'operacion', 'activo', 'imagen']
    template_name = 'editar_centro.html'
    context_object_name = 'centro'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listar_centros')
# def editar_centro(request, id):
#     centro = Centro.objects.get(id=id)
#     if request.method == 'POST':
#         formulario = CrearCentro(request.POST, request.FILES)
#         if formulario.is_valid():
#             info = formulario.cleaned_data
#             centro.nombre = info.get('nombre')
#             centro.operacion = info.get('operacion')
#             centro.activo = info.get('activo')
#             if info.get('imagen'):
#                 centro.imagen = info.get('imagen')
#             centro.save()
#             return redirect('listar_centros')
#     else:
#         formulario = CrearCentro(initial={
#             'nombre': centro.nombre,
#             'operacion': centro.operacion,
#             'activo': centro.activo,
#         })
#     return render(request, 'editar_centro.html', {'formulario': formulario, 'centro': centro})

# def eliminar_centro(request, id):
#     centro = Centro.objects.get(id=id)
#     if request.method == 'POST':
#         centro.delete()
#         return redirect('listar_centros')
#     return render(request, 'eliminar_centro.html', {'centro': centro})
class EliminarCentro(LoginRequiredMixin, DeleteView):
    model = Centro
    template_name = "eliminar_centro.html"
    context_object_name = "centro"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("listar_centros")

def ver_centro(request, id):
    centro = Centro.objects.get(id=id)
    return render(request, 'ver_centro.html', {'centro': centro})

def about(request):
    return render(request, 'about.html')