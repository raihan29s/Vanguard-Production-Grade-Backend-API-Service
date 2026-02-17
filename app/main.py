from fastapi import FastAPI
from app.api.v1.endpoints import auth
from app.core.redis import cache

app = FastAPI(title="Vanguard API")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/health")
async def health():
    return {"status": "online"}
