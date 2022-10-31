"""
Tests checks DELETE /pet/{id} handler
"""
import allure
import pytest
import requests
from swagger_codegen.api.exceptions import ErrorApiResponse

pytestmark = [allure.suite("DELETE /pet/{id}")]


def test_delete_existing_pet(test_client, test_pet):
    """
    Test check positive deleting pet flow
    """
    with allure.step("Add pet"):
        pet = test_client.pet.addPet(test_pet)
    with allure.step("Delete pet"):
        test_client.pet.deletePet(petid=pet.id)
    with allure.step("Try to get deleted pet"):
        try:
            test_client.pet.getPetById(petid=pet.id)
        except ErrorApiResponse as e:
            assert e.response.status_code == 404
            assert e.response.body.get('message') == "Pet not found"


def test_delete_pet_two_times(test_client, test_pet, main_host):
    """
    Test checks deleting of non-existent pet
    """
    with allure.step("Add pet"):
        pet = test_client.pet.addPet(test_pet)
    with allure.step("Delete pet"):
        test_client.pet.deletePet(petid=pet.id)
    with allure.step("Delete pet again ang handle error"):
        response = requests.delete(url=f"{main_host}/v2/pet/{pet.id}")
        assert response.status_code == 404
        assert response.reason == "Not Found"


@pytest.mark.parametrize(
    "pet_id",
    ("test", "$@#$!", u'\U0001f604')
)
def test_delete_pet_with_unknown_id(test_client, pet_id):
    """
    Test invalid pet it string data
    """
    try:
        test_client.pet.deletePet(petid=pet_id)
    except ErrorApiResponse as e:
        assert e.response.status_code == 404
        assert e.response.body.get("type") == "unknown"


@pytest.mark.parametrize(
    "pet_id",
    (0, -1)
)
def test_delete_pet_with_invalid_int_id(test_client, pet_id, main_host):
    """
    Test invalid pet id
    """
    response = requests.delete(url=f"{main_host}/v2/pet/{pet_id}")
    assert response.status_code == 404
    assert response.reason == "Not Found"
