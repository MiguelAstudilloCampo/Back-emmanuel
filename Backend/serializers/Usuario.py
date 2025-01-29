from rest_framework import serializers
from Backend.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Añadimos password para serializarlo correctamente

    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {
            'identificacion': {'required': True},
            'nombre': {'required': True},
            'correo': {'required': True},
            'telefono': {'required': True},
            'rol_usuario': {'required': False},
        }

    def create(self, validated_data):
        # Encriptar la contraseña antes de guardar
        password = validated_data.pop('password', None)  # Eliminar 'password' del diccionario de validated_data
        user = Usuario.objects.create(**validated_data)  # Crear el usuario sin la contraseña
        if password:
            user.set_password(password)  # Establecer la contraseña encriptada
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance = super().update(instance, validated_data)
        if password:
            instance.set_password(password)  # Establecer la nueva contraseña encriptada
        instance.save()
        return instance
