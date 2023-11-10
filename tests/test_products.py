from httpx import AsyncClient


async def test_add_product(ac: AsyncClient):
    response = await ac.post("/products/create", json={
        "id": 1,
        "title": "Coca",
        "price": 500,
        "created_at": "2023-11-10T21:51:54.603",
        "updated_at": "2023-11-10T21:51:54.603",
        "is_active": True,
    })

    assert response.status_code == 200


