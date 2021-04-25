#from _typeshed import NoneType
from django.db.models.fields import NullBooleanField
from .models import Indicador, Tipofuncion, Data, Parametro, Objetivo
from math import *
import numexpr



def calcular(indic, date_Until):
    #Calcula el valor del indicador a la ultima fecha disponible anterior a date_Until
    print(indic)
    
    if 1 == 1:
    #try:
        indicador = Indicador.objects.get(id=indic)
        tipofuncion = Tipofuncion.objects.get(id=indicador.tipofuncion_id)
        parametro = Parametro.objects.filter(vigencia__lte = date_Until, indicador_id=indicador.id).last()    
        #parametro = Parametro.objects.filter(indicador_id=indicador.id).last()
        data = Data.objects.filter(datetime__lte = date_Until, indicador_id=indicador.id).last()
        #data = Data.objects.filter(indicador_id=indicador.id).last()
        x = data.value
        a = parametro.parama
        b = parametro.paramb
        c = parametro.paramc
        mifuncion = tipofuncion.func
        # salida = eval(mifuncion)
        print(mifuncion)
        salida = numexpr.evaluate(mifuncion).item()
        return salida
    #except:
    #    return None

def calcular_objetivo(id_obj, date_Until, matrix):
    matrix_objetivos=matrix

    #Primero verificar si tiene indicador asociado
    objetivo = Objetivo.objects.get(pk=id_obj)
    if objetivo.tiene_indicador:
        #print(objetivo.id_indicador)
        co = calcular(objetivo.id_indicador.id, date_Until)
        #print(co)
        if co == None:
            color = "#D4D4D4"
        else:
            if co >= 0.75:
                color = "#00FF00"
            else:
                if co >= 0.5:
                    color = "#FFFF00"
                else:
                    if co >= 0.25:
                        color = "#FF8800"
                    else:
                        color = "#FF0000"
        elem = [objetivo.codigo, objetivo.parent.codigo, 1, color, co]
    else:
        #Averiguar los hijos de objetivo
        hijos = objetivo.get_children()
        if hijos:
            prefer_acum = 0
            valor_acum = 0
            for hijo in hijos:
                Item = calcular_objetivo(hijo.id, date_Until, matrix_objetivos)
                if Item[-1][4]:
                    prefer_acum = prefer_acum + hijo.prefer
                    valor_acum = valor_acum + Item[-1][4] * hijo.prefer
            
            try:
                valor = valor_acum / prefer_acum
            except:
                valor = None

            if valor == None:
                    color = "#D4D4D4"
            else:
                if valor >= 0.75:
                    color = "#00FF00"
                else:
                    if valor >= 0.5:
                        color = "#FFFF00"
                    else:
                        if valor >= 0.25:
                            color = "#FF8800"
                        else:
                            color = "#FF0000"

            #Si no tiene padre (en el caso de raiz) dejar una cadena vacia
            if objetivo.parent:
                padre = objetivo.parent.name
            else:
                padre = "Raiz"

            elem = [objetivo.codigo, padre, objetivo.prefer, color, valor]
        else:
            #El objetivo no tiene ni indicador ni hijos .. Dejar en gris
            elem = [objetivo.codigo, objetivo.parent.codigo, 1, "#D4D4D4", None]

    matrix_objetivos.append(elem)
    return matrix_objetivos
                
        

            



    


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
