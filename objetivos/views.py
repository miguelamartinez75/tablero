from django.http import HttpResponse
from datetime import date, datetime
import numpy as np

from .utils import calcular, calcular_objetivo





def objetivos_index(request):
    salida = calcular(3, date(2021, 4, 25))

    return HttpResponse(salida)

def armar_tablero(request, id_obj, date_Until_text):
    #Rojo = "#FF0000"
    #Naranja = "#FF8800"
    #Amarillo = "#FFFF00"
    #Verde = "#00FF00"
    #Gris = "#D4D4D4"

    matrix_objetivos=[]
    date_Until = datetime.strptime(date_Until_text, '%d-%m-%Y')
    matrix_resultados = calcular_objetivo(id_obj, date_Until, matrix_objetivos)
    
    matrix_transversa = np.array(matrix_resultados).T

    return HttpResponse(matrix_transversa)
