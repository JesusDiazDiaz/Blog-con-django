from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class BaseNombre(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre


class Profesion(BaseNombre):
    class Meta:
        verbose_name = 'Profesion'
        verbose_name_plural = 'Profesiones'


class Categoria(BaseNombre):
    pass


class Autor(User):
    GENERO = (
        ('M', 'MASCULINO'),
        ('F', 'FEMENINO')
    )
    sexo = models.CharField(max_length=1, choices=GENERO)
    sobre_mi = models.TextField()
    profesion = models.ForeignKey(Profesion)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


class Articulo(models.Model):
    STATUS = (
        ('B', 'BORRADOR'),
        ('P', 'PUBLICADO'),
        ('R', 'RETIRADO')
    )
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200, blank=True, null=True)
    categoria = models.ForeignKey(Categoria)
    contenido = models.TextField()
    autor = models.ForeignKey(User)
    fecha_publicacion = models.DateField(auto_now=True, auto_now_add=False)
    status = models.CharField(max_length=1, choices=STATUS)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('articulo-detail', kwargs={'pk': self.pk})
