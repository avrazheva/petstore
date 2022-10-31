"""
Tests checks PUT /pet handler
"""
import allure
import pytest
from utils import random_simple_data_util as data_util
from swagger_codegen.api.exceptions import ErrorApiResponse

pytestmark = [allure.suite("PUT /pet")]


@pytest.mark.parametrize(
    "update_name, update_photo",
    (
        [True, False],
        [False, True],
        [True, True],
        [False, False]
    )
)
def test_update_pet_mandatory_fields(test_client, simple_test_pet, update_name, update_photo):
    """
    Test updating pet with only mandatory fields
    """
    with allure.step("Create new pet"):
        pet = test_client.pet.addPet(simple_test_pet)
    with allure.step("Prepare data to update"):
        new_name = pet.name if not update_name else data_util.generate_random_string()
        new_photo = pet.photoUrls if not update_photo else [data_util.generate_random_image_url()]
        pet.name = new_name
        pet.photoUrls = new_photo
    with allure.step("Update pet"):
        updated_pet = test_client.pet.updatePet(pet)
    with allure.step("Get pet"):
        pet_from_server = test_client.pet.getPetById(petid=pet.id)
        assert updated_pet.id == pet.id == pet_from_server.id
        assert updated_pet.name == new_name == pet_from_server.name
        assert updated_pet.photoUrls == new_photo == pet_from_server.photoUrls


def test_update_all_pet_fields(test_client, simple_test_pet, test_pet):
    """
    Test checks all pet fields update
    """
    with allure.step("Create new pet"):
        pet = test_client.pet.addPet(simple_test_pet)
    with allure.step("Update all fields"):
        test_pet.id = pet.id
        updated_pet = test_client.pet.updatePet(test_pet)
        pet_from_server = test_client.pet.getPetById(petid=pet.id)
        assert updated_pet == test_pet == pet_from_server


def test_update_pet_several_times(test_client, simple_test_pet, test_pet):
    """
    Test checks several times pet update
    """
    with allure.step("Create new pet"):
        pet = test_client.pet.addPet(simple_test_pet)
    with allure.step("Update all fields with the same data"):
        test_pet.id = pet.id
        for i in range(0, 3):
            updated_pet = test_client.pet.updatePet(test_pet)
            pet_from_server = test_client.pet.getPetById(petid=pet.id)
            assert updated_pet == test_pet == pet_from_server
    with allure.step("Update again with the new data fields"):
        new_photo = data_util.generate_random_image_url()
        test_pet.photoUrls = [new_photo]
        updated_pet = test_client.pet.updatePet(test_pet)
        pet_from_server = test_client.pet.getPetById(petid=pet.id)
        assert updated_pet == test_pet == pet_from_server


@pytest.mark.skip("Not handled error on server side")
def test_update_non_existent_pet(test_client, simple_test_pet):
    """
    Test checks error while updating non-existent pet
    """
    with allure.step("Create new pet"):
        pet = test_client.pet.addPet(simple_test_pet)
        pet.id += 1
        pet.name = data_util.generate_random_string()
    with allure.step("Update pet"):
        try:
            test_client.pet.updatePet(pet)
        except ErrorApiResponse as e:
            assert e.response.status_code != 200
