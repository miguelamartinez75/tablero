from django.http import HttpResponse
from django.shortcuts import render
from datetime import date, datetime, timedelta
import numpy as np
import plotly.graph_objects as go

from .utils import calcular, calcular_objetivo, ajustar_cadena





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
    matrix_resultados = calcular_objetivo(id_obj, 100, date_Until, matrix_objetivos)
    
    matrix_transversa = np.array(matrix_resultados).T
    marcadores=dict(colors=matrix_transversa[3])
    
    etiquetas = [] #matrix_transversa[0].copy()
    valores = matrix_transversa[4].copy()
    
    #print (etiquetas, valores)

    for i in range(0, len(valores)):
        #print(i)
        if valores[i] == None:
            etiquetas.append(f"{matrix_transversa[0][i]} <br> <b>Sin datos</b>") 
            #print(etiquetas[i])
        else:
            etiquetas.append(f"{matrix_transversa[0][i]} <br> <b>{int(round(float(valores[i])*100, 0))}</b>")
            #print(etiquetas[i])

    #print(etiquetas)
    

    
    fig = go.Figure(go.Sunburst(
        ids = matrix_transversa[0],
        labels = etiquetas, # + " " + str(matrix_transversa[4]),
        parents = matrix_transversa[1],
        values = matrix_transversa[2],
        maxdepth = 3,
        #branchvalues = 'total',
        #branchvalues = "remainder",
        marker=marcadores,
        hovertemplate='%{label} <br> %{percentEntry:0%}'
        ))
    
        
    fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
    fig.show()

    return render(request, "plantilla_diagrama.html", {"imagen":fig} )



def armar_tablero_doble(request, id_obj, date_until_text, delta_fechas):
    #Rojo = "#FF0000"
    #Naranja = "#FF8800"
    #Amarillo = "#FFFF00"
    #Verde = "#00FF00"
    #Gris = "#D4D4D4"
    print("Primer diagrama")

    matrix_objetivos=[]
    date_until = datetime.strptime(date_until_text, '%d-%m-%Y')
    matrix_resultados = calcular_objetivo(id_obj, 100, date_until, matrix_objetivos)
    
    matrix_transversa = np.array(matrix_resultados).T
    marcadores=dict(colors=matrix_transversa[3])
    
    etiquetas = [] #matrix_transversa[0].copy()
    valores = matrix_transversa[4].copy()
    
    #print (etiquetas, valores)

    for i in range(0, len(valores)):
        #print(i)
        if valores[i] == None:
            etiquetas.append(f"{ajustar_cadena(matrix_transversa[0][i])} <br> <b>Sin datos</b>") 
            #print(etiquetas[i])
        else:
            etiquetas.append(f"{ajustar_cadena(matrix_transversa[0][i])} <br> <b>{int(round(float(valores[i])*100, 0))}</b>")
            #print(etiquetas[i])

    #print(etiquetas)
    
    fig = go.Figure()
    fig.add_trace(go.Sunburst(
        ids = matrix_transversa[0],
        labels = etiquetas, # + " " + str(matrix_transversa[4]),
        parents = matrix_transversa[1],
        values = matrix_transversa[2],
        maxdepth = 4,
        domain=dict(column=0),
        #branchvalues = 'total',
        #branchvalues = "remainder",
        marker=marcadores,
        hovertemplate='%{label} <br> %{percentEntry:0%}'
        ))
    
    print("Segundo diagrama")

    #Borramos listas anteriores
    matrix_objetivos.clear
    matrix_resultados.clear
    etiquetas.clear
    marcadores.clear





    #Aca se calcula el semaforo comparativo, para el trimestre anterior
    matrix_objetivos=[]
    delta = timedelta(days=90)
    date_until = datetime.strptime(date_until_text, '%d-%m-%Y') - delta
    #print(date_until)


    matrix_resultados = calcular_objetivo(id_obj, 100, date_until, matrix_objetivos)
    
    matrix_transversa = np.array(matrix_resultados).T
    marcadores=dict(colors=matrix_transversa[3])
    
    etiquetas = [] #matrix_transversa[0].copy()
    valores = matrix_transversa[4].copy()
    
    #print (etiquetas, valores)

    for i in range(0, len(valores)):
        #print(i)
        if valores[i] == None:
            etiquetas.append(f"{ajustar_cadena(matrix_transversa[0][i])} <br> <b>Sin datos</b>") 
            #print(etiquetas[i])
        else:
            etiquetas.append(f"{ajustar_cadena(matrix_transversa[0][i])} <br> <b>{int(round(float(valores[i])*100, 0))}</b>")
            #print(etiquetas[i])
    
    fig.add_trace(go.Sunburst(
        ids = matrix_transversa[0],
        labels = etiquetas, # + " " + str(matrix_transversa[4]),
        parents = matrix_transversa[1],
        values = matrix_transversa[2],
        maxdepth = 4,
        domain=dict(column=1),
        #branchvalues = 'total',
        #branchvalues = "remainder",
        marker=marcadores,
        hovertemplate='%{label} <br> %{percentEntry:0%}'
        )) 
        
    fig.update_layout(
        grid=dict(columns=2, rows=1), 
        margin = dict(t=0, l=0, r=0, b=0),
        )

    fig.show()

    return render(request, "plantilla_diagrama.html", {"imagen":fig} )