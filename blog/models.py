from django.db import models
from datetime import datetime

# Create your models here.
class obeid(models.Model):
    pass
class customer(models.Model):
    name_customer=models.CharField(max_length=100,null=False)
    date_created=models.DateTimeField(auto_now=datetime.now)
    
