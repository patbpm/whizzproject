import math
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
# Create your models here.


class Business_stream(models.Model):
    business_stream_name = models.CharField(max_length=30, unique=True)
    business_stream_description = models.CharField(max_length=100)

    def __str__(self):
        return self.business_stream_name

class Company(models.Model):
    company_name = models.CharField(max_length=100, unique=True)
    profile_description = models.CharField(max_length=100)
    business_stream_id = models.ForeignKey(Business_stream, related_name='companies',on_delete=models.PROTECT)
    last_updated = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.company_name
