from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from manager import Manager
import threading

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("the Retriever server started")
    m = Manager()
    t = threading.Thread(target=m.run, daemon=True)
    t.start()
    yield

    print("the Retriever server finished")

app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)