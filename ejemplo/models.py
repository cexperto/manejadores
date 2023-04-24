from django.db import models

class EjemploManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(nombre="n1")

# Create your models here.
class Ejemplo(models.Model):
    nombre = models.CharField(max_length=250)    
    tipo = models.CharField(max_length=250)
    precio = models.CharField(max_length=250)

    objects = models.Manager()
    ejemplo_manager = EjemploManager()

    def __str__(self) -> str:
        return self.nombre
    
    
    

# Ejemplo.objects.create(nombre="n1",tipo="t1",precio="200cop")
# Ejemplo.objects.create(nombre="n2",tipo="t1",precio="200cop")
# Ejemplo.objects.create(nombre="n2",tipo="t1",precio="200cop")

# from ejemplo.models import *

# Ejemplo.objects.all()
# Ejemplo.ejemplo_manager.all()

# Ejemplo.objects.get(nombre="n1")

