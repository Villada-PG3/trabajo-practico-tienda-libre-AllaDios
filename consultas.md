# Consultas ORM Clase 5

```python
from tienda.models import Categoria, Producto

Producto.objects.all()

Producto.objects.filter(categoria__nombre='Mouses')

Producto.objects.exclude(categoria__nombre='Mouses')

Producto.objects.get(pk=1)

Producto.objects.order_by('-precio')

Producto.objects.filter(nombre__icontains='logitech')

Producto.objects.filter(precio__gt=100000)

Producto.objects.filter(stock__lt=10)

Producto.objects.filter(categoria__nombre__in=['Auriculares', 'Monitores'])

cat = Categoria.objects.get(nombre='Auriculares')
cat.productos.all()

cat_acc = Categoria.objects.get(nombre='Accesorios')
Producto.objects.create(
    categoria=cat_acc,
    nombre='Producto de prueba ORM',
    descripcion='Creado desde la shell',
    precio=25000,
    stock=10
)
```
