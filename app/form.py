from django import forms
from .models import Noticias, Grupos

class NoticiasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        grupos = Grupos.objects.all()
        opciones = [(grupo.id, grupo.grupo) for grupo in grupos]
        self.fields['grupo'].widget.choices = opciones
    class Meta:
        model = Noticias
        fields = ['titulo', 'contenido', 'imagen', 'grupo', 'autor']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo de la noticia','style':'border: 1px solid #000'}),
            'grupo': forms.Select(attrs={'class': 'form-control','style':'border: 1px solid #000'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenido de la noticia','style':'border: 1px solid #000'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Imagen'}),
        }