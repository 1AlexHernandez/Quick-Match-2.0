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
from django.contrib.auth import login, authenticate #para autentificar(registrar) el usuario 
from django.contrib.auth.decorators import login_required

def  dasboard(request):
    return render(request,'dasboard/index.html')
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
        form = registroForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']  #cleeaned limpia los datos cuando ya el  usuario se a registrado
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password) #autentificando al usuario
            login(request, user) # usuario ya logueado
            messages.success(request, 'Bienvenido a QUICK MATCH')
            return redirect('principal')

    else:
        form = registroForm()
  
    return render(request,'login/registro.html', {"form": form} )





   
        #En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al ind


#cotizacion
def contact(request): 
    if request.method=='POST':
        subject=request.POST['asunto']
        message=request.POST['mensaje']+ "|Remitente "+ request.POST['email']
        email_from=settings.EMAIL_HOST_USER
        recipent_list=["davidhc1083@gmail.com"]
        send_mail(subject, message, email_from, recipent_list)
        messages.success(request, 'Cotización enviada exitosamente')
        return redirect('contact')
    return render(request, "Principal/contact.html ")

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
                cancha = formulario.save(commit=False) #devolverá un objeto que aún no se ha guardado en la base de datos 
                cancha.user = current_user #para saber quien agrego la cancha
                cancha.save()
                messages.success(request, 'Agregada cancha con exito')
            #data['mensaje'] = 'Su cancha fue guardada exitosamente'
            return redirect ('principal')
    else: #se enviara nuevamente el formulario
            #data["form"] = formulario
        formulario = CanchasForm()
     
      
    return render(request, 'crud/agregar.html',{'formulario': formulario})
    

def Reservas1(request):

    #data = {
    #    'form': CanchaForm()
    #}
    current_user = get_object_or_404(User, pk=request.user.pk) #para lanzar una excepción de tipo Http404 si el registro no se encuentra.
    if request.method == 'POST': #si la peticion viene por un metodo de enviar
            formulario = Reservas1Form(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                cancha = formulario.save(commit=False) #devolverá un objeto que aún no se ha guardado en la base de datos 
                cancha.user = current_user #para saber quien agrego la cancha
                cancha.save()
                messages.success(request, 'Agregada cancha con exito')
            #data['mensaje'] = 'Su cancha fue guardada exitosamente'
            return redirect ('principal')
    else: #se enviara nuevamente el formulario
            #data["form"] = formulario
        formulario = Reservas1Form()
      
    return render(request, 'reserva/reserva1.html',{'formulario': formulario})     

def listar(request):
    cancha = Canchas.objects.all()
    context ={             # diccionario de datos, representa toda la informacion que va hacer enviada al template
        'cancha': cancha   #para enviar la consulta canchas lo envio  a través de un parametro contexto 
    }
    return render(request, 'crud/listar.html', context)

def listar1(request):
    cancha = Reservas.objects.all()
    context ={             # diccionario de datos, representa toda la informacion que va hacer enviada al template
        'cancha': cancha   #para enviar la consulta canchas lo envio  a través de un parametro contexto 
    }
    return render(request, 'crud/reservas.html', context)


def modificar_cancha(request,pk):
    
    cancha = get_object_or_404(Canchas, pk=pk)

    data = {
        'form': CanchasForm(instance=cancha) #va rellenar el formulario
    }
    if request.method == 'POST':
        formulario = CanchasForm(data=request.POST, instance=cancha, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Su cancha está modificada con exito ')
            return redirect(to="perfil")
        data["form"] = formulario    
    return render(request,  'crud/modificar.html', data)


def eliminar_cancha(request, pk):
    Cancha = get_object_or_404(Canchas, pk=pk) #para lanzar una excepción de tipo Http404 si el registro no se encuentra.
    Cancha. delete()
    return redirect(to="listar")


 
def perfil(request, username=None):
    current_user = request.user
    if username and username !=current_user.username:  #revisar el  usuarioel  cual esta logueado o el usuario que quiero visitar
        user = User.objects.get(username=username)
        canchas = user.canchas.all() #llama los modelos

    else:
        canchas = current_user.canchas.all()
        user = current_user
    return render(request, 'principal/perfil.html', {'user':user, 'canchas':canchas})


def editar_Perfil(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user) #solitud de recuperacion de usuario
        p_form = PerfilUpdateForm(request.POST, request.FILES, instance=request.user.perfil) #solicitud de envio de datos del usuario - solicitud de envio de imagenes 
        if u_form.is_valid() and p_form.is_valid(): #se validan
            u_form.save()
            p_form.save()
            return redirect('perfil')
            

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = PerfilUpdateForm()
    context= {'u_form' : u_form, 'p_form':p_form} #diccionario de datos para enviar la data un html
    return render(request, 'principal/EditarPerfil.html', context)



def  index(request):
    return render(request,'index.html')

def  calendar(request):
    return render(request,'admin/calendar.html')

def  cancelacion(request):
    return render(request,'reserva/cancelacion.html')




def  chat(request):
    return render(request,'admin/charts.html') 


def vistas_usuario (request):
    canchas = Canchas.objects.all()
    context={
        'canchas':canchas
    }
    return render (request, 'vista_usuario.html', context)

def canchas_vista (request):
    canchas = Canchas.objects.all()

    context = {
        'canchas': canchas,

    }
    return render (request, 'principal/canchas_vista.html', context)




def perfil_usuarios(request, username=None):
    current_user = request.user
    if username and username !=current_user.username:
        user = User.objects.get(username=username)
        canchas = user.canchas.all()
        reserva = user.reserva.all()
        

    else:
        canchas = current_user.canchas.all()
        reserva = current_user.reserva.all()
        user = current_user
    return render(request, 'principal/perfil_usu.html', {'user':user, 'canchas':canchas, 'reserva':reserva})

class ListadoReservascliente(ListView):
    template_name = 'crud/reservas.html'
    model = Reservas
    paginate_by = 10
    context_object_name = 'object_list'
    fields =   ['fecha_reserva', 'fecha_solicitud',  'cantidad_personas',]


  #-----------------------------------cancha-----------------------------------------------------#

class ListadoCanchas(ListView):
    template_name = '/templates/dasboard/crud/canchas/index.html'
    model = Canchas
    paginate_by = 10
    context_object_name = 'object_list'
    
class CanchasCrear(SuccessMessageMixin, CreateView):
    model =Canchas
    form = Canchas
    fields =  ['user', 'nombre',  'image', 'telefono', 'descripcion', 'ubicacion','precio']

    success_message ='Cancha creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leer') # Redireccionamos a la vista principal 'leer'

class CanchasDetalle (DetailView):
    model =Canchas

class  CanchasActualizar(SuccessMessageMixin,UpdateView):
    model =  Canchas
    form = Canchas
    fields =  ['user','nombre',  'image', 'telefono', 'descripcion', 'ubicacion','precio']
 # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Cancha Actualizada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leer') # Redireccionamos a la vista principal 'leer'
class CanchasEliminar(SuccessMessageMixin, DeleteView): 
    model = Canchas
    form = Canchas
    fields =  ['user','nombre',  'image', 'telefono', 'descripcion', 'ubicacion','precio']
    
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Cancha Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leer' )# Redireccionamos a la vista principal 'leer'
    

     #-----------------------------------Reservas-----------------------------------------------------#

class ListadoReservas(ListView):
    template_name = '/templates/dasboard/reservacrud/index.html'
    model = Reservas
    paginate_by = 10
    context_object_name = 'object_list'
    fields =   ['fecha_reserva', 'fecha_solicitud',  'cantidad_personas']
    
class ReservasCrear(SuccessMessageMixin, CreateView):
    model =Reservas
    form = Reservas
    fields =   ['fecha_reserva', 'fecha_solicitud',  'cantidad_personas']
    success_message ='Cancha creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leer1') # Redireccionamos a la vista principal 'leer'

class ReservasDetalle (DetailView):
    model =Reservas

class  ReservasActualizar(SuccessMessageMixin,UpdateView):
    model = Reservas
    form = Reservas
    fields =   ['fecha_reserva', 'fecha_solicitud',   'cantidad_personas','estado']# Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Cancha Actualizada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leer1') # Redireccionamos a la vista principal 'leer'
class ReservasEliminar(SuccessMessageMixin, DeleteView): 
    model = Reservas
    form = Reservas
    fields =   ['fecha_reserva', 'fecha_solicitud',  'cantidad_personas']
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Municipio Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leer1' )# Redireccionamos a la vista principal 'leer'
    
     #-----------------------------------Horarios-----------------------------------------------------#

class ListadoHorario(ListView):
    template_name = '/templates/dasboard/horarios/index.html'
    model = Horario
    paginate_by = 10
    context_object_name = 'object_list'
    
class HorarioCrear(SuccessMessageMixin, CreateView):
    model =Horario
    form = Horario
    fields =   ['horario_apertura', 'horario', 'dias', 'horario_cierre'] 
    success_message ='Cancha creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leer2') # Redireccionamos a la vista principal 'leer'

class HorarioDetalle (DetailView):
    model =Horario

class  HorarioActualizar(SuccessMessageMixin,UpdateView):
    model = Horario
    form = Horario
    fields =   ['horario_apertura', 'horario', 'dias', 'horario_cierre'] # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Cancha Actualizada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leer2') # Redireccionamos a la vista principal 'leer'
class HorarioEliminar(SuccessMessageMixin, DeleteView): 
    model = Horario
    form = Horario
    fields =   ['horario_apertura', 'horario', 'dias', 'horario_cierre']   
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Cancha Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leer2' )# Redireccionamos a la vista principal 'leer'

     #-----------------------------------estadocancha-----------------------------------------------------#

class ListadoEstado(ListView):
    template_name = '/templates/dasboard/estadocancha/index.html'
    model = Estado
    paginate_by = 10
    context_object_name = 'object_list'
    
class EstadoCrear(SuccessMessageMixin, CreateView):
    model =Estado
    form = Estado
    fields =   ['disponible', 'fuera_de_servicio', 'reservada'] 
    success_message ='Cancha creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leer3') # Redireccionamos a la vista principal 'leer'

class EstadoDetalle (DetailView):
    model =Estado

class  EstadoActualizar(SuccessMessageMixin,UpdateView):
    model = Estado
    form = Estado
    fields =  ['disponible', 'fuera_de_servicio', 'reservada']  # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Cancha Actualizada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leer3') # Redireccionamos a la vista principal 'leer'
class EstadoEliminar(SuccessMessageMixin, DeleteView): 
    model = Estado
    form = Estado
    fields =   ['disponible', 'fuera_de_servicio', 'reservada']    
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Cancha Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leer3' )# Redireccionamos a la vista principal 'leer'



def reservas_usu (request):
    reserva = Reservas.objects.all()
    context = {
        'reserva':reserva,
    }
    return render (request, 'principal/reservas_usu.html', context)


       