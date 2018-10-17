import math
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
# Create your models here.

# Database for all the food classification #
class Database(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

 
# Database for all Food Industry #
class Company(models.Model):
    company_name = models.CharField(max_length=100, unique=True)
    profile_description = models.CharField(max_length=100)
    full_description = models.TextField(null=True)
    database = models.ForeignKey(Database, related_name='companies',on_delete=models.PROTECT)
    last_updated = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.company_name

# Database for all address of the Food Industry #
class CompanyAddress(models.Model):
    company_name = models.ForeignKey(Company, related_name='companyAddress',on_delete=models.PROTECT, unique=True)
    location = models.CharField(max_length=200)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    country = models.CharField(max_length=25)
    postal_code = models.CharField(max_length=6)
    fax= models.CharField(max_length=50, null=True, blank=True)
    telephone = models.CharField(max_length=50)
    website = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.company_name.company_name

# Database for all the Ingredients Categories #
class IngredientsCategories(models.Model):
    category = models.CharField(max_length=50, unique=True)
    

    def __str__(self):
        return self.category

# Database for all The Ingredients #
class Ingredients(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(IngredientsCategories, related_name='Ingredients',on_delete=models.PROTECT)
    company_name = models.ForeignKey(Company, related_name='Ingredients',on_delete=models.PROTECT)
    product_code = models.CharField(max_length=10, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name + " - " + self.company_name.company_name 


class IngredientDetail(models.Model):
    ingredient_name = models.ForeignKey(Ingredients, related_name='IngredientDetail',on_delete=models.PROTECT, unique=True)
    declaration= models.CharField(max_length=500, null=True, blank=True)
    usage = models.CharField(max_length=500, null=True, blank=True)
    full_description = models.TextField(null=True)
    
    
    def __str__(self):
        return self.ingredient_name.name + " - " + self.ingredient_name.company_name.company_name 

class ProductPhysicalProperty(models.Model):
    ingredient_name = models.ForeignKey(Ingredients, related_name='ProductPhysicalProperty',on_delete=models.PROTECT, unique=True)
    appearance = models.CharField(max_length=500, null=True, blank=True)
    Colour= models.CharField(max_length=500, null=True, blank=True)
    Taste = models.CharField(max_length=500, null=True, blank=True)
    Flavour = models.CharField(max_length=500, null=True, blank=True)
    
    
    def __str__(self):
        return self.ingredient_name.name + " - " + self.ingredient_name.company_name.company_name

class ProductPicture(models.Model):
    ingredient_name = models.ForeignKey(Ingredients, related_name='ProductPicture',on_delete=models.PROTECT,  unique=True)
    picture = models.ImageField(verbose_name=u'Image', upload_to="uploads/productPictures", null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.ingredient_name.name + " - " + self.ingredient_name.company_name.company_name

class CompanyLogo(models.Model):
    company_name = models.ForeignKey(Company, related_name='CompanyLogo',on_delete=models.PROTECT, unique=True)
    picture = models.ImageField(verbose_name=u'Image', upload_to="uploads/CompanyLogos", default= 'uploads/CompanyLogos/noimage.png', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.company_name.company_name