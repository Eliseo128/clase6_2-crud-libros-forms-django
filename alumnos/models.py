# students/models.py

from django.db import models

class Estudiante(models.Model):
    nombre= models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=100)  # NOTA: En un proyecto real, nunca guardes contraseñas en texto plano. Usa el sistema de usuarios de Django.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre