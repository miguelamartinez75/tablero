from .models import Indicador, Tipofuncion, Data, Parametro
from math import *
import numexpr


def calcular(indic):
    indicador = Indicador.objects.get(pk=indic)
    tipofuncion = Tipofuncion.objects.get(pk=indicador.tipofuncion_id)
    parametro = Parametro.objects.filter(indicador_id=indicador.id).last()
    data = Data.objects.filter(indicador_id=indicador.id).last()
    x = data.value
    a = parametro.parama
    b = parametro.paramb
    c = parametro.paramc
    mifuncion = tipofuncion.func
    # salida = eval(mifuncion)
    salida = numexpr.evaluate(mifuncion).item()
    return salida


def calc(indic, value):
    indicador = Indicador.objects.get(pk=indic)
    tipofuncion = Tipofuncion.objects.get(pk=indicador.tipofuncion_id)
    parametro = Parametro.objects.filter(indicador_id=indicador.id).last()
    x = value
    a = parametro.parama
    b = parametro.paramb
    c = parametro.paramc
    mifuncion = tipofuncion.func
    # salida = eval(mifuncion)
    salida = numexpr.evaluate(mifuncion).item()
    return salida
