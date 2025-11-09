from django.contrib import admin
from django.urls import path, include
from pisoplanta.views import home_pisoplanta, crear_centro, listar_centros
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_pisoplanta),
    path('crear-centro/<nombre>/<operacion>/<activo>/', crear_centro),
    path('listar-centros/', listar_centros),
]
