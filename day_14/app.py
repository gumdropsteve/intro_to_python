# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)

df = pd.read_parquet('https://github.com/gumdropsteve/datasets/raw/master/airlines.parquet')

t = pd.DataFrame()

t['bool'] = df.ArrDelayBinary.value_counts().index
t['count'] = df.ArrDelayBinary.value_counts()

fig = px.bar(t, x="bool", y='count')

app.layout = html.Div(children=[html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    dcc.Graph(
        id='example-graph2',
        figure=fig,
        style={'width': '60vh', 'height': '60vh'}
    )
                                
])

if __name__ == '__main__':
    app.run_server(debug=True)
