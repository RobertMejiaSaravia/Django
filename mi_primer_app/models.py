from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    parentesco = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f'{self.nombre} ({self.edad} anios) - {self.parentesco}'
    
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_semanas = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre