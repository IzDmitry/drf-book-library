from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    """
    Переопределение модели AbstractUser
    """
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)
    registration_date = models.DateTimeField(default=timezone.now)
