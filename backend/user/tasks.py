from celery import shared_task
from django.core.mail import send_mail
from time import sleep


@shared_task
def send_welcome_email_task(email, username):
    """
    Функция для отпраки email.
    """
    sleep(10)
    send_mail(
        f'Hello {username}',
        'Registration completed successfully',
        'izdmitry.py@yandex.ru',
        [email],
        fail_silently=False,)
