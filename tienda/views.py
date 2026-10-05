from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views.generic import ListView, TemplateView

from .models import Producto


class HomeView(TemplateView):
    template_name = "tienda/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "titulo": "Productos de la semana",
            "subtitulo": "Ofertas especiales para ti",
            "nombre_usuario": "ana",
            "fecha_hoy": timezone.localdate(),
            "productos": Producto.objects.order_by("-fecha_de_creacion")[:3],
            "usuario_logueado": True,
        })
        return context


class CatalogoView(ListView):
    model = Producto
    template_name = "tienda/catalogo.html"
    context_object_name = "productos"
    ordering = ["-fecha_de_creacion"]


def acerca_de_mi(request):
    return render(request, 'tienda/acerca-de-mi.html')


def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    return render(
        request,
        'tienda/detalle.html',
        {'producto':producto}
    )