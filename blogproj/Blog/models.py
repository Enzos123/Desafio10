from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    activo = models.BooleanField(default=True, verbose_name='Activo')
    creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    class Meta:
        db_table = 'blog_Categoria'


class Articulo(models.Model):
    titulo = models.CharField(max_length=250, unique=True, verbose_name='Título')
    contenido = RichTextField(verbose_name='Contenido')
    imagen = models.ImageField(upload_to='blog/articulos/imagenes', null=True, blank=True, verbose_name='Imagen')
    publicado = models.BooleanField(default=False, verbose_name='Publicado')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, related_name='get_articulos',null=True, blank=True, verbose_name='Categoría')
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='get_articulos', null=True, blank=True, verbose_name='Autor')
    creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    
    class Meta:
        db_table = 'blog_Articulo'

class Acerca(models.Model):
    descripcion = models.CharField(max_length=450, verbose_name='Descripción')
    creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        db_table = 'blog_Acerca'
