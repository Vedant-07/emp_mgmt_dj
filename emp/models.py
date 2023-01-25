from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField( max_length=100)
    emp_id=models.CharField( max_length=100)
    phone=models.CharField( max_length=10)
    e_addr=models.CharField( max_length=300)
    wfh=models.BooleanField(default=False)
    dept=models.CharField(max_length=100)