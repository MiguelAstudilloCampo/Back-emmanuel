from Backend.models import Predio
from Backend.serializers.Predio import PredioSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import os
from django.conf import settings

# Directorio local para guardar imágenes
MEDIA_ROOT = settings.MEDIA_ROOT  # El directorio base para guardar archivos en tu proyecto Django
MEDIA_URL = settings.MEDIA_URL  # URL base para acceder a los archivos

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def predio_controlador(request, pk=None):
    if pk:
        try:
            predio = Predio.objects.get(pk=pk)
        except Predio.DoesNotExist:
            return Response({'error': 'Predio no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = PredioSerializer(predio)
            return Response(serializer.data)

        elif request.method == 'PUT':
            if 'foto_predio' in request.FILES:
                foto = request.FILES['foto_predio']
                
                # Crear una ruta de archivo única para guardar la imagen
                file_path = os.path.join(MEDIA_ROOT, f"predios/{foto.name}")
                
                # Guardar la imagen localmente
                with open(file_path, 'wb') as f:
                    for chunk in foto.chunks():
                        f.write(chunk)

                # URL de la imagen guardada
                image_url = os.path.join(MEDIA_URL, f"predios/{foto.name}")

                # Actualizar el campo de imagen en la solicitud
                request.data['foto_predio'] = image_url
            
            serializer = PredioSerializer(predio, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            predio.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        if request.method == 'GET':
            predios = Predio.objects.all()
            serializer = PredioSerializer(predios, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            try:
                if 'foto_predio' in request.FILES:
                    foto = request.FILES['foto_predio']
                    
                    # Crear una ruta de archivo única para guardar la imagen
                    file_path = os.path.join(MEDIA_ROOT, f"predios/{foto.name}")
                    
                    # Guardar la imagen localmente
                    with open(file_path, 'wb') as f:
                        for chunk in foto.chunks():
                            f.write(chunk)

                    # URL de la imagen guardada
                    image_url = os.path.join(MEDIA_URL, f"predios/{foto.name}")

                    # Agregar la URL de la imagen al request data
                    request.data['foto_predio'] = image_url

                # Serializar y guardar los datos
                serializer = PredioSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            except Exception as e:
                return Response({'error': f'Error general: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
