from django.db import models

# Create your models here.
from django.utils import timezone  


class Post_Restaurant(models.Model):
    autor = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_publicado = models.DateTimeField(
            blank=True, null=True)

    def publicacion(self):
        self.fecha_publicado = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo