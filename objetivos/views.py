from django.http import HttpResponse
from django.shortcuts import render
from datetime import date, datetime
import numpy as np
import plotly.graph_objects as go

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
    marcadores=dict(colors=matrix_transversa[3])
    print(marcadores)
    fig = go.Figure(go.Sunburst(
        labels= matrix_transversa[0],
        parents= matrix_transversa[1],
        values= matrix_transversa[2],
        #maxdepth=3,
        #branchvalues = 'total',
        #branchvalues = "remainder",
        marker=marcadores,
        ))
    fig.show()
        
    fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
    
    return render(request, "plantilla_diagrama.html", {"imagen":fig} )