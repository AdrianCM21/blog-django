from rest_framework import serializers
from ..models import Noticias, Grupos, Usuarios, Comentarios

class GruposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupos
        fields = ['id', 'grupo']

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['id', 'nombre', 'usuario', 'estado', 'nivel', 'grupo']

class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = ['nombre', 'comentario', 'fecha', 'visible']

class NoticiasSerializer(serializers.ModelSerializer):
    grupo = GruposSerializer()
    autor = UsuariosSerializer()
    comentarios = serializers.SerializerMethodField()

    class Meta:
        model = Noticias
        fields = ['id', 'titulo', 'subtitulo', 'fecha', 'contenido', 'imagen', 'grupo', 'autor', 'comentarios']

    def get_comentarios(self, obj):
        comentarios = obj.comentarios_set.filter(visible=True)
        return ComentariosSerializer(comentarios, many=True).data
