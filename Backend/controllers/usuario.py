from rest_framework_simplejwt.tokens import RefreshToken
from Backend.models import Usuario
from Backend.serializers.Usuario import UsuarioSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def usuario_controlador(request, pk=None):
    # Si existe la pk se manejan los métodos GET, PUT, DELETE
    if pk:
        try:
            usuario = Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if request.method == 'GET':
            try:
                serializer = UsuarioSerializer(usuario)
                return Response(serializer.data)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if request.method == 'PUT':
            try:
                serializer = UsuarioSerializer(usuario, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if request.method == 'DELETE':
            try:
                usuario.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        if request.method == 'GET':
            try:
                usuarios = Usuario.objects.all()
                serializer = UsuarioSerializer(usuarios, many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        elif request.method == 'POST':
            try:
                serializer = UsuarioSerializer(data=request.data)

                if serializer.is_valid():
                    # No es necesario encriptar la contraseña manualmente, el serializador lo hará
                    user = serializer.save()

                    # Generar los tokens JWT
                    refresh = RefreshToken.for_user(user)
                    access_token = str(refresh.access_token)

                    response = Response({'usuario': serializer.data}, status=status.HTTP_201_CREATED)

                    # Guardar los tokens en las cookies
                    response.set_cookie(
                        key='jwt-access',
                        value=access_token,
                        httponly=True,
                        secure=True,  
                        samesite='None'  
                    )

                    return response

                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def inicio_sesion(request):
    try:
        user = Usuario.objects.get(identificacion=request.data['identificacion'])
        
        # Verificar la contraseña
        if not user.check_password(request.data['password']):  # Cambié 'contraseña' por 'password'
            return Response({'error': 'Usuario o Contraseña no son correctos, vuelva a intentar.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Generar los tokens JWT (access y refresh)
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        serializer = UsuarioSerializer(instance=user)
        response = Response({'user': serializer.data, 'token': access_token}, status=status.HTTP_200_OK)

        # Guardar los tokens en las cookies
        response.set_cookie(
            key='jwt-access',
            value=access_token,
            httponly=True,
            secure=True,  
            samesite='None',
        )

        return response

    except Usuario.DoesNotExist:
        return Response({'error': 'Debe registrarse.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def validarToken(request):
    return Response({'message': 'Usuario autenticado correctamente'}, status=200)
