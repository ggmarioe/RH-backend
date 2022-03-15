from django.db import models
from .custom_user import CustomUser
from .expenses import Expenses

class ExpensesUsers(models.Model):
    expense = models.ForeignKey(Expenses, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)