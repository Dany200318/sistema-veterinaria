from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_recordatorios, name='lista_recordatorios'),
    path('enviar/', views.enviar_recordatorios, name='enviar_recordatorios'),
]