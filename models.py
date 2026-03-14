from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email:str
    password:str

class UserResponse(BaseModel):
    username:str
    email:str
    created_at: datetime

    class config:
        from_attributes = True


class PostCreate(BaseModel):
    title: str
    content: str
    category: Optional[str] = None

class PostResponse(BaseModel):
    
    id: int #post ki id
    title: str
    content: str
    category: Optional[str] = None
    user_id: int #user ki id

    class Config:
        from_attributes= True


class Token(BaseModel):
    access_token:str
    token_type:str 

class TokenData(BaseModel):
    id: Optional[int] = None



