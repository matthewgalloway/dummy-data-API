from dash import Dash, html, dcc, Input, Output, dash_table
import pandas as pd
from loguru import logger
import dash_bootstrap_components as dbc

layout = html.Div(children=[
    html.H1(children='Dummy Data for Services Projects'),
    html.Div(children='''
    Data Preview:
'''),
    dash_table.DataTable(
        id='sample-table-output'
    ),
    html.Div(children='''
    Variables for data Creation
'''),
    html.Br(),
    dbc.Row([
        dbc.Col(dcc.Checklist(['Active Column']), width=3),
        dbc.Col(dcc.Input(value='Col Name', type='text')),
        dbc.Col(html.Label('Data Type')),
        dbc.Col(dcc.Dropdown(['Float', 'Date', 'Categorical'], 'Float'), width=3),
    ]),
    html.Br(),
    html.Div([
        "Number of rows of data: ",
        dcc.Input(id='num-rows-input', value=5, type='number')
    ]),
    html.Button("Download csv", id="btn_xlsx"),
    dcc.Download(id="download-dataframe-xlsx"),

])