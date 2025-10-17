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

class Movie(BaseModel):
    id:PyObjectID=Field(alias="_id")
    title:str
    year:Optional[int]=None
    path:Optional[str]=None
    duration:Optional[int]=None
    timestamp:Optional[int]=None
    image:Optional[str]=None
    opened:bool=False
    playing:bool=False

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
    
class UpdateMovie(BaseModel):
    title:Optional[str]=None
    year:Optional[int]=None
    path:Optional[str]=None
    duration:Optional[int]=None
    timestamp:Optional[int]=None
    image:Optional[str]=None
    opened:Optional[bool]=None
    playing:Optional[bool]=None
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}