from django.shortcuts import render
from .models import Producto

def home(request):
    return render(request, "tienda/home.html")

def acerca_de_mi(request):
    return render(request, 'tienda/acerca-de-mi.html')

def productos(request):
    productos = Producto.objects.all()

    return render(
        request,
        'tienda/productos.html',
        {'productos': productos}
    )