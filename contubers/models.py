from django.db import models
from datetime import datetime

# Create your models here.

class Contuber(models.Model):
    full_name=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField(blank=True)
    created_date = models.DateTimeField(blank=True, default = datetime.now)
    
    def __str__(self):
        return self.subject 
    