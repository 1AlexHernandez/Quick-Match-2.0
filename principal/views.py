from multiprocessing import context
# librerias del crud
from django.urls import reverse
from webbrowser import get
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect,get_object_or_404
from django.core.mail import send_mail

#importo el modelo de la base de datos de models.py
from .models import *
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 

# Habilitamos los formularios en Django
from django import forms
from django.conf import settings
from .forms import * 

from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
def  templo(request ,pk ):
    canchas = Canchas.objects.filter(pk=pk) #estamos haciendo una consulta de mejor facilidad que filtre los valores por su llave primaria
    context = {     # diccionario de datos, representa toda la informacion que va hacer enviada al template
        'canchas':canchas   #para enviar la consulta canchas lo envio  a través de un parametro contexto 
    }

    return render(request,'principal/templo.html', context) # para enviar la variable contexto

def principal(request):
    canchas = Canchas.objects.all()
    context = {
        'canchas':canchas
    }
    return render(request, 'principal/principal.html', context)

   
def  register(request):
    if request.method =='POST':
        form = registroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Bienvenido a QUICK MATCH')
            return redirect('principal')

    else:
        form = registroForm()
  
    return render(request,'login/registro.html', {"form": form} )





   
        #En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
       
      


def cotizacion(request):
    return render(request, "principal/cotizacion.html")


def  cotizar(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + " / Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["aanacona40@misena.edu.co"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        messages.success(request, f'usuario {username} Bienvenido a QUICK MATCH')
        return render(request, "principal/bombonera.html")  
    return render(request, "principal/cotizacion.html")


def  profile(request):
    return render(request,'admin/profile.html')



def  reserva(request):
    return render(request,'reserva/reserva.html')


 

def agregar(request):

    #data = {
    #    'form': CanchaForm()
    #}
    current_user = get_object_or_404(User, pk=request.user.pk) #para lanzar una excepción de tipo Http404 si el registro no se encuentra.
    if request.method == 'POST': #si la peticion viene por un metodo de enviar
            formulario = CanchasForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                cancha = formulario.save(commit=False)
                cancha.user = current_user
                cancha.save()
                messages.success(request, 'producto cargado')
            #data['mensaje'] = 'Su cancha fue guardada exitosamente'
            return redirect ('principal')
    else:
            #data["form"] = formulario
        formulario = CanchasForm()

        #return render(request, 'app/producto/agregarproducto.html', {'formulario' : formulario})
    return render(request, 'crud/agregar.html',{'formulario': formulario})

def listar(request):
    cancha = Canchas.objects.all()
    context ={             # diccionario de datos, representa toda la informacion que va hacer enviada al template
        'cancha': cancha
    }
    return render(request, 'crud/listar.html', context)


def modificar_cancha(request,pk):
    
    cancha = get_object_or_404(Canchas, pk=pk)

    data = {
        'form': CanchasForm(instance=cancha)
    }
    if request.method == 'POST':
        formulario = CanchasForm(data=request.POST, instance=cancha, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="perfil")
        data["form"] = formulario    
    return render(request,  'crud/modificar.html', data)


def eliminar_cancha(request, pk):
    Cancha = get_object_or_404(Canchas, pk=pk) #para lanzar una excepción de tipo Http404 si el registro no se encuentra.
    Cancha. delete()
    return redirect(to="listar")


 
def perfil(request, username=None):
    current_user = request.user
    if username and username !=current_user.username:
        user = User.objects.get(username=username)
        canchas = user.canchas.all()

    else:
        canchas = current_user.canchas.all()
        user = current_user
    return render(request, 'principal/perfil.html', {'user':user, 'canchas':canchas})


def editar_Perfil(request):
    if request.method == 'POST':
        u_formulario = UserUpdateForm(request.POST, instance=request.user)
        p_formulario = PerfilUpdateForm(request.POST, request.FILES, instance=request.user.perfil)
        if u_formulario.is_valid() and p_formulario.is_valid():
            u_formulario.save()
            p_formulario.save()
            return redirect('perfil')
            

    else:
        u_formulario = UserUpdateForm(instance=request.user)
        p_formulario = PerfilUpdateForm()
    context= {'u_formulario' : u_formulario, 'p_formulario':p_formulario} #diccionario de datos para enviar la data un html
    return render(request, 'principal/EditarPerfil.html', context)



def  index(request):
    return render(request,'index.html')

def  calendar(request):
    return render(request,'admin/calendar.html')

def  cancelacion(request):
    return render(request,'reserva/cancelacion.html')


def  contact(request):
    return render(request,'admin/contact.html') 

def  chat(request):
    return render(request,'admin/charts.html') 


def vistas_usuario (request):
    canchas = Cancha.objects.all()
    context={
        'canchas':canchas
    }
    return render (request, 'vista_usuario.html', context)

def perfil_usuarios(request, username=None):
    current_user = request.user
    if username and username !=current_user.username:
        user = User.objects.get(username=username)
        canchas = user.canchas.all()

    else:
        canchas = current_user.canchas.all()
        user = current_user
    return render(request, 'principal/perfil.html', {'user':user, 'canchas':canchas})

