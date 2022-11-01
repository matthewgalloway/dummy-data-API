import numpy as np
import pandas as pd

from data_generator.data_creator import DummyDataCreator
from data_generator.data_structures import columns


def test_full():
    "Full end to end test of data creation"
    input_value = 10
    ddc = DummyDataCreator()
    df = ddc.create_dummy_data(columns_dict=columns, iter_number=input_value)

    true_col_names = {}
    for i in columns.keys():
        true_col_names[columns[i]["name"]] = columns[i]["DataType"]

    assert len(df) == input_value
    assert all(df.columns == list(true_col_names.keys()))

    for col_name in true_col_names.keys():
        if true_col_names[col_name] == "Int":
            assert type(df[col_name][0]) == np.int64
        if true_col_names[col_name] == "Date":
            assert type(df[col_name][0]) == pd._libs.tslibs.timestamps.Timestamp
        if true_col_names[col_name] == "Categorical":
            assert type(df[col_name][0]) == str
        if true_col_names[col_name] == "Float":
            assert type(df[col_name][0]) == np.float64

def test_text_corpuse():
    input_value = 10
    ddc = DummyDataCreator()
    df = ddc.create_dummy_data(columns_dict=columns, iter_number=input_value)

    assert isinstance(ddc.text_corpus, list)
    assert len(ddc.text_corpus)>100
    assert isinstance(ddc.text_corpus[10], str)

