from fastapi import APIRouter, Response
from app.data_package.data_generator.data_creator import DummyDataCreator
from app.config import max_row_error
from loguru import logger
from typing import Any
from fastapi.encoders import jsonable_encoder
import ast
from app.schemas.create import DataCreationInputs
api_router = APIRouter()
ddc = DummyDataCreator()

@api_router.post("/create", status_code=200)
async def create(input_data:DataCreationInputs) -> Any:
    """
    Creates dummy data based on an input json
    """
    logger.info(f"Received incoming data type {type(input_data)} to API {input_data}")
    input_data_json = jsonable_encoder(input_data)

    if  input_data_json["NumOfRows"]>1000:
        return max_row_error

    logger.info(f"Creating dummy data based on inputs: {input_data_json}")

    dummy_data_df = ddc.create_dummy_data(input_data_json)

    logger.info(f"Head of Dummy data creates: {dummy_data_df.head()} ")

    return Response(dummy_data_df.to_json(orient="records", date_format='iso'), media_type="application/json")