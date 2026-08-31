from datetime import date
from django.shortcuts import render
from .models import Producto

def home(request):
    productos_destacados = [
        {'nombre': 'producto 1', 'precio': 10.99},
        {'nombre': 'producto 2', 'precio': 19.99},
        {'nombre': 'producto 3', 'precio': 5.99},
        {'nombre': 'producto 4', 'precio': 29.50},
        {'nombre': 'producto 5', 'precio': 99.00},
        {'nombre': 'producto 6', 'precio': None},
    ]
    context = {
        'titulo': 'Productos de la semana',
        'subtitulo': 'Ofertas especiales para ti',
        'nombre_usuario': 'ana',
        'fecha_hoy': date(2026, 7, 20),
        'productos': productos_destacados,
        'usuario_logueado': True,
    }
    return render(request, 'tienda/home.html', context)

def acerca_de_mi(request):
    return render(request, 'tienda/acerca-de-mi.html')

def productos(request):
    productos = Producto.objects.all()

    return render(
        request,
        'tienda/productos.html',
        {'productos': productos}
    )