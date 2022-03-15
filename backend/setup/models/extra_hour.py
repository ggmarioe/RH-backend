from django.db import models
from .custom_user import CustomUser

class ExtraHour(models.Model):
    id  = models.AutoField(primary_key=True)
    date = models.DateField()
    hours = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField()
    status = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
