import smtplib
from email.message import EmailMessage

from celery import Celery
from fastapi import Depends

from src.auth.models import User
from src.config import SMTP_PASSWORD, SMTP_USER

from src.auth.base_config import current_user

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery = Celery('tasks', broker='redis://localhost:6379')


def get_email_template_dashboard(user: User = Depends(current_user)):
    email = EmailMessage()
    email['Subject'] = 'Password confirmation'
    email['From'] = SMTP_USER
    email['To'] = user.email

    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте,'
        f' {user.username}, Вы успешно внесли изменения в продукт или удалили его😊</h1>'
        '</div>',
        subtype='html'
    )
    return email


@celery.task
def send_email_report():
    email = get_email_template_dashboard()
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)
