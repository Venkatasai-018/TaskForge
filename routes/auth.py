from fastapi import FastAPI,APIRouter, status, Depends, HTTPException, responses
from sqlalchemy.orm import Session
from schema.schema import *
from db.database import get_db

router = APIRouter(
    
    tags=["Authentication"]
)

@router.post("/register", status_code=status.HTTP_201_CREATED)
def registration(userdata: Usercreate, db: Session = Depends(get_db)):
    return {"message": userdata}
