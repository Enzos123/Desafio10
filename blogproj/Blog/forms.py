from django import forms
from django.forms import ModelForm
from .models import Articulo

class BlogForm(forms.ModelForm):  
    class Meta:  
        model = Articulo
        fields = "__all__"  