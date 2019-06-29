from django.db import models

# Create your models here.
from django.utils import timezone  
from .data import TIPO_OPCIONES
from .data import SUR_AMERICA

from django.contrib.auth.models import User

class PostRestaurant(models.Model):
    autor = models.ForeignKey(User, related_name='blog_restaurante', on_delete=models.PROTECT)
    #autor = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_publicado = models.DateTimeField(
            blank=True, null=True)
    categoria = models.CharField(max_length=50, choices=TIPO_OPCIONES, default=SUR_AMERICA)
    tags = models.CharField(max_length=100, null=True, blank=True)
    comentarios = models.TextField(max_length=500, default='deja tu comentario aqui!')
    likes = models.ManyToManyField(User, related_name='likes', blank=True)


    def publicacion(self):
        self.fecha_publicado = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo