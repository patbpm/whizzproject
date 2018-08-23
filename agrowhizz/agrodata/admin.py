from django.contrib import admin

# Register your models here.
from .models import Database, Company

admin.site.register(Database)
admin.site.register(Company)