from __future__ import annotations

import datetime
import typing

import pydantic
from pydantic import BaseModel
from swagger_codegen.api import json
from swagger_codegen.api.base import BaseApi
from swagger_codegen.api.request import ApiRequest


class User(BaseModel):
    email: typing.Optional[str]  = None
    firstName: typing.Optional[str]  = None
    id: typing.Optional[int]  = None
    lastName: typing.Optional[str]  = None
    password: typing.Optional[str]  = None
    phone: typing.Optional[str]  = None
    username: typing.Optional[str]  = None
    userStatus: typing.Optional[int]  = None

def make_request(self: BaseApi,

    __request__: typing.List[User],


) -> None:
    """Creates list of users with given input array"""

    
    body = __request__
    

    m = ApiRequest(
        method="POST",
        path="/v2/user/createWithList".format(
            
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
    
        "default": {
            
                "default": None,
            
        },
    
    }, m)