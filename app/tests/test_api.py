from fastapi.testclient import TestClient
import pandas as pd
from loguru import logger
import numpy as np

def test_basic(client):
    response = client.get(
        "http://localhost:8001/"
    )
    logger.info(f"response json is {response}")
    assert response.status_code == 200


def test_create_dd(client, test_data)->None:
    dummy_api_json = test_data
    logger.info(f"dummy json is {dummy_api_json}")
    response = client.post(
        "http://localhost:8001/create",
        json=dummy_api_json,
    )

    logger.info(f"response json is {response.json()[:10]}")


    assert response.status_code ==200

    df = pd.DataFrame(response.json())

    columns = dummy_api_json["Columns"]
    number_of_rows = dummy_api_json["NumOfRows"]

    true_col_names = {}
    for i in columns.keys():
        true_col_names[columns[i]["name"]] = columns[i]["DataType"]

    assert len(df) == number_of_rows
    assert all(df.columns == list(true_col_names.keys()))

    for col_name in true_col_names.keys():
        if true_col_names[col_name] == "Int":
            assert type(df[col_name][0]) == np.int64
        if true_col_names[col_name] == "Date":
            assert type(df[col_name][0]) == str
        if true_col_names[col_name] == "Categorical":
            assert type(df[col_name][0]) == str
        if true_col_names[col_name] == "Float":
            assert type(df[col_name][0]) == np.float64