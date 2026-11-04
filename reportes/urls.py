from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),  # Asegúrate de que esta línea exista
    path('citas/', views.reporte_citas, name='reporte_citas'),
    path('pacientes/', views.reporte_pacientes, name='reporte_pacientes'),
    path('consultas/', views.reporte_consultas, name='reporte_consultas'),
    path('vacunas/', views.reporte_vacunas, name='reporte_vacunas'),
]