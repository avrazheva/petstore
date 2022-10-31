from __future__ import annotations

import datetime
import typing

import pydantic
from pydantic import BaseModel
from swagger_codegen.api import json
from swagger_codegen.api.base import BaseApi
from swagger_codegen.api.request import ApiRequest


class Tag(BaseModel):
    id: typing.Optional[int]  = None
    name: typing.Optional[str]  = None

class Category(BaseModel):
    id: typing.Optional[int]  = None
    name: typing.Optional[str]  = None

class Pet(BaseModel):
    category: typing.Optional[Category]  = None
    id: typing.Optional[int]  = None
    name: str 
    photoUrls: typing.List[str] 
    status: typing.Optional[str]  = None
    tags: typing.Optional[typing.List[Tag]]  = None

def make_request(self: BaseApi,

    __request__: Pet,


) -> Pet:
    """Update an existing pet"""

    
    body = __request__
    

    m = ApiRequest(
        method="PUT",
        path="/v2/pet".format(
            
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
            
                "application/json": Pet,
            
                "application/xml": Pet,
            
        },
    
        "400": {
            
                "default": None,
            
        },
    
        "404": {
            
                "default": None,
            
        },
    
        "405": {
            
                "default": None,
            
        },
    
    }, m)