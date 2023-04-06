from pydantic import BaseModel
from typing import List,Optional


class CreateCustomersRequest(BaseModel):
    first_name: str
    second_name: str
    addresses: str
    phone: str 
    service: List[int] 
    class Config:
        orm_mode = True

class GetServiceResponse(BaseModel):
    service_id: int
    pay: int
    name: str
    class Config:
        orm_mode = True

class GetPhoneResponse(BaseModel):
    phone: int
    class Config:
        orm_mode = True


class GetCustomersResponse(BaseModel):
    customers_id: int
    first_name: str
    second_name: str
    addresses: str 
    phone: Optional[GetPhoneResponse]
    service: List[GetServiceResponse]

    class Config:
        orm_mode = True  

