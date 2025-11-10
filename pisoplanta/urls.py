from django.contrib import admin
from django.urls import path, include
from pisoplanta.views import home_pisoplanta, crear_centro, listar_centros # Importar las vistas desde pisoplanta.views
#Creamos un archivo URL para la app pisoplanta, como no tenemos otra la dejamos definida en el home del proyecto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_pisoplanta), #Pantalla de inicio de la appo y por lo tanto del proyecto
    path('crear-centro/<nombre>/<operacion>/<activo>/', crear_centro), # Ruta para crear un centro de trabajo nuevo
    path('listar-centros/', listar_centros), # Ruta para listar los centros de trabajo de la base de datos
]
