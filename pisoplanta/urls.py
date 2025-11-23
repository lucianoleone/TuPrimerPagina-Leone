from django.urls import path
from pisoplanta.views import (
    home_pisoplanta,
    crear_centro,
    listar_centros,
    EditarCentro,
    EliminarCentro,
    ver_centro,
    about,
)

urlpatterns = [
    path('', home_pisoplanta, name='home_pisoplanta'),
    path('crear-centro/', crear_centro, name='crear_centro'),
    path('listar-centros/', listar_centros, name='listar_centros'),
    path('editar-centro/<int:id>/', EditarCentro.as_view(), name='editar_centro'),
    path('eliminar-centro/ <int:id>/', EliminarCentro.as_view(), name='eliminar_centro'),
    path('ver-centro/<int:id>/', ver_centro, name='ver_centro'),
    path('about/', about, name='about'),

]