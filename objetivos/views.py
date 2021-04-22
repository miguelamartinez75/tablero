from django.http import HttpResponse
from datetime import date

from .utils import calcular


def objetivos_index(request):
    salida = calcular(3, date(2021, 4, 25))

    return HttpResponse(salida)
