from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Articulo, Categoria, Contacto
from .forms import ContactoForm

# Create your views here.


class ArticulosView(ListView):
    model = Articulo
    context_object_name = 'articulo_list'
    paginate_by = 5
    template_name = 'AppBlog/index.html'

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.filter(status='P')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categoria_list'] = Categoria.objects.distinct()
        return context


def articulos_categoria(request, categoria=None):
    context = {
        'articulo_list': Articulo.objects.filter(categoria__nombre=categoria, status='P'),
        'categoria_list': Categoria.objects.distinct()
    }
    return render(request, 'AppBlog/index.html', context)


class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'AppBlog/articulo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['ultimos_articulos'] = self.model.objects.order_by('-fecha_publicacion')[:3]
        return context


class ContactoView(CreateView):
    model = Contacto
    template_name = 'AppBlog/contacto.html'
    form_class = ContactoForm