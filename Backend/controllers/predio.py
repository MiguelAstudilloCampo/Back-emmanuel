from Backend.models import Predio
from Backend.serializers.Predio import PredioSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status 
from decouple import config
import pyrebase

# Configuración de Firebase
config = {
    "apiKey": config("api_key"),
    "authDomain": "senauthenticator.firebaseapp.com",
    "projectId": "senauthenticator",
    "storageBucket": "senauthenticator.appspot.com",
    "messagingSenderId": "488326704430",
    "appId": "1:488326704430:web:4cd223f4443303b9b71ebf",
    "measurementId": "G-GP2WL4P876",
  "service_account": "FireBaseProjecto.json",
  "databaseURL":"https://senauthenticator-default-rtdb.firebaseio.com/"
}

firebase_storage = pyrebase.initialize_app(config)
storage = firebase_storage.storage()

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def predio_controlador(request, pk=None):
    if pk:
        try:
            predio = Predio.objects.get(pk=pk)
        except Predio.DoesNotExist:
            return Response({'error': 'Objeto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = PredioSerializer(predio)
            return Response(serializer.data)

        elif request.method == 'PUT':
            if 'foto_predio' in request.FILES:
                foto = request.FILES['foto_predio']
                file_bytes = foto.read()  # Leer el archivo directamente

                # Subir el archivo a Firebase Storage directamente
                storage_path = f"predios/{foto.name}"
                storage.child(storage_path).put(file_bytes)  # Subir los bytes del archivo
                image_url = storage.child(storage_path).get_url(None)  # Obtener la URL

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
            objetos = Predio.objects.all()
            serializer = PredioSerializer(objetos, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            try:
                if 'foto_predio' in request.FILES:
                    foto = request.FILES['foto_predio']
                    file_bytes = foto.read()  # Leer el archivo directamente

                    # Subir el archivo a Firebase Storage
                    storage_path = f"predios/{foto.name}"
                    storage.child(storage_path).put(file_bytes)  # Subir los bytes del archivo
                    image_url = storage.child(storage_path).get_url(None)  # Obtener la URL

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