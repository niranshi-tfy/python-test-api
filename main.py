from fastapi import FastAPI
import asyncio
import os
import dotenv

app = FastAPI()

dotenv.load_dotenv(".env")
@app.get("/")
async def root():
    await asyncio.sleep(int(os.environ["SLEEP_TIME"]))
    return {"message": "Hello World"}
