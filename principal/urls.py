#from django.conf.urls import url
#from django.urls import URLPattern

#from .views import(
 
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
from . import views


urlpatterns = [
    
    path('', principal, name="principal"),
    #path('', index, name="principal"),
    path('login1/', LoginView.as_view(template_name='login/login1.html'), name="login1"),
    path('logout/', LogoutView.as_view(template_name='login/login1.html'), name="logout"),
    path('register/', register, name="register"),
    path('Reservas1/', Reservas1, name="reservas1"),
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
   
    path('misreservas/', misreservas, name='misreservas' ),
    path('vercanchas/', vercanchas, name='vercanchas' ),
    #path('vercancha/',vercancha, name='vercancha'),
    
    
 #--------------------------------------------URL CANCHAS ------------------------------------------------------------------------#
    path('Canchas/', ListadoCanchas.as_view(template_name = "dasboard/crud/canchas/index.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una p??gina con los detalles de un Categoria o registro 
    path('Canchas/detalle/<int:pk>', CanchasDetalle.as_view(template_name = "dasboard/crud/canchas/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Canchas/crear', CanchasCrear.as_view(template_name = "dasboard/crud/canchas/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Canchas/editar/<int:pk>', CanchasActualizar.as_view(template_name = "dasboard/crud/canchas/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Canchas/eliminar/<int:pk>', CanchasEliminar.as_view(), name='dasboard/crud/canchas/eliminar.html'),  
    
    #--------------------------------------------URL Reservas ------------------------------------------------------------------------#
    path('Reservas/', ListadoReservas.as_view(template_name = "dasboard/crud/reservacrud/index.html"), name='leer1'),
 
    # La ruta 'detalles' en donde mostraremos una p??gina con los detalles de un Categoria o registro 
    path('Reservas/detalle/<int:pk>', ReservasDetalle.as_view(template_name = "dasboard/crud/reservacrud/detalle.html"), name='detalles1'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Reservas/crear', ReservasCrear.as_view(template_name = "dasboard/crud/reservacrud/crear.html"), name='crear1'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Reservas/editar/<int:pk>', ReservasActualizar.as_view(template_name = "dasboard/crud/reservacrud/actualizar.html"), name='actualizar1'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Reservas/eliminar/<int:pk>', ReservasEliminar.as_view(), name='dasboard/crud/reservacrud/eliminar.html'),  

     #--------------------------------------------URL Horario ------------------------------------------------------------------------#
    path('Horario/', ListadoHorario.as_view(template_name = "dasboard/crud/horarios/index.html"), name='leer2'),
 
    # La ruta 'detalles' en donde mostraremos una p??gina con los detalles de un Categoria o registro 
    path('Horario/detalle/<int:pk>', HorarioDetalle.as_view(template_name = "dasboard/crud/horarios/detalle.html"), name='detalles2'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Horario/crear', HorarioCrear.as_view(template_name = "dasboard/crud/horarios/crear.html"), name='crear2'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Horario/editar/<int:pk>', HorarioActualizar.as_view(template_name = "dasboard/crud/horarios/actualizar.html"), name='actualizar2'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Horario/eliminar/<int:pk>', HorarioEliminar.as_view(), name='dasboard/crud/horarios/eliminar.html'),  

  #--------------------------------------------URL Estado de la cancha ------------------------------------------------------------------------#
    path('Estado/', ListadoEstado.as_view(template_name = "dasboard/crud/estadocancha/index.html"), name='leer3'),
 
    # La ruta 'detalles' en donde mostraremos una p??gina con los detalles de un Categoria o registro 
    path('Estado/detalle/<int:pk>', EstadoDetalle.as_view(template_name = "dasboard/crud/estadocancha/detalle.html"), name='detalles3'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('Estado/crear', EstadoCrear.as_view(template_name = "dasboard/crud/estadocancha/crear.html"), name='crear3'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('Estado/editar/<int:pk>', EstadoActualizar.as_view(template_name = "dasboard/crud/estadocancha/actualizar.html"), name='actualizar3'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('Estado/eliminar/<int:pk>', EstadoEliminar.as_view(), name='dasboard/crud/estadocancha/eliminar.html'),  


    

    #crud import
    #path('formulario/',formularioContacto ), 
    #path('contactar/',contactar ), 
    
 
    # La ruta 'detalles' en donde mostraremos una p??gina con los detalles de un Categoria o registro 
   
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
   
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    
]
    





if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

      #las urls le estamos agregando la media url, cuando alguien ingrese ahi va ser rediregido a la carpeta media_root
