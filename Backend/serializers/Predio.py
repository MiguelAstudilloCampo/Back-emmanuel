from rest_framework import serializers

from Backend.models import Predio


class PredioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predio
        fields = '__all__'
        extra_kwargs = {
            'nombre':{'required':True},
            'edad':{'required':True},
            'identficacion':{'required':True},
            'procedencia':{'required':True},
            'antiguedad':{'required':True},
            'acceso_salud':{'required':True},
            'ocupacion':{'required':True},
            'cultivo_animales':{'required':True},
            'atractivo_ecoturistico':{'required':True},
            'fuente_agua':{'required':True},
            'foto_predio': {'required': True},
        } 