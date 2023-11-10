from fastapi import APIRouter


from .tasks import send_email_report


router = APIRouter(prefix="/report")


@router.get("/dashboard")
def get_dashboard_report():
    send_email_report.delay()

    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }


