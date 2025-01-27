from rest_framework import serializers

from Backend.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {
            'identificacion': {'required': True},
            'nombre': {'required': True},
            'correo': {'required': True},
            'telefono': {'required': True},
            'rol_usuario': {'required': False},
            'contraseña': {'required': True},
        } 