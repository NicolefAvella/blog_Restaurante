from django.conf.urls import url
from .import views
from django.conf.urls.static import static


urlpatterns = [
     url('', views.post_restaurant, name='post_restaurant'),
]