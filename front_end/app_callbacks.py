from dash import Dash, html, dcc, Input, Output, dash_table
import pandas as pd
from data_package.data_generator.data_creator import DummyDataCreator
from data_package.data_generator.data_structures import columns
from loguru import logger
from front_end.app_layout import layout
DDC = DummyDataCreator()
df = pd.DataFrame()

def get_callbacks(app):
    @app.callback(
        Output(component_id='sample-table-output', component_property='data'),
        Input(component_id='num-rows-input', component_property='value')
    )
    def update_dashtable(input_value):
        logger.info('Updating dash table')
        sample_df = DDC.create_dummy_data(columns_dict=columns, iter_number=5)
        logger.info(f'Updating dash table with columns {sample_df.columns}')
        return sample_df.to_dict('records')

    @app.callback(
        Output("download-dataframe-xlsx", "data"),
        # Input(component_id='num-rows-input', component_property='value'),
        Input("btn_xlsx", "n_clicks"),
        prevent_initial_call=True,
    )
    def excel_downlaod_button(n_clicks):
        logger.info(f"number of clicks is: {n_clicks}")
        logger.info('Updating dash table')
        df = DDC.create_dummy_data(columns_dict=columns, iter_number=5)
        logger.info(f'Downloading Data')
        return dcc.send_data_frame(df.to_excel, "dummy_data.xlsx", sheet_name="Sheet_name_1")