# Generated by Django 2.2.2 on 2019-06-30 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0015_auto_20190630_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fecha_comentario',
            field=models.DateTimeField(auto_now=True),
        ),
    ]