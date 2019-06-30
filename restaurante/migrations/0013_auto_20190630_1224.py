# Generated by Django 2.2.2 on 2019-06-30 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurante', '0012_postrestaurant_fecha_desactivado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postrestaurant',
            name='comentarios',
        ),
        migrations.AlterField(
            model_name='postrestaurant',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentarios', models.TextField(default='deja tu comentario aqui!', max_length=500)),
                ('autor_comentario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('post_restaurant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurante.PostRestaurant')),
            ],
        ),
    ]
