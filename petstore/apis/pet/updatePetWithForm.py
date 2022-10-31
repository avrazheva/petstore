from __future__ import annotations

import datetime
import typing

import pydantic
from pydantic import BaseModel
from swagger_codegen.api import json
from swagger_codegen.api.base import BaseApi
from swagger_codegen.api.request import ApiRequest


class PetpetIdpostRequest(BaseModel):
    name: typing.Optional[str]  = None
    status: typing.Optional[str]  = None

def make_request(self: BaseApi,

    __request__: PetpetIdpostRequest,


    petid: int,

) -> None:
    """Updates a pet in the store with form data"""

    
    body = __request__
    

    m = ApiRequest(
        method="POST",
        path="/v2/pet/{petId}".format(
            
                petId=petid,
            
        ),
        content_type="application/json",
        body=body,
        headers=self._only_provided({
        }),
        query_params=self._only_provided({
        }),
        cookies=self._only_provided({
        }),
    )
    return self.make_request({
    
        "405": {
            
                "default": None,
            
        },
    
    }, m)