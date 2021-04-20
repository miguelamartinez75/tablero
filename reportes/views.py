from django.shortcuts import render
from .utils import get_plot
from objetivos.models import Data
from objetivos.utils import calc

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np



def tableroObjetivos(request):
    template = "reportes/tablero.html"

    origen = open("sunburst.csv", "r")
    id = []
    label = []
    parent = []
    value = []

    for x in origen:
        linea = x.split(",")
        id.append(linea[0])
        label.append(linea[1].replace(' ', '<br>'))
        parent.append(linea[2])
        value.append(linea[3].replace('\n', ''))

    marcadores=dict(colors=["#ffff00", "#ffff00", "#ff0000", "#ff0000", "#ffff00", "#00ff00", "#ffff00", "#00ff00", "#ffff00", "#ff8800", "#ffff00", "#00ff00", "#ff8800", "#ff8800", "#ffff00", "#00ff00", "#00ff00", "#00ff00", "#00ff00", "#00ff00", "#00ff00", "#00ff00", "#ff8800", "#ff8800", "#ff8800", "#00ff00", "#00ff00", "#ff8800", "#ff0000", "#ff0000", "#00ff00", "#ffff00", "#ff0000", "#ffff00", "#00ff00", "#00ff00", "#ff0000", "#00ff00", "#ffff00", "#ffff00", "#00ff00", "#ffff00", "#ffff00"])
    data = dict(ids = id, parents = parent, value = value, labels = label)
    df = pd.DataFrame.from_dict(data)

    fig = go.Figure()

    # df = pd.read_csv(destino.read())
    # df = pd.read_csv('http://institutogalileo.com.ar/central/sunburst.csv')

    # fig = px.sunburst(
    #     data,
    #     names='character',
    #     labels='label',
    #     parents='parent',
    #     values='value',
    #     maxdepth=3,
    # )

    fig.add_trace(go.Sunburst(
        ids=df.ids,
        labels=df.labels,
        parents=df.parents,
        domain=dict(column=1),
        maxdepth=4,
        marker=marcadores
    ))

    fig.show()

    return render(request, template, {})
