#from django.conf.urls import url
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views

app_name = "restaurante"

urlpatterns = [

    path('', views.post_restaurant, name='post_restaurant'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('register', views.register, name='registro'),

    #Recuperar contraseña
    #path('accounts/', include('django.contrib.auth.urls')),


    #path('password_reset/', auth_views.PasswordChangeView.as_view()),
    #path('password_reset', auth_views.password_reset, name= "password_reset"),
    #path('password_reset/done', auth_views.password_reset_done, name= "password_reset_done"),
    #path('password_reset/confirm/(?P<uidb64>[\w-]+)/(?P<token>[\w-]+)/', auth_views.password_reset_confirm, name= "password_reset_confirm"),
    #path('password_reset/complete', auth_views.password_reset_complete, name= "password_reset_complete"),
]
