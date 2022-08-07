from celery import shared_task

from django.core.mail import send_mail


@shared_task
def send_task(subject, email_recipient, message):
    send_mail(
        subject=subject,
        message=message,
        from_email='admin@example.com',
        recipient_list=[email_recipient],
        fail_silently=False
    )
