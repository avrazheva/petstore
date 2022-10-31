"""
Tests for checking POST /pet handler for adding a new pet
"""

import pytest
import allure
from utils.random_simple_data_util import generate_random_string, generate_random_image_url
from utils.pet_util import create_pet_tag, PetStatus
from swagger_codegen.api.exceptions import ErrorApiResponse


pytestmark = [allure.suite("POST /pet")]


def test_add_pet_with_mandatory_fields(test_client, simple_test_pet):
    """
    Add pet with minimum valid data
    """
    pet = test_client.pet.addPet(simple_test_pet)
    assert pet.name == simple_test_pet.name
    assert pet.photoUrls == simple_test_pet.photoUrls
    assert pet.id is not None


def test_add_pet_with_full_data(test_client, test_pet):
    """
    Add pet with all data fields
    """
    pet = test_client.pet.addPet(test_pet)
    assert pet.name == test_pet.name
    assert pet.photoUrls == test_pet.photoUrls
    assert pet.tags == test_pet.tags
    assert pet.status == test_pet.status
    assert pet.id is not None


def test_add_same_pet_several_time(test_client, simple_test_pet):
    """
    Test several pet adding with the same data
    """
    pet_ids = []
    pet = test_client.pet.addPet(simple_test_pet)
    pet_ids.append(pet.id)
    for i in range(0, 20):
        pet = test_client.pet.addPet(simple_test_pet)
        assert pet.name == simple_test_pet.name
        assert pet.photoUrls == simple_test_pet.photoUrls
        assert pet.id not in pet_ids
        pet_ids.append(pet.id)


@pytest.mark.parametrize(
    "pet_id", [0, -1, None]
)
def test_add_pet_with_invalid_id(test_client, simple_test_pet, pet_id):
    """
    Test adding Pet with invalid id value
    """
    simple_test_pet.id = pet_id
    pet = test_client.pet.addPet(simple_test_pet)
    assert pet.id > 0


@pytest.mark.parametrize(
    "pet_name", ["", "3737", "$@#$!", u'\U0001f604']
)
def test_add_pet_with_specific_name(test_client, simple_test_pet, pet_name):
    simple_test_pet.name = pet_name
    pet = test_client.pet.addPet(simple_test_pet)
    assert pet.name == pet_name
    assert pet.photoUrls == simple_test_pet.photoUrls
    assert pet.id is not None


@pytest.mark.parametrize(
    "pet_photo",
    (
            [],
            [generate_random_image_url()],
            [generate_random_string()],
            [generate_random_image_url(), generate_random_image_url(), generate_random_string()],
            [generate_random_image_url(ext="png"), generate_random_image_url(ext="bmp"),
             generate_random_image_url(ext="gif"), generate_random_image_url(ext="tiff")]
    )
)
def test_add_pet_with_different_photo(test_client, simple_test_pet, pet_photo):
    """
    Test which checks different image url formats
    """
    simple_test_pet.photoUrls = pet_photo
    pet = test_client.pet.addPet(simple_test_pet)
    assert pet.name == simple_test_pet.name
    assert pet.photoUrls == pet_photo
    assert pet.id is not None


@pytest.mark.parametrize(
    "pet_tags",
    (
        [],
        [create_pet_tag(tag_id=0)],
        [create_pet_tag(tag_id=-1)],
        [create_pet_tag(tag_name="")],
        [create_pet_tag(tag_name="354")],
        [create_pet_tag(tag_name="%#")],
        [create_pet_tag(tag_name=u'\U0001f604')],
        [create_pet_tag(), create_pet_tag()]
    )
)
def test_add_pet_tag_data(test_client, simple_test_pet, pet_tags):
    """
    Test which checks tag validation since it uses in search handler
    """
    simple_test_pet.tags = pet_tags
    pet = test_client.pet.addPet(simple_test_pet)
    assert pet.name == simple_test_pet.name
    assert pet.photoUrls == simple_test_pet.photoUrls
    assert pet.tags == pet_tags
    assert pet.id is not None


@pytest.mark.parametrize(
    "pet_status",
    [
            "", "3737", "$@#$!", u'\U0001f604',
            PetStatus.SOLD.value, PetStatus.PENDING.value, PetStatus.AVAILABLE.value
    ]
)
def test_add_pet_status_data(test_client, simple_test_pet, pet_status):
    """
    Test which checks status validation since it uses in search handler
    """
    simple_test_pet.status = pet_status
    pet = test_client.pet.addPet(simple_test_pet)
    assert pet.name == simple_test_pet.name
    assert pet.photoUrls == simple_test_pet.photoUrls
    assert pet.status == pet_status
    assert pet.id is not None


@pytest.mark.parametrize(
    "invalid_name, invalid_photo",
    (["", ""], [[], []])
)
def test_add_pet_with_incorrect_data_type(test_client, simple_test_pet, invalid_name, invalid_photo):
    """
    Test invalid data types for mandatory fields
    """
    simple_test_pet.photoUrls = invalid_name
    simple_test_pet.name = invalid_photo
    try:
        test_client.pet.addPet(simple_test_pet)
    except ErrorApiResponse as e:
        assert e.response.status_code == 500
        assert e.response.body.get("message") == "something bad happened"
