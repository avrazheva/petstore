from __future__ import annotations

import datetime
import typing

import pydantic
from pydantic import BaseModel
from swagger_codegen.api import json
from swagger_codegen.api.base import BaseApi
from swagger_codegen.api.request import ApiRequest


class Order(BaseModel):
    complete: bool  = False
    id: typing.Optional[int]  = None
    petId: typing.Optional[int]  = None
    quantity: typing.Optional[int]  = None
    shipDate: typing.Optional[datetime.datetime]  = None
    status: typing.Optional[str]  = None

def make_request(self: BaseApi,

    __request__: Order,


) -> Order:
    """Place an order for a pet"""

    
    body = __request__
    

    m = ApiRequest(
        method="POST",
        path="/v2/store/order".format(
            
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
            
                "application/json": Order,
            
                "application/xml": Order,
            
        },
    
        "400": {
            
                "default": None,
            
        },
    
    }, m)