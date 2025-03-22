from contextlib import asynccontextmanager
from fastapi import FastAPI
from kafka import consume, stop_producer
import asyncio


@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(consume())
    yield
    await stop_producer()


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello From RentSafe AI Service!"}
