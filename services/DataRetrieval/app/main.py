"""REST API for retrieving stored tweets."""

from fastapi import FastAPI
from dal import Dal
import uvicorn




app = FastAPI()
dal = Dal ()

@app.get("/")
def root():
    """Health check endpoint."""
    return {"ok": True}

@app.get("/antisemitic_data")
def get_all_antisemitic_data():
   """Return a sample of antisemitic documents."""
   res = dal.get_antisemitic_data()
   return res

@app.get("/not_antisemitic_data")
def get_all_not_antisemitic_data():
   """Return a sample of non-antisemitic documents."""
   res = dal.get_not_antisemitic_data()
   return res

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8004)