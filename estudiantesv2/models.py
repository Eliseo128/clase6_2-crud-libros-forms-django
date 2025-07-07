from django.db import models

# Create your models here.
# estudiantes/models.py
from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
