from fastapi import *
import uvicorn

app=FastAPI()


@app.get("/")
def entry():
    return {"message":"Entry to TaskForge"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)