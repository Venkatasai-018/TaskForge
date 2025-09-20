from fastapi import *
import uvicorn

app=APIRouter()




@app.get("/")
def entry():
    return {"message":"Entry to TaskForge"}