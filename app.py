from dash import Dash, html, dcc, Input, Output, dash_table
import pandas as pd
from data_package.data_generator.data_creator import DummyDataCreator
from data_package.data_generator.data_structures import columns
from loguru import logger
from front_end.app_layout import layout
from front_end.app_callbacks import get_callbacks
import dash_bootstrap_components as dbc
app = Dash(__name__)
# app.layout = layout
app.layout = html.Div(
    [
        dbc.Row(
            dbc.Col(
                html.Div("A single, half-width column"),
                width={"size": 6, "offset": 3},
            )
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div("The last of three columns"),
                    width={"size": 3, "order": "last", "offset": 1},
                ),
                dbc.Col(
                    html.Div("The first of three columns"),
                    width={"size": 3, "order": 1, "offset": 2},
                ),
                dbc.Col(
                    html.Div("The second of three columns"),
                    width={"size": 3, "order": 5},
                ),
            ]
        ),
    ]
)
get_callbacks(app)





if __name__ == '__main__':
    logger.info('Starting Dash Server')
    app.run_server(debug=True)