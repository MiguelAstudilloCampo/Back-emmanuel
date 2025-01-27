from django.urls import path
from Backend.controllers import usuario, predio
# from app_senauthenticator.controllers.autenticacion_facial import AutenticacionFacial
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Usuario
    path('usuario/', usuario.usuario_controlador, name="cont_usuario"),
    path('usuario/<int:pk>/', usuario.usuario_controlador, name="cont_usuario_detail"), 
    path('inicioSesion/', usuario.inicio_sesion, name="inicio_sesion"),
    path('validarToken/', usuario.validarToken, name='protected_view'),
    # Predio
    path('predio/', predio.predio_controlador, name="cont_objeto"),
    path('predio/<int:pk>/', predio.predio_controlador, name="cont_objeto"),
]



if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
