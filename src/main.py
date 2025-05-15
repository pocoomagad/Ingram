import uvicorn
from fastapi import FastAPI

app = FastAPI(
    description="Analogie of Instagram with chats on websokets", 
    title="INGRAM",
    version="0.1.0",
    summary="New explore with websokets",
    )

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)