from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from manager import Manager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("the Enricher server started")
    m = Manager()
    m.run()
    yield

    print("the Enricher server finished")

app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8002)