from typing import Generator

import pandas as pd
import pytest
from fastapi.testclient import TestClient
from app.data_package.data_generator.data_structures import dummy_api_json
from app.main import app

@pytest.fixture(scope="module")
def test_data():
    return dummy_api_json

@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides={}