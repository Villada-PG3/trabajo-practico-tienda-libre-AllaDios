from django.urls import path
from . import views

app_name = 'tienda'
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.acerca_de_mi, name="acerca_de_mi"),
    path('productos/', views.productos, name='productos'),

]