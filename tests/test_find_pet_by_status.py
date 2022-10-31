"""
Tests which checks GET /findByStatus handler
"""
import pytest
import allure
from utils.pet_util import PetStatus

pytestmark = [allure.suite("GET /findByStatus")]


@pytest.mark.parametrize(
    "pet_status",
    (
        PetStatus.AVAILABLE.value,
        PetStatus.SOLD.value,
        PetStatus.PENDING.value,
        "", "3737", "$@#$!", u'\U0001f604'
    )
)
def test_find_pet_with_valid_status(test_client, pet_status):
    """
    Test checks handler with valid status
    """
    pets = test_client.pet.findPetsByStatus(status=[pet_status])
    assert all([pet.status == pet_status for pet in pets])


@pytest.mark.parametrize(
    "pet_status",
    (
        [],
        [PetStatus.AVAILABLE.value, ""],
        ["", "", "", ""],
        [PetStatus.AVAILABLE.value, PetStatus.SOLD.value, PetStatus.PENDING.value],
        [PetStatus.AVAILABLE.value, PetStatus.AVAILABLE.value]
    )
)
def test_find_pet_with_list_of_statuses(test_client, pet_status):
    """
    Test check different list of statuses
    """
    pets = test_client.pet.findPetsByStatus(status=pet_status)
    assert all([pet.status in pet_status for pet in pets])
