from django.shortcuts import render
from .models import PostRestaurant
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import RestauranteForm

# Create your views here.

def post_restaurant(request):
	posts = PostRestaurant.objects.filter(fecha_publicado__lte=timezone.now()).order_by('fecha_publicado')
	return render (request, 'restaurante/post_restaurant.html',{'posts': posts})


def post_detail(request, pk):
	print(pk)
	post = get_object_or_404(PostRestaurant, pk=pk)
	return render(request, 'restaurante/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = RestauranteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_publicado = timezone.now()
            post.save()
            return redirect('restaurante.views.post_detail', pk=post.pk)
    else:
        form = RestauranteForm()
    return render(request, 'restaurante/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(PostRestaurant, pk=pk)
    if request.method == "POST":
        form = RestauranteForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_publicado = timezone.now()
            post.save()
            return redirect('restaurante.views.post_detail', pk=post.pk)
    else:
        form = RestauranteForm(instance=post)
    return render(request, 'restaurante/post_edit.html', {'form': form})    