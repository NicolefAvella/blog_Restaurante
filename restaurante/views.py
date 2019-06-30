from django.shortcuts import render
from .models import PostRestaurant
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RestauranteForm,  LoginForm

from django.template import RequestContext
from django.shortcuts import render_to_response
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
# Create your views here.

def post_restaurant(request):
    # lt = less than  e= qual <= gt, lt, gte
    posts = PostRestaurant.objects.filter(
        Q(fecha_desactivado__isnull=True) | Q(fecha_desactivado__gte=timezone.now()),
        fecha_publicado__lte=timezone.now(),
        ).order_by('fecha_publicado').distinct().reverse() 
    query = request.GET.get('q')
    if query :
        posts = PostRestaurant.objects.filter(
        Q(categoria=query)|
        Q(tags__icontains=query)|    
        Q(autor__username__icontains=query), # post_contenido
        ).distinct()
    return render (request, 'restaurante/post_restaurant.html',{'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(PostRestaurant, pk=pk)
    is_liked=False
    if request.user.is_authenticated :   
        like_user=post.likes.filter(
        username=request.user.username
        )
        if like_user.count()==1:
            is_liked=True

    if request.method=='POST':
        if is_liked==True:
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user) 
        
    context = {
    'post': post,
    'is_liked' : is_liked,
    }    
    return render(request, 'restaurante/post_detail.html', context)

@login_required()
def post_new(request):
    if request.method == "POST":
        form = RestauranteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
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
    if user == post.autor or user.is_superuser:
        if request.method == "POST":
            form = RestauranteForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.save()
                return redirect('restaurante:post_detail', pk=post.pk)
        # GET, PUT, DELETE, 
        else:
            form = RestauranteForm(instance=post)
            context = {
                'form': form,
            }    
        return render(request, 'restaurante/post_edit.html', context)    
    else:
        return redirect('restaurante:post_restaurant')


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

def logout_page(request):
    logout(request)
    return redirect('restaurante:post_restaurant')    

def register(request):
    if request.method == 'POST' :
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])    
            new_user.save()
            return redirect('restaurante:post_restaurant')

    else:
        form = RegistrationForm()
    context = {
        'form' : form,
    }
    return render(request, 'registro/register.html', context)
                