from django.db import models

tipo_rol=[
    ('Administrador','Administrador'),
    ('Usuario','Usuario'),
]


class Usuario(models.Model):
    identificacion = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255) 
    correo = models.CharField(max_length=255) 
    telefono = models.CharField(max_length=255) 
    rol_usuario = models.CharField(max_length=20, choices=tipo_rol)
    contraseña = models.CharField(max_length=255) 
   

    def __str__(self):
        return self.nombre
    

class Predio(models.Model):
    nombre = models.CharField(max_length=255)
    edad = models.PositiveIntegerField()
    identificacion = models.CharField(max_length=255) 
    procedencia = models.CharField(max_length=255)
    antiguedad = models.PositiveIntegerField()
    acceso_salud = models.CharField(max_length=255)
    ocupacion = models.CharField(max_length=255)
    cultivo_animales = models.BooleanField(default=False)
    atractivo_ecoturistico = models.BooleanField(default=False)
    colaboracion = models.TextField(null=True, blank=True) 
    fuente_agua = models.CharField(max_length=255)
    foto_predio = models.URLField(max_length=300,db_column='foto_predio', blank=True, null=True)

    def __str__(self):
        return self.nombre
