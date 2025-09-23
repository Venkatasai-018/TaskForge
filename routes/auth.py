from fastapi import FastAPI,APIRouter, status, Depends, HTTPException, responses
from sqlalchemy.orm import Session
from schema.schema import *
from db.database import get_db
from passlib.context import CryptContext
from models import *
from routes.utils import *


router = APIRouter(
    
    tags=["Authentication"]
)




@router.post("/register", status_code=status.HTTP_201_CREATED,response_model=UserOut)
def registration(userdata: Usercreate, db: Session = Depends(get_db)):
    userdata.password=pwd_context.hash(userdata.password)
    new_user=User(**userdata.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login")
def login(user_cred:Userlogin,db: Session = Depends(get_db)):
    user=db.query(User).filter(User.email == user_cred.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return {"no match"}
    if not verify(user_cred.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return {"invalid"}
    return {"Msg":"sample token"}