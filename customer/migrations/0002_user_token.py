# Generated by Django 3.2.7 on 2021-10-07 17:05

import customer.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(default=customer.models.random_str, max_length=15),
        ),
    ]