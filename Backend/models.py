from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


tipo_rol=[
    ('Administrador','Administrador'),
    ('Usuario','Usuario'),
]


class UsuarioManager(BaseUserManager):
    def create_user(self, identificacion, nombre, correo, telefono, password=None):
        if not identificacion:
            raise ValueError('El usuario debe tener una identificación')

        user = self.model(
            identificacion=identificacion,
            nombre=nombre,
            correo=correo,
            telefono=telefono
        )
        user.set_password(password)  # Encripta la contraseña
        user.save(using=self._db)
        return user

    def create_superuser(self, identificacion, nombre, correo, telefono, password):
        user = self.create_user(identificacion, nombre, correo, telefono, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):  # Ahora hereda de AbstractBaseUser
    identificacion = models.CharField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255) 
    correo = models.CharField(max_length=255) 
    telefono = models.CharField(max_length=255) 
    rol_usuario = models.CharField(max_length=20, choices=tipo_rol)

    objects = UsuarioManager()  # Se usa el Manager personalizado

    USERNAME_FIELD = 'identificacion'
    REQUIRED_FIELDS = ['nombre', 'correo', 'telefono']

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
