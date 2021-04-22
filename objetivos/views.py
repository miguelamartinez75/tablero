from django.http import HttpResponse

from .utils import calcular


def objetivos_index(request):
    salida = calcular(2)

    return HttpResponse(salida)
