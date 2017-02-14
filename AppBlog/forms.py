from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Autor, Contacto
from django.forms import ModelForm, Textarea

class AutorForm(UserCreationForm):
    class Meta:
        model = Autor
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'profesion',
            'sexo',
            'sobre_mi'
        )


class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        widgets = {
            'pregunta': Textarea(attrs={'rows': 6})
        }