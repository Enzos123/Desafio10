from typing import Any, Dict, Iterable, Optional, Tuple
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify

#acercade

class Acerca(models.Model):
    descripcion = models.CharField(max_length=450,verbose_name='Descripcion')
    creacion = models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')
    actualizacion = models.DateField(auto_now=True, verbose_name='Fecha de actualizacion')


    class Meta:
        verbose_name='Acerca de'
        verbose_name_plural='Acerca de nosotros'
        ordering = ['-creacion']
    

    def __str__(self):
        return self.descripcion

#red

class Red(models.Model):
    nombre = models.CharField(max_length=150,verbose_name='Red social')
    url = models.URLField(max_length=300,null=True, blank=True, verbose_name='Enlace')
    icono = models.CharField(max_length=150, null=True, blank=True, verbose_name='Icono')
    creacion = models.DateField(auto_now_add=True,verbose_name='Fecha de creacion')
    actualizacion = models.DateField(auto_now=True, verbose_name='Fecha de actualizacion')


    class Meta:
        verbose_name = 'Red social'
        verbose_name_plural = 'Redes sociales'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    
#categoria 

class Categoria(models.Model):
    nombre = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    slug = models.SlugField()
    activo = models.BooleanField(default=True, verbose_name='Activo')
    creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')



    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Categoria, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.nombre
    


#etiqueta 

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    activo = models.BooleanField(default=True, verbose_name='Activo')
    creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')

    
    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ['nombre']

    
    def __str__(self):
        return self.nombre
    

#articulo

class Articulo(models.Model):
    titulo = models.CharField(max_length=350, unique=True, verbose_name='Titulo')
    slug = models.SlugField()
    bajada = models.CharField(max_length=300, verbose_name='Bajada')
    contenido = RichTextField(verbose_name='Contenido')
    imagen = models.ImageField(upload_to='blog/articulos/imagenes', null=True, blank=True, verbose_name='Imagen')
    publicado = models.BooleanField(default=True, verbose_name='Publicado')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, related_name='get_articulo', null=True, blank=True, verbose_name='Categoria')
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='get_articulo', null=True, blank=True, verbose_name='Autor')
    etiqueta = models.ManyToManyField(Etiqueta, verbose_name='Etiqueta')
    creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')




    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-creacion']

    
    def delete(self, using = None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        return super().delete()
    


    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Articulo, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo