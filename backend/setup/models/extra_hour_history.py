from django.db import models
from .extra_hour import ExtraHour
from .custom_user import CustomUser

class ExtraHourHistory(models.Model):
    id = models.AutoField(primary_key=True)
    extra_hour = models.ForeignKey(ExtraHour, on_delete=models.CASCADE)
    date = models.DateField()
    action = models.CharField(max_length=200)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)