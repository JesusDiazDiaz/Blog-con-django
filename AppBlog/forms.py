from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Autor

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