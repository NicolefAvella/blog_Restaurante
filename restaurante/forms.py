from django import forms

from .models import PostRestaurant

class RestauranteForm(forms.ModelForm):

    class Meta:
        model = PostRestaurant
        fields = ('titulo', 'texto','comentarios','categoria')

class LoginForm(forms.Form):
	username= forms.CharField(label="usuario")
	password = forms.CharField(label="contraseña", widget=forms.PasswordInput)
	
        