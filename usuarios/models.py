from django.db import models

class PerfilUsuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
