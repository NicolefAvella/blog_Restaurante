from django.db import models

# Create your models here.
from django.utils import timezone  
from .data import TIPO_OPCIONES
from .data import SUR_AMERICA
from datetime import date
from django.contrib.auth.models import User

class PostRestaurant(models.Model):
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_publicado = models.DateField(default=date.today)
    fecha_desactivado = models.DateField(blank=True, null=True)
    fecha_edicion = models.DateTimeField(auto_now=True)
    categoria = models.CharField(max_length=50, choices=TIPO_OPCIONES, default=SUR_AMERICA)
    tags = models.CharField(max_length=100, null=True, blank=True, default= 'tag')
    
    likes = models.ManyToManyField(User, related_name='likes', blank=True)


    def publicacion(self):
        self.fecha_publicado = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

    def total_likes(self):
        return self.likes.count()   

    #atribut shell, implicito manytomany
    def get_comentarios(self):
        return  self.comentario_set.all() 

class Comentario(models.Model):
    post_restaurant = models.ForeignKey(PostRestaurant, on_delete=models.PROTECT)
    comentarios = models.TextField(max_length=200, default='deja tu comentario aqui!', null=True)
    autor_comentario = models.ForeignKey(User, on_delete=models.PROTECT)
    fecha_comentario = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.post_restaurant.titulo, str(self.post_restaurant.autor))
    
