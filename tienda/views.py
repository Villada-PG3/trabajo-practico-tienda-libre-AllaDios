from django.shortcuts import render, get_object_or_404
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()

    return render(
        request,
        "productos.html",
        {
            "productos": productos
        }
    )


def detalle_producto(request, id):
    producto = get_object_or_404(
        Producto,
        id=id
    )

    return render(
        request,
        "detalle_producto.html",
        {
            "producto": producto
        }
    )