from django.contrib import admin

# Register your models here.
#from .models import Blog
#from . import models
from .models import Articulo
from .models import Categoria
from .models import Acerca

admin.site.register(Articulo)
admin.site.register(Categoria)
admin.site.register(Acerca)