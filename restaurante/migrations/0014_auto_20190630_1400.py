# Generated by Django 2.2.2 on 2019-06-30 19:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0013_auto_20190630_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postrestaurant',
            name='fecha_publicado',
            field=models.DateField(default=datetime.date.today),
        ),
    ]