from django.contrib import admin

# Register your models here.
from .models import PostRestaurant, Comentario


#Modelo visible en el administrador
class RestauranteAdmin(admin.ModelAdmin):
	list_display = ("autor", "fecha_publicado", "categoria", "tags")
	list_filter = ("categoria","tags",)
	search_fields = ("tags","autor")

admin.site.register(PostRestaurant, RestauranteAdmin)  
admin.site.register(Comentario)