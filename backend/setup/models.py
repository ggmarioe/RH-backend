from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    contract_state= models.CharField(max_length=5, blank=True, null=True)



# clase para definir los documentos que se van a subir
class documents(models.Model):
    pass

# clase para definir la asocicación entre los documentos y los usuarios
class documentsUsers(models.Model):
    pass


# clase para definir una rendición de cuenta
class expenses(models.Model):
    pass

# clase de asociación entre la rendición de cuenta y los usuarios
class expensesUsers(models.Model):
    pass



