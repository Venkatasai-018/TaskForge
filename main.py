from fastapi import FastAPI, Depends
import uvicorn
from sqlalchemy.orm import Session
from db.database import engine, get_db
import models
from routes import auth



models.Base.metadata.create_all(engine)


app = FastAPI()
app.include_router(auth.router) 


 

@app.get("/")
def entry():
    print("Auth router:", auth.router)
    return {"message": auth.router}

@app.get("/getrouter")
def entry():
    print("Auth router:", auth.router)
    return {"message": auth.router}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
