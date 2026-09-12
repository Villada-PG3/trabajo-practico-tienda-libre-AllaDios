from datetime import date
from django.shortcuts import render
from .models import Producto

def home(request):
    productos_destacados = Producto.objects.order_by('-fecha_de_creacion')[:3]
    context = {
        'titulo': 'Productos de la semana',
        'subtitulo': 'Ofertas especiales para ti',
        'nombre_usuario': 'ana',
        'fecha_hoy': date,
        'productos': productos_destacados,
        'usuario_logueado': True,
    }
    return render(request, 'tienda/home.html', context)

def acerca_de_mi(request):
    return render(request, 'tienda/acerca-de-mi.html')

def catalogo(request):
    productos = Producto.objects.all()

    return render(
        request,
        'tienda/catalogo.html',
        {'productos': productos}
    )