from fastapi import FastAPI
from dal import Dal
import uvicorn




app = FastAPI()
dal = Dal ()

@app.get("/")
def root():
    return {"ok": True}

@app.get("/antisemitic_data")
def get_all_antisemitic_data():
   res = dal.get_antisemitic_data()
   return res

@app.get("/not_antisemitic_data")
def get_all_not_antisemitic_data():
   res = dal.get_not_antisemitic_data()
   return res

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8004)
