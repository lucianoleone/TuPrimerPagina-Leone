from django.db import models

# Create your models here.

#Definidmos el modelo Centro con los campos nombre, operacion y activo, los mismos corresponden a centros de trabajo industriales que realizan una operacion dentro de una linea de montaje
class Centro(models.Model):
    nombre = models.CharField(max_length=30)
    operacion = models.CharField(max_length=30)
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='centros/', null=True, blank=True)

    def __str__(self):
        return self.nombre