from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from multiselectfield import MultiSelectField



tipo_rol=[
    ('Administrador','Administrador'),
    ('Usuario','Usuario'),
]

tipo_documento=[
    ('CC','CC'),
    ('CE','CE'),
    ('Otro','Otro')
]

sexo=[
    ('Masculino','Masculino'),
    ('Femenino','Femenino'),
]

etnia = [
    ('Indígena', 'Indígena'),
    ('Afrodescendiente', 'Afrodescendiente'),
    ('Mestizo', 'Mestizo'),
    ('Campesino', 'Campesino'),
    ('Otro', 'Otro'),
    ('Ninguno', 'Ninguno'),
]

conflicto_armado = [
    ('SI', 'SI'),
    ('NO', 'NO')
]

# Opciones para el grado máximo de estudios culminado
grado_estudios = [
    ('Primaria', 'Primaria'),
    ('Secundaria', 'Secundaria'),
    ('Técnico/Tecnólogo', 'Técnico/tecnólogo'),
    ('Profesional', 'Profesional'),
    ('Posgrado', 'Posgrado'),
]

# Opciones para el acceso a servicios de salud
servicio_salud = [
    ('EPS', 'Mensualmente paga a una EPS (régimen contributivo)'),
    ('SISBEN', 'SISBEN (régimen subsidiado)'),
]

# Opciones para la ocupación principal
ocupacion = [
    ('Hogar', 'Tareas de su propio hogar'),
    ('Estudiante', 'Estudia tiempo completo'),
    ('Estudiante_Trabajador', 'Estudia y trabaja'),
    ('Empleado', 'Empleado(a) (dependiente con vinculación permanente, así sea informal)'),
    ('Cuenta_Propia', 'Trabajador(a) por cuenta propia (negocio propio formal o informal)'),
    ('Contratista', 'Contratista o Prestación de servicios (independiente)'),
    ('Otra', 'Otra ¿cuál?'),
]

actividades_Productivas=[
    ('Cultivo de Cafe','Cultivo de Cafe'),
    ('Cultivo de caña panela','Cultivo de caña panela'),
    ('Producción pecuria','Producción pecuria'),
    ('Turismo','Turismo'),
    ('Transformación de productos','Transformación de productos')
]

atractivos_turisticos = [
    ('Hospedaje', 'Hospedaje'),
    ('Camping', 'Zonas de camping'),
    ('Senderismo', 'Senderismo'),
    ('Gastronomia', 'Gastronomía local'),
    ('Avistamiento_Aves', 'Avistamiento de aves'),
    ('Historia', 'Sitios de importancia histórica'),
    ('Ciclomontañismo', 'Ciclomontañismo'),
    ('Bote', 'Paseo en bote'),
    ('Experiencias', 'Experiencias productivas'),
    ('Otro', 'Otro ¿cuál?'),
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
    tipo_sexo = models.CharField(max_length=20, choices=sexo)
    tipo_documento = models.CharField(max_length=20, choices=tipo_documento)
    edad = models.IntegerField()
    Organización_comunitaria  = models.CharField(max_length=255)
    etnia = models.CharField(max_length=20, choices=etnia)
    conflicto_armado = models.CharField(max_length=20, choices=conflicto_armado)
    municipio_predio = models.CharField(max_length=255) 
    barrio_predio = models.CharField(max_length=255) 
    Vitalidad = models.IntegerField()
    grado_estudios = models.CharField(max_length=20, choices=grado_estudios)
    servicio_salud = models.CharField(max_length=20, choices=servicio_salud)
    ocupacion = models.CharField(max_length=200, choices=ocupacion)
    
    objects = UsuarioManager()  # Se usa el Manager personalizado

    USERNAME_FIELD = 'identificacion'
    REQUIRED_FIELDS = ['nombre', 'correo', 'telefono']

    def __str__(self):
        return self.nombre
    

class Predio(models.Model):
    localizacion = models.CharField(max_length=255)
    nombre =  models.CharField(max_length=255)
    area_predio = models.CharField(max_length=255) 
    cuenca_microcuenca = models.CharField(max_length=255)
    actividades_productivas = MultiSelectField(choices=actividades_Productivas, max_length=200)
    atractivos_turisticos = MultiSelectField(choices=atractivos_turisticos, max_length=200)
    usuario=models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True)
    foto_predio = models.URLField(max_length=300,db_column='foto_predio', blank=True, null=True)

    def __str__(self):
        return self.nombre
    
