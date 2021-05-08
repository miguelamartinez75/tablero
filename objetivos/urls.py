from django.contrib import admin
from django.urls import path
from .views import objetivos_index, armar_tablero, armar_tablero_doble

urlpatterns = [
    path('', objetivos_index, name='objetivos-index'),
    path('tablero/<int:id_obj>/<date_Until_text>', armar_tablero, name='tablero'),
    path('tablero_doble/<int:id_obj>/<date_Until_text>', armar_tablero_doble, name='tablero_doble'),
]
