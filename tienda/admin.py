from django.contrib import admin

# Register your models here.
from tienda.models import Producto, Categoria

admin.site.register(Producto)
admin.site.register(Categoria)