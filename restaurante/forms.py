from django import forms
from .models import PostRestaurant
from django.contrib.auth.models import User

class RestauranteForm(forms.ModelForm):

    class Meta:
        model = PostRestaurant
        fields = ('titulo', 'texto','comentarios','categoria')

class LoginForm(forms.Form):
	username= forms.CharField(label="usuario")
	password = forms.CharField(label="contraseña", widget=forms.PasswordInput)
	
class RegistrationForm(forms.ModelForm):     
    password = forms.CharField(label="contraseña", widget=forms.PasswordInput(attrs={'placeholder':'Ingrese contraseña aqui'}))
    confirm_password = forms.CharField(label=" confirmar contraseña", widget=forms.PasswordInput(attrs={'placeholder':'Confirmar contraseña'}))
	
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')
 
    def clean_confirm_password(self):
        password=self.cleaned_data.get('password')	
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password Mismatch")
        return confirm_password	