import math
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
# Create your models here.


class Database(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Company(models.Model):
    company_name = models.CharField(max_length=100, unique=True)
    profile_description = models.CharField(max_length=100)
    business_stream_id = models.ForeignKey(Database, related_name='companies',on_delete=models.PROTECT)
    last_updated = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.company_name
