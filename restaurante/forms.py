from django import forms

from .models import PostRestaurant

class RestauranteForm(forms.ModelForm):

    class Meta:
        model = PostRestaurant
        fields = ('titulo', 'texto',)