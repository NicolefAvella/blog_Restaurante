# Generated by Django 2.2.2 on 2019-06-29 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postrestaurant',
            name='comentarios',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='postrestaurant',
            name='tags',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
