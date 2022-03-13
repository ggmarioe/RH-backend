from ssl import create_default_context
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    contract_state= models.CharField(max_length=5, blank=True, null=True)


# clase para definir los documentos que se van a subir
class documents(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    file_path = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)


# clase para definir la asocicación entre los documentos y los usuarios
class documentsUsers(models.Model):
    id = models.AutoField(primary_key=True)
    document = models.ForeignKey(documents, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

# clase para definir una rendición de cuenta
class expenses(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

# clase de asociación entre la rendición de cuenta y los usuarios
class expensesUsers(models.Model):
    expense = models.ForeignKey(expenses, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class expensesHistory(models.Model): 
    id = models.AutoField(primary_key=True)
    expense = models.ForeignKey(expenses, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=500)


class ExtraHour(models.Model):
    id  = models.AutoField(primary_key=True)
    date = models.DateField()
    hours = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField()
    status = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class ExtraHourHistory(models.Model):
    id = models.AutoField(primary_key=True)
    extra_hour = models.ForeignKey(ExtraHour, on_delete=models.CASCADE)
    date = models.DateField()
    action = models.CharField(max_length=200)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    


