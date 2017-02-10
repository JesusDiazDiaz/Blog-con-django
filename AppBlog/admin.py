from django.contrib import admin
from .models import Autor, Profesion, Categoria, Articulo
from .forms import AutorForm


# Register your models here.


@admin.register(Profesion, Categoria)
class BaseRegisterAdmin(admin.ModelAdmin):
    pass


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status')
    ordering = ['titulo']
    date_hierarchy = 'fecha_publicacion'  # navegacion de exploracion basada en fecha
    actions = ['hacer_publico', 'hacer_retiro']
    list_filter = ('status',)
    search_fields = ['titulo']

    # Metodos cambiar estado de articulos
    def hacer_publico(self, request, queryset):
        queryset.update(status='P')

    def hacer_retiro(self, request, queryset):
        queryset.update(status='R')

    # Mensaje descriptivo de Acción
    hacer_retiro.short_description = "Retirar articulos seleccionado/s"
    hacer_publico.short_description = "Publicar articulos seleccionado/s"




@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'profesion']
    form = AutorForm
