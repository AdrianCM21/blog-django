
from rest_framework import serializers
from ..models import Usuarios

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['id', 'nombre', 'usuario', 'password', 'estado', 'nivel', 'grupo']