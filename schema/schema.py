from pydantic import BaseModel,EmailStr


class Usercreate(BaseModel):
    email: EmailStr
    password: str