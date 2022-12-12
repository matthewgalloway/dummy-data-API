from fastapi import APIRouter, Response
from app.data_package.data_generator.data_creator import DummyDataCreator
from loguru import logger
from typing import Any
from fastapi.encoders import jsonable_encoder
import ast
from app.schemas.create import DataCreationInputs
api_router = APIRouter()
ddc = DummyDataCreator()

@api_router.get("/create", status_code=200)
async def create(input_data: DataCreationInputs) -> Any:
    """
    Creates dummy data based on an input json
    """
    input_data_json = ast.literal_eval(input_data)
    logger.info(f"data type is {type(input_data_json)}")
    logger.info(f"Creating dummy data based on inputs: {input_data}")

    dummy_data_df = ddc.create_dummy_data(input_data_json)

    logger.info(f"Head of Dummy data creates: {dummy_data_df.head()} ")

    return Response(dummy_data_df.to_json(orient="records"), media_type="application/json")