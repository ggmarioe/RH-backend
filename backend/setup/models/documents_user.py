import imp
from django.db import models
from .custom_user import CustomUser
from .documents import Documents

# clase para definir la asocicación entre los documentos y los usuarios
class documentsUsers(models.Model):
    id = models.AutoField(primary_key=True)
    document = models.ForeignKey(Documents, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)