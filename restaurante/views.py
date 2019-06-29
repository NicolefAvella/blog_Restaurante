from django.shortcuts import render
from .models import PostRestaurant
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RestauranteForm

from django.template import RequestContext
from django.shortcuts import render_to_response
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

def post_restaurant(request):
	posts = PostRestaurant.objects.filter(fecha_publicado__lte=timezone.now()).order_by('fecha_publicado').reverse() 
	return render (request, 'restaurante/post_restaurant.html',{'posts': posts})


def post_detail(request, pk):
	post = get_object_or_404(PostRestaurant, pk=pk)
	return render(request, 'restaurante/post_detail.html', {'post': post})

@login_required()
def post_new(request):
    if request.method == "POST":
        form = RestauranteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_publicado = timezone.now()
            post.save()
            return redirect('restaurante:post_detail', pk=post.pk)
    else:
        form = RestauranteForm()
    return render(request, 'restaurante/post_edit.html', {'form': form})

# restringir con login
@login_required()
def post_edit(request, pk):
    # el user ya esta logueado 
    user = request.user
    post = get_object_or_404(PostRestaurant, pk=pk)
    if user == post.autor:
        if request.method == "POST":
            form = RestauranteForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.fecha_publicado = timezone.now()
                post.save()
                return redirect('restaurante:post_detail', pk=post.pk)
        # GET, PUT, DELETE, 
        else:
            form = RestauranteForm(instance=post)
        return render(request, 'restaurante/post_edit.html', {'form': form})    
    else:
        return redirect('restaurante:post_restaurant')

def like_post(request):
    post = get_object_or_404(PostRestaurant, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(post.get_absolute_url())

def login_page(request) :
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('restaurante:post_restaurant')
            else:
                pass

    else:
        form = LoginForm()
    
    context ={
        'form': form
    }
    return render(request, 'restaurante/registro.html', context)