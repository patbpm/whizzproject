from django.contrib import admin

# Register your models here.
from .models import Database, Company, CompanyAddress, IngredientsCategories, Ingredients

admin.site.register(Database)
admin.site.register(Company)
admin.site.register(CompanyAddress)
admin.site.register(IngredientsCategories)
admin.site.register(Ingredients)