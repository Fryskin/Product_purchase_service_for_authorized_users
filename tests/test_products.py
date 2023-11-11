from httpx import AsyncClient


async def test_add_product_unauthorized(ac: AsyncClient):
    response = await ac.post("/products/create", json={
        "id": 1,
        "title": "Coca",
        "price": 500,
        "created_at": "2023-11-10T21:51:54.603",
        "updated_at": "2023-11-10T21:51:54.603",
        "is_active": True,
    })

    assert response.status_code == 401


async def test_update_product_unauthorized(ac: AsyncClient):
    response = await ac.put("/products/update?product_id=1", json={
        "title": "Cuca",
        "price": 480,
        "updated_at": "2023-11-11T09:49:47.161"
    })

    assert response.status_code == 401


async def test_delete_product_unauthorized(ac: AsyncClient):
    response = await ac.delete('/products/delete?product_id=1')

    assert response.status_code == 401
