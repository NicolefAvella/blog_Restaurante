from django.contrib import admin

# Register your models here.
from .models import PostRestaurant


#Modelo visible en el administrador


class RestauranteAdmin(admin.ModelAdmin):
	list_display = ("autor", "fecha_publicado")
	search_fields = ("autor",  )


admin.site.register(PostRestaurant, RestauranteAdmin)  

