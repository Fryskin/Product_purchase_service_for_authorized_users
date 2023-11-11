from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
import aioredis
from src.auth.base_config import auth_backend, fastapi_users
from src.auth.router import router as router_user
from src.shopper.router import router as router_product
from src.auth.schemas import UserRead, UserCreate


app = FastAPI(
    title="Product purchase service for authorized users",
    openapi_url='/swagger.io'
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)


app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)


app.include_router(router_user)

app.include_router(router_product)


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url("redis://localhost",
                              encoding="utf8",
                              decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
