from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class PyObjectID(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, field=None):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return str(v)  # 👈 convierte ObjectId a str

class Movie(BaseModel):
    id: Optional[PyObjectID] = Field(default=None, alias="_id")
    title: str
    year: Optional[int] = None
    path: Optional[str] = None
    duration: Optional[int] = None
    timestamp: Optional[int] = 0
    image: Optional[str] = None
    opened: bool = False
    playing: bool = False

    class Config:
        from_attributes = True
        validate_by_name = True
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
        from_attributes = True                  # ✅ reemplaza a orm_mode
        validate_by_name = True                 # ✅ reemplaza a allow_population_by_field_name
        json_encoders = {ObjectId: str}
