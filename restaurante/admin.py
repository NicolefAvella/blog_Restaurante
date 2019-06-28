from django.contrib import admin

# Register your models here.
from .models import Post_Restaurant


#Modelo visible en el administrador


class RestauranteAdmin(admin.ModelAdmin):
	list_display = ("autor", "fecha_publicado")
	search_fields = ("autor",  )


admin.site.register(Post_Restaurant,RestauranteAdmin)  
