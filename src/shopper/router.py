
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_cache.decorator import cache

from src.auth.base_config import current_user
from src.auth.models import User
from src.database import get_async_session
from src.shopper.models import product
from src.shopper.schemas import ProductCreate, ProductUpdate


router = APIRouter(
    prefix="/products",
    tags=["Product"]
)


@router.get("/retrieve")
@cache(expire=600)
async def get_all_products(limit: int = 10, offset: int = 0, session: AsyncSession = Depends(get_async_session),
                           user: User = Depends(current_user)):
    if user.active is False:
        return {"code": 401, "message": "Unauthorized"}

    query = select(product)
    result = await session.execute(query)

    return result.mappings().all()[offset:][:limit]


@router.post("/create")
async def add_product(new_product: ProductCreate, session: AsyncSession = Depends(get_async_session),
                      user: User = Depends(current_user)):
    if user.active is False:
        return {"code": 401, "message": "Unauthorized"}

    stmt = insert(product).values(**new_product.dict())
    await session.execute(stmt)
    await session.commit()

    return {"status": "The product was successfully created"}


@router.put("/update")
async def update_product(product_id: int, new_stmt: ProductUpdate, session: AsyncSession = Depends(get_async_session),
                         user: User = Depends(current_user)):
    if user.active is False:
        return {"code": 401, "message": "Unauthorized"}

    stmt = update(product).values(**new_stmt.dict()).where(product.c.id == product_id)
    await session.execute(stmt)
    await session.commit()

    return {"status": "The product was successfully updated"}


@router.delete("/delete")
# async def delete_product(product_id: int, session: AsyncSession = Depends(get_async_session)):
async def delete_product(product_id: int, session: AsyncSession = Depends(get_async_session),
                         user: User = Depends(current_user)):

    if user.active is False:
        return {"code": 401, "message": "Unauthorized"}

    stmt = delete(product).where(product.c.id == product_id)
    await session.execute(stmt)
    await session.commit()

    return {"status": "The product was successfully deleted"}




