from cProfile import label
from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Canchas, perfil, AuthUser,Reservas

class registroForm(UserCreationForm):
    class Meta:
        model = User
        fields =[ 
            'username',
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        
        ]

        

class CanchasForm(forms.ModelForm):
     class  Meta:
        model =  Canchas
        fields = ['nombre',  'image', 'telefono', 'descripcion', 'ubicacion','precio']


class Reservas1Form(forms.ModelForm):
     class  Meta:
        model =  Reservas
        fields = ['fecha_reserva', 'fecha_solicitud', 'cantidad_personas']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'username']

class PerfilUpdateForm(forms.ModelForm):
     class Meta:
        model = perfil
        fields = ['image', 'descripcion']
        


