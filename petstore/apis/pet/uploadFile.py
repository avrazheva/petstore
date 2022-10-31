from __future__ import annotations

import datetime
import pydantic
import typing

from pydantic import BaseModel

from swagger_codegen.api.base import BaseApi
from swagger_codegen.api.request import ApiRequest
from swagger_codegen.api import json
class PetpetIduploadImagepostRequest(BaseModel):
    additionalMetadata: typing.Optional[str]  = None
    file: typing.Optional[bytes]  = None

class ApiResponse(BaseModel):
    code: typing.Optional[int]  = None
    message: typing.Optional[str]  = None
    type: typing.Optional[str]  = None

def make_request(self: BaseApi,

    __request__: PetpetIduploadImagepostRequest,


    petid: int,

) -> ApiResponse:
    """uploads an image"""

    
    body = __request__
    

    m = ApiRequest(
        method="POST",
        path="/v2/pet/{petId}/uploadImage".format(
            
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
    
        "200": {
            
                "application/json": ApiResponse,
            
        },
    
    }, m)