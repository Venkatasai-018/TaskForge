from fastapi import *
import uvicorn
from db.db import *

app=FastAPI()


@app.get("/")
def entry():
    cursor.execute("""SELECT * FROM users """)
    res=cursor.fetchall()
    return {"message":res}

# if __name__ == "__main__":
#     uvicorn.run(app, reload=True)