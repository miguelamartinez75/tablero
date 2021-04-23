from django.contrib import admin
from django.urls import path
from .views import objetivos_index, armar_tablero

urlpatterns = [
    path('', objetivos_index, name='objetivos-index'),
    path('tablero/<int:id_obj>/<date_Until_text>', armar_tablero, name='tablero'),
]
