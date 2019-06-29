# Generated by Django 2.2.2 on 2019-06-29 16:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurante', '0007_auto_20190629_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='postrestaurant',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
