# Generated by Django 2.0.6 on 2018-10-17 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrodata', '0007_auto_20181017_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companylogo',
            name='picture',
            field=models.ImageField(blank=True, default='/noimage.png', null=True, upload_to='uploads/CompanyLogos', verbose_name='Image'),
        ),
    ]
