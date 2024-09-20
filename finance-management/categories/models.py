import uuid

from django.db import models

from authenticate.models import CustomUser


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    plaid_id = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
