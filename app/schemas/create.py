from pydantic import BaseModel
from typing import List, Optional, Tuple, Dict



class HouseDataInputSchema(BaseModel):
    Alley: Optional[str]
    BedroomAbvGr: Optional[int]

class DataCreationInputs(BaseModel):
    NumOfRows: Optional[int]
    Columns: Optional[dict]

    class Config:
        schema_extra ={
            "example":{
                        "NumOfRows": 1000,
                        "Columns": {
                            "col1": {
                                "name": "INT_EXAMPLE",
                                "DataType": "Int",
                                "BottomRange": "0",
                                "TopRange": "4",
                            },
                            "col2": {
                                "name": "DATE_EXAMPLE",
                                "DataType": "Date",
                                "StartDate": "01/01/2021",
                                "EndDate": "01/01/2022",
                            },
                            "col3": {
                                "name": "CATEGORICAL_EXAMPLE",
                                "DataType": "Categorical",
                                "Categories": ["CAT1", "CAT2", "CAT3"],
                            },
                            "col4": {
                                "name": "FLOAT_EXAMPLE",
                                "DataType": "Float",
                                "BottomRange": "10000",
                                "TopRange": "0",
                            },
                            "col5": {
                                "name": "FLOAT_EXAMPLE",
                                "DataType": "Float",
                                "BottomRange": "10000",
                                "TopRange": "0",
                            },
                            "col6": {
                                "name": "FLOAT_EXAMPLE",
                                "DataType": "Float",
                                "BottomRange": "10000",
                                "TopRange": "0",
                            },
                            "col7": {
                                "name": "TEXT_EXAMPLE",
                                "DataType": "Text",
                                "MaxNumberOfWords": "15",
                                "MinNumberOfWords": "3",
                            }
                        }
                    }

        }

