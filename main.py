from fastapi import FastAPI
from bot_controller import router as bot_router

app = FastAPI()

app.include_router(bot_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)