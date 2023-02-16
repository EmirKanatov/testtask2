from django.core.mail import send_mail

from todoproject import settings
from todoproject.celery import app


@app.task
def send_notification(email, task):
    mail_subject = "Hye from celery"
    message = f"You have to complete this task {task} in 24hours!!!"
    to_email = email
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
    )
