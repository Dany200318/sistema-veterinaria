from django.urls import path
from . import views

urlpatterns = [
    # Propietarios
    path('propietarios/', views.lista_propietarios, name='lista_propietarios'),
    path('propietarios/crear/', views.crear_propietario, name='crear_propietario'),
    path('propietarios/editar/<int:pk>/', views.editar_propietario, name='editar_propietario'),
    path('propietarios/eliminar/<int:pk>/', views.eliminar_propietario, name='eliminar_propietario'),
    
    # Mascotas
    path('mascotas/', views.lista_mascotas, name='lista_mascotas'),
    path('mascotas/crear/', views.crear_mascota, name='crear_mascota'),
    path('mascotas/editar/<int:pk>/', views.editar_mascota, name='editar_mascota'),
    path('mascotas/eliminar/<int:pk>/', views.eliminar_mascota, name='eliminar_mascota'),
    path('mascotas/detalle/<int:pk>/', views.detalle_mascota, name='detalle_mascota'),
    
    # Historial médico
    path('historial/crear/', views.crear_historial, name='crear_historial'),
    path('historial/crear/<int:mascota_id>/', views.crear_historial, name='crear_historial_mascota'),
    path('historial/editar/<int:pk>/', views.editar_historial, name='editar_historial'),
    path('historial/eliminar/<int:pk>/', views.eliminar_historial, name='eliminar_historial'),
    
    # Vacunas
    path('vacunas/crear/', views.crear_vacuna, name='crear_vacuna'),
    path('vacunas/crear/<int:mascota_id>/', views.crear_vacuna, name='crear_vacuna_mascota'),
    path('vacunas/editar/<int:pk>/', views.editar_vacuna, name='editar_vacuna'),
    path('vacunas/eliminar/<int:pk>/', views.eliminar_vacuna, name='eliminar_vacuna'),
]