from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from manager import Manager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("the Persister server started")
    m = Manager()
    m.run()
    yield

    print("the Persister server finished")

app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8003)