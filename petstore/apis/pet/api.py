from __future__ import annotations

from swagger_codegen.api.base import BaseApi

from . import addPet
from . import updatePet
from . import findPetsByStatus
from . import findPetsByTags
from . import getPetById
from . import updatePetWithForm
from . import deletePet
from . import uploadFile
class PetApi(BaseApi):
    addPet = addPet.make_request
    updatePet = updatePet.make_request
    findPetsByStatus = findPetsByStatus.make_request
    findPetsByTags = findPetsByTags.make_request
    getPetById = getPetById.make_request
    updatePetWithForm = updatePetWithForm.make_request
    deletePet = deletePet.make_request
    uploadFile = uploadFile.make_request