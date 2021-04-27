#from _typeshed import NoneType
from django.db.models.fields import NullBooleanField
from .models import Indicador, Tipofuncion, Data, Parametro, Objetivo
from math import *
import numexpr



def calcular(indic, date_Until):
    #Calcula el valor del indicador a la ultima fecha disponible anterior a date_Until
        
    if 1 == 1:
    #try:
        indicador = Indicador.objects.get(id=indic)
        tipofuncion = Tipofuncion.objects.get(id=indicador.tipofuncion_id)
        parametro = Parametro.objects.filter(vigencia__lte = date_Until, indicador_id=indicador.id).last()    
        #parametro = Parametro.objects.filter(indicador_id=indicador.id).last()
        data = Data.objects.filter(datetime__lte = date_Until, indicador_id=indicador.id).last()
        #data = Data.objects.filter(indicador_id=indicador.id).last()
        if data:
            x = data.value
            a = parametro.parama
            b = parametro.paramb
            c = parametro.paramc
            mifuncion = tipofuncion.func
            # salida = eval(mifuncion)
            salida = numexpr.evaluate(mifuncion).item()
            salida = max(0, min(1, salida))
            print(indicador.name, mifuncion, salida)
        else:
            salida = None
            print(indicador.name, " no tiene datos o parametros")
        return salida
    #except:
    #    return None

def calcular_objetivo(id_obj, peso_relativo, date_Until, matrix):
    matrix_objetivos=matrix

    #Primero verificar si tiene indicador asociado
    objetivo = Objetivo.objects.get(pk=id_obj)
    if objetivo.id_indicador:
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
        elem = [objetivo.codigo, objetivo.parent.codigo, peso_relativo, color, co]
    else:
        #Averiguar los hijos de objetivo
        hijos = objetivo.get_children()
        #print("%s tiene %s hijos" %(objetivo.codigo, len(hijos)))
        if hijos:
            suma_pesos = 0
            for hijo in hijos:
                suma_pesos = suma_pesos + hijo.prefer
            

            #prefer_acum = 0
            valor_acum = 0
            for hijo in hijos:
                peso_hijo = peso_relativo * hijo.prefer / suma_pesos
                Item = calcular_objetivo(hijo.id, peso_hijo, date_Until, matrix_objetivos)
                if Item[-1][4] != None:
                    #prefer_acum = prefer_acum + hijo.prefer
                    valor_acum = valor_acum + Item[-1][4] * hijo.prefer / suma_pesos
            
            try:
                valor = valor_acum #/ prefer_acum
                print(objetivo.codigo, valor)
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
                padre = objetivo.parent.codigo
            else:
                padre = "Raiz"

            elem = [objetivo.codigo, padre, 0, color, valor]
        else:
            #El objetivo no tiene ni indicador ni hijos .. Dejar en gris
            elem = [objetivo.codigo, objetivo.parent.codigo, peso_relativo, "#D4D4D4", None]

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
