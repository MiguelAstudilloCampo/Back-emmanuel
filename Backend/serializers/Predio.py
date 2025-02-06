from rest_framework import serializers
from Backend.models import Predio

class PredioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predio
        fields = '__all__'
        extra_kwargs = {
            'localizacion': {'required': True},
            'nombre': {'required': True},
            'area_predio': {'required': True},
            'cuenca_microcuenca': {'required': True},
            'actividades_productivas': {'required': True},
            'atractivos_turisticos': {'required': True},
            'usuario': {'required': True},  # Asegúrate de que el usuario sea requerido si es necesario
            'foto_predio': {'required': True},
        }