from django.shortcuts import render
from .models import Post_Restaurant
from django.utils import timezone

# Create your views here.

def post_restaurant(request):
	posts = Post_Restaurant.objects.filter(fecha_publicado__lte=timezone.now()).order_by('fecha_publicado')
	return render (request, 'restaurante/post_restaurant.html',{'posts': posts})





