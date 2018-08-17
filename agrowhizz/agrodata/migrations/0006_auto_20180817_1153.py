# Generated by Django 2.0.6 on 2018-08-17 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agrodata', '0005_auto_20180817_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='company',
            name='business_stream_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='companies', to='agrodata.Database'),
        ),
        migrations.DeleteModel(
            name='Business_stream',
        ),
    ]
