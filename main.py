from fastapi import FastAPI
import asyncio
import os
import dotenv

app = FastAPI()

dotenv.load_dotenv(".env")
@app.get("/")
async def root():
    await asyncio.sleep(0.1)
    return {"message": "Hello World"}
