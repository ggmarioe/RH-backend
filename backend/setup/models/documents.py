from django.db import models

class Documents(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    file_path = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)