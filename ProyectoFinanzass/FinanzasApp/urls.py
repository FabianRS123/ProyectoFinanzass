from django.urls import path
from . import views

urlpatterns = [
    # Ejemplo de ruta
    path('', views.index, name='index'),
]
