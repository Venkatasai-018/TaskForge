from fastapi import *
import uvicorn
from sqlalchemy.orm import Session
from db.database import engine,get_db
import models

app=FastAPI()

models.Base.metadata.create_all(engine)

@app.get("/")
def entry(db: Session = Depends(get_db)):
    
    return {"message":"Success"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)