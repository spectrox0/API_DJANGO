# Generated by Django 3.1 on 2020-08-16 20:02

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200808_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]