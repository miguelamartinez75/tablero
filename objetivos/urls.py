from django.contrib import admin
from django.urls import path
from .views import objetivos_index

urlpatterns = [
    path('', objetivos_index, name='objetivos-index'),
]
