from django.contrib import admin
from .models import Centro

@admin.register(Centro)
class CentroAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "operacion", "activo", "preview_img")
    list_filter = ("activo", "operacion")
    search_fields = ("nombre", "operacion")

    # Vista previa de la imagen
    def preview_img(self, obj):
        if obj.imagen:
            return f"<img src='{obj.imagen.url}' width='60' height='60' style='object-fit:cover;border-radius:5px;'/>"
        return "—"
    preview_img.allow_tags = True
    preview_img.short_description = "Imagen"
