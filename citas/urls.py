from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_cita, name='registrar_cita'),
    path('lista/', views.lista_citas, name='lista_citas'),
    
    # Nuevas URLs para editar y eliminar
    path('editar/<int:pk>/', views.editar_cita, name='editar_cita'),
    path('eliminar/<int:pk>/', views.eliminar_cita, name='eliminar_cita'),
    path('detalle/<int:pk>/', views.detalle_cita, name='detalle_cita'),  # También añadimos una URL para ver detalles
]