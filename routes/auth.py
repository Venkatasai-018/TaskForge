from fastapi import FastAPI,APIRouter, status, Depends, HTTPException, responses
from sqlalchemy.orm import Session
from schema.schema import *
from db.database import get_db
from passlib.context import CryptContext
from models import *
from routes.utils import *
from fastapi.security.oauth2 import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from routes.oauth import *
from routes.utils import *
from typing import Annotated
from jose import JWTError,jwt

db_connected=Annotated[Session,Depends(get_db)]

router = APIRouter(
    
    tags=["auth"]
)




@router.post("/register", status_code=status.HTTP_201_CREATED,response_model=UserOut)
def registration(userdata: Usercreate, db: db_connected):
    userdata.password=pwd_context.hash(userdata.password)
    new_user=User(**userdata.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def create_access_token(username: str, id: int, expires_delta: timedelta | None = None):
    to_encode = {"sub": username, "id": id}

    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": int(expire.timestamp())})  
    print(to_encode)
    try:
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    except JWTError as e:
        print("JWT encoding failed:", e)
        raise


@router.post("/token")
def login_for_access(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    if not verify(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    try:
        access_token = create_access_token(user.username,user.id,timedelta(minutes=10))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Token generation failed: {e}")
    
    return {"access_token": access_token, "token_type": "Bearer"}

async def authenticate(token: Annotated[str,Depends(oauth2_scheme)]):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str=payload.get('sub')
        user_id:int=payload.get('id')
        if user_id is None or username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not find user")
        return {"username":username,"userid":user_id}
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not find user")



