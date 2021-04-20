from django.http import HttpResponse

from .utils import calcular


def objetivos_index(request):
    salida = calcular(1)

    return HttpResponse(salida)
