from fastapi import FastAPI
import os

app = FastAPI()

from src.bot_controller import router as bot_router
app.include_router(bot_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "8000"))
    reload = os.getenv("RELOAD", "false").lower() == "true"
    
    uvicorn.run("src.main:app", host=host, port=port, reload=reload)