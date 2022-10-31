import random
from enum import Enum

from petstore.apis.pet.addPet import Category, Pet, Tag
from utils import random_simple_data_util as data_util


class PetStatus(Enum):
    AVAILABLE = "available"
    SOLD = "sold"
    PENDING = "pending"

    @classmethod
    def get_random_status(cls):
        return random.choice([PetStatus.AVAILABLE.value, PetStatus.PENDING.value, PetStatus.SOLD.value])


def create_pet_category() -> Category:
    return Category(
        id=data_util.generate_random_digit(),
        name=data_util.generate_random_string()
    )


def create_pet_tag(tag_id: int = None, tag_name: str = None) -> Tag:
    return Tag(
        id=data_util.generate_random_digit() if tag_id is None else tag_id,
        name=data_util.generate_random_string() if tag_name is None else tag_name
    )


def create_pet() -> Pet:
    return Pet(
        id=data_util.generate_random_digit(),
        category=create_pet_category(),
        name=data_util.generate_random_string(),
        photoUrls=[data_util.generate_random_image_url()],
        status=PetStatus.get_random_status(),
        tags=[create_pet_tag()]
    )


def create_simple_pet() -> Pet:
    return Pet(
        name=data_util.generate_random_string(),
        photoUrls=[data_util.generate_random_image_url()],
    )
