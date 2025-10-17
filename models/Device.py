from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId


class PyObjectID(ObjectId):
    @classmethod
    def __get_validators__(cls):  # doble guion bajo
        yield cls.validate

    @classmethod
    def validate(cls, v, field=None):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return str(v)

class Device(BaseModel):
    id:PyObjectID=Field(alias="_id")
    name:str
    ip:str
    type:Optional[str]=None
    status:bool=False
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}

class UpdateDevice(BaseModel):
    name:Optional[str]=None
    ip:Optional[str]=None
    type:Optional[str]=None
    status:Optional[bool]=None
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
