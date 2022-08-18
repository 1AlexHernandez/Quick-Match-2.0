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
    #path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('principal/',include(('principal.urls','principal'))),
    path('', principal, name="principal"),
    path('dasboard/', dasboard, name="dasboard"),
    #path('reservas_usu/', reservas_usu, name='reservas_usu' ),
    
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

      #las urls le estamos agregando la media url, cuando alguien ingrese ahi va ser rediregido a la carpeta media_root