from django.shortcuts import render
from django.views.generic.base import ContextMixin
from django.views.generic import ListView, DetailView, CreateView, View
from .models import Articulo, Categoria, Contacto
from .forms import ContactoForm


# Create your views here.

class BaseContextData(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categoria_list'] = Categoria.objects.distinct()
        return context


class ArticulosView(BaseContextData, ListView):
    model = Articulo
    context_object_name = 'articulo_list'
    paginate_by = 5
    template_name = 'AppBlog/index.html'

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.filter(status='P')


class ArticulosCategoriaView(ArticulosView):
    def get_queryset(self, *args, **kwargs):
        return self.model.objects.filter(categoria__nombre=self.kwargs['categoria'], status='P')


class ArticuloDetailView(BaseContextData, DetailView):
    model = Articulo
    template_name = 'AppBlog/articulo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['ultimos_articulos'] = self.model.objects.order_by('-fecha_publicacion')[:3]
        return context


class ContactoView(BaseContextData, CreateView):
    model = Contacto
    template_name = 'AppBlog/contacto.html'
    form_class = ContactoForm
