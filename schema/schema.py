from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional


class Usercreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    username: str
    
    class Config:
        orm_mode=True
class Userlogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None