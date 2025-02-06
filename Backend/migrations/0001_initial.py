# Generated by Django 5.1.5 on 2025-02-06 04:36

import django.db.models.deletion
import multiselectfield.db.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('identificacion', models.CharField(max_length=255, unique=True)),
                ('nombre', models.CharField(max_length=255)),
                ('correo', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
                ('rol_usuario', models.CharField(choices=[('Administrador', 'Administrador'), ('Usuario', 'Usuario')], max_length=20)),
                ('tipo_sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=20)),
                ('tipo_documento', models.CharField(choices=[('CC', 'CC'), ('CE', 'CE'), ('Otro', 'Otro')], max_length=20)),
                ('edad', models.IntegerField()),
                ('Organización_comunitaria', models.CharField(max_length=255)),
                ('etnia', models.CharField(choices=[('Indígena', 'Indígena'), ('Afrodescendiente', 'Afrodescendiente'), ('Mestizo', 'Mestizo'), ('Campesino', 'Campesino'), ('Otro', 'Otro'), ('Ninguno', 'Ninguno')], max_length=20)),
                ('conflicto_armado', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=20)),
                ('municipio_predio', models.CharField(max_length=255)),
                ('barrio_predio', models.CharField(max_length=255)),
                ('Vitalidad', models.IntegerField()),
                ('grado_estudios', models.CharField(choices=[('Primaria', 'Primaria'), ('Secundaria', 'Secundaria'), ('Técnico/Tecnólogo', 'Técnico/tecnólogo'), ('Profesional', 'Profesional'), ('Posgrado', 'Posgrado')], max_length=20)),
                ('servicio_salud', models.CharField(choices=[('EPS', 'Mensualmente paga a una EPS (régimen contributivo)'), ('SISBEN', 'SISBEN (régimen subsidiado)')], max_length=20)),
                ('ocupacion', models.CharField(choices=[('Hogar', 'Tareas de su propio hogar'), ('Estudiante', 'Estudia tiempo completo'), ('Estudiante_Trabajador', 'Estudia y trabaja'), ('Empleado', 'Empleado(a) (dependiente con vinculación permanente, así sea informal)'), ('Cuenta_Propia', 'Trabajador(a) por cuenta propia (negocio propio formal o informal)'), ('Contratista', 'Contratista o Prestación de servicios (independiente)'), ('Otra', 'Otra ¿cuál?')], max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Predio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacion', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('area_predio', models.CharField(max_length=255)),
                ('cuenca_microcuenca', models.CharField(max_length=255)),
                ('actividades_productivas', multiselectfield.db.fields.MultiSelectField(choices=[('Cultivo de Cafe', 'Cultivo de Cafe'), ('Cultivo de caña panela', 'Cultivo de caña panela'), ('Producción pecuria', 'Producción pecuria'), ('Turismo', 'Turismo'), ('Transformación de productos', 'Transformación de\xa0productos')], max_length=200)),
                ('atractivos_turisticos', multiselectfield.db.fields.MultiSelectField(choices=[('Hospedaje', 'Hospedaje'), ('Camping', 'Zonas de camping'), ('Senderismo', 'Senderismo'), ('Gastronomia', 'Gastronomía local'), ('Avistamiento_Aves', 'Avistamiento de aves'), ('Historia', 'Sitios de importancia histórica'), ('Ciclomontañismo', 'Ciclomontañismo'), ('Bote', 'Paseo en bote'), ('Experiencias', 'Experiencias productivas'), ('Otro', 'Otro ¿cuál?')], max_length=200)),
                ('foto_predio', models.URLField(blank=True, db_column='foto_predio', max_length=300, null=True)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
