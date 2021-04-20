from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.tableroObjetivos, name='reporte_principal'),
    url(r'^treewidget/', include('treewidget.urls')),
]
