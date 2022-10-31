import pytest
import allure
from swagger_codegen.api.adapter.requests import RequestsAdapter
from swagger_codegen.api.configuration import Configuration
from petstore.client import new_client
from utils.pet_util import create_pet, create_simple_pet


@pytest.fixture()
def main_host():
    return "https://petstore.swagger.io"


@allure.step("Init test client")
@pytest.fixture()
def test_client(main_host):
    client = new_client(
        adapter=RequestsAdapter(),
        configuration=Configuration(host=main_host)
    )
    yield client


@allure.step("Create test pet with only mandatory fields")
@pytest.fixture()
def simple_test_pet():
    return create_simple_pet()


@allure.step("Create test pet ")
@pytest.fixture()
def test_pet():
    return create_pet()
