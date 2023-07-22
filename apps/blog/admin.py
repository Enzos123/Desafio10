from django.contrib import admin
from . import models

admin.site.site_header = 'Administracion del blog'
admin.site.index_title = 'Panel de control'
admin.site.site_title = 'Blog'


#acerca

class AcercaAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('descripcion', 'creacion')


admin.site.register(models.Acerca, AcercaAdmin)

#redes

class RedAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('nombre', 'url', 'icono')

admin.site.register(models.Red, RedAdmin)



#categoria

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('nombre', 'activo', 'creacion')
    prepopulated_fields = {'slug': ('nombre', )}


admin.site.register(models.Categoria, CategoriaAdmin)



#etiqueta


class EtiquetaAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('nombre', 'activo', 'creacion')


admin.site.register(models.Etiqueta, EtiquetaAdmin)


#articulo

class ArticuloAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('titulo', 'categoria', 'publicado', 'autor', 'creacion', 'actualizacion')
    prepopulated_fields = {'slug': ('titulo', )}
    ordering = ('autor', '-creacion')
    search_fields = ('titulo', 'contenido', 'autor_username', 'categoria_nombre')
    list_filter = ('autor', 'categoria', 'etiqueta')

    def articuloEtiquetas(self, obj):
        return ' - '.join([etiqueta.nombre for etiqueta in obj.etiquetas.all().order_by('nombre')])
    
    articuloEtiquetas.short_description = 'Etiquetas'


admin.site.register(models.Articulo, ArticuloAdmin)
    