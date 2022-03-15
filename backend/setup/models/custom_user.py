from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    contract_state= models.CharField(max_length=5, blank=True, null=True)