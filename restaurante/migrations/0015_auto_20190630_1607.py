# Generated by Django 2.2.2 on 2019-06-30 21:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0014_auto_20190630_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='fecha_comentario',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='comentarios',
            field=models.TextField(default='deja tu comentario aqui!', max_length=200),
        ),
    ]
