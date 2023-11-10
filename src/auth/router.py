from fastapi import APIRouter, Depends

from src.auth.base_config import current_user
from src.auth.models import User
from src.tasks.router import get_dashboard_report

router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@router.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    get_dashboard_report()
    return f"Hello, {user.email}"
