from django.db import models
from .extra_hour import ExtraHour
from .custom_user import CustomUser
from .expenses import Expenses

class ExpensesHistory(models.Model): 
    id = models.AutoField(primary_key=True)
    expense = models.ForeignKey(Expenses, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=500)