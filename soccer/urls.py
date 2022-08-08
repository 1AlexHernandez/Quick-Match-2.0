"""soccer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from atexit import register
#from atexit import principal
#from atexit import login
#from atexit import reserva
#from atexit import index
#from atexit import cubo
#from atexit import bombonera
#from atexit import templo
#from principal.views import CanchaActualizar, CanchaCrear, CanchaDetalle, CanchaEliminar, ListadoCancha, formularioContacto,contactar

from django.contrib import admin
from unicodedata import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import  include
from principal.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', principal, name="principal"),
    #path('', index, name="principal"),
    path('login1/', LoginView.as_view(template_name='login/login1.html'), name="login1"),
    path('logout/', LogoutView.as_view(template_name='login/login1.html'), name="logout"),
    path('register/', register, name="register"),
    path('reserva/', reserva, name="reserva"),
    path('contact/', contact, name="contact"),
     path('cancelacion/', cancelacion, name="cancelacion"),
    path('templo/<int:pk>/', templo, name="templo"),
    path('agregar/', agregar, name="agregar"),
    path('listar/', listar, name="listar"),
    path('perfil/', perfil, name='perfil'),
    path('perfil_usuarios/<str:username>/', perfil_usuarios, name='perfil_usuarios'),
    #path('', index, name="index"),
    path('perfil/<str:username>/', perfil, name='perfil'),
    path('editar_Perfil/', editar_Perfil, name="editar_Perfil"),
    path('modificar_cancha/<int:pk>', modificar_cancha, name="modificar_cancha"), #importamos
    path('eliminar_cancha/<int:pk>', eliminar_cancha, name="eliminar_cancha"), #importamos
    path('profile/', profile),
    #path('iindex/', panel),
    path('calendar/', calendar, name="calendar"),
    #path('contact/', contact, name="contact")
    path('charts/', chat),
    path('vistas_usuario/', vistas_usuario, name='vistas_usuario'),
    path('canchas_vista/' , canchas_vista, name='canchas_vista'),
    #path('vercancha/',vercancha, name='vercancha'),



    #crud import
    #path('formulario/',formularioContacto ), 
    #path('contactar/',contactar ), 
    
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
   
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
   
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    
]
    





if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

      #las urls le estamos agregando la media url, cuando alguien ingrese ahi va ser rediregido a la carpeta media_root