# Generated by Django 2.0.6 on 2018-09-06 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agrodata', '0007_companylogo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyaddress',
            name='company_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='companyAddress', to='agrodata.Company', unique=True),
        ),
        migrations.AlterField(
            model_name='companyaddress',
            name='fax',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='companylogo',
            name='company_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='CompanyLogo', to='agrodata.Company', unique=True),
        ),
        migrations.AlterField(
            model_name='companylogo',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/CompanyLogos', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='ingredientdetail',
            name='declaration',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='ingredientdetail',
            name='ingredient_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='IngredientDetail', to='agrodata.Ingredients', unique=True),
        ),
        migrations.AlterField(
            model_name='ingredientdetail',
            name='usage',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='product_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='productphysicalproperty',
            name='Colour',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='productphysicalproperty',
            name='Flavour',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='productphysicalproperty',
            name='Taste',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='productphysicalproperty',
            name='ingredient_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ProductPhysicalProperty', to='agrodata.Ingredients', unique=True),
        ),
        migrations.AlterField(
            model_name='productpicture',
            name='ingredient_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ProductPicture', to='agrodata.Ingredients', unique=True),
        ),
    ]