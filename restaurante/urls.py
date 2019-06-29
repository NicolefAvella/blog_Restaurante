#from django.conf.urls import url
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [

    path('', views.post_restaurant, name='post_restaurant'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
