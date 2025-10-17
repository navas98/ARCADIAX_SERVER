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
        from_attributes = True                
        validate_by_name = True                 
        json_encoders = {ObjectId: str}


class UpdateDevice(BaseModel):
    name:Optional[str]=None
    ip:Optional[str]=None
    type:Optional[str]=None
    status:Optional[bool]=None
    class Config:
        from_attributes = True                  
        validate_by_name = True                 
        json_encoders = {ObjectId: str}
