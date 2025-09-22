from fastapi import APIRouter,status,Depends,HTTPException,responses
from sqlalchemy.orm import Session    

router=APIRouter(
    tags=["Authentication"]
)


@router.login()
def login():
    return None

