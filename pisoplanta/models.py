from django.db import models

# Create your models here.
class Centro(models.Model):
    nombre = models.CharField(max_length=30)
    operacion = models.CharField(max_length=30)
    activo = models.BooleanField(default=True)