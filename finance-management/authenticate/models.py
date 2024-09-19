from django.contrib.auth.models import AbstractUser

from django.db import models


class CustomUser(AbstractUser):
    id = models.CharField(primary_key=True, editable=False)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
