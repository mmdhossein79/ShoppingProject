# Generated by Django 3.2.7 on 2021-10-14 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='user',
            name='post_code',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
