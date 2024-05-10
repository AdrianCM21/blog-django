from django import forms
from .models import Noticias

class NoticiasForm(forms.ModelForm):
    class Meta:
        model = Noticias
        fields = ['titulo', 'contenido', 'imagen', 'grupo', 'autor']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo de la noticia','style':'border: 1px solid #000'}),
            'grupo': forms.Select(attrs={'class': 'form-control','style':'border: 1px solid #000'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenido de la noticia','style':'border: 1px solid #000'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Imagen'}),
        }