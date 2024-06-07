import json
from ...models import Comentarios, Noticias
from ...serializers.UsuarioSerializers import UsuariosSerializer
from ...serializers.NoticiasSeralizers import NoticiasSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status

class ComentariosView(APIView):

    @csrf_exempt
    def post(self, request, format=None):
        session_header = request.headers.get('session')
        if session_header:
            try:
                session_data = json.loads(session_header)
                nombre = session_data.get('nombre')
                v_comentario = request.data.get('comentario')
                v_noticia_id = request.data.get('id_noticia')
            

                if not (nombre and v_comentario and v_noticia_id):
                    return JsonResponse({'error': 'Faltan datos necesarios'}, status=status.HTTP_400_BAD_REQUEST)

                try:
                    noticia = Noticias.objects.get(id=v_noticia_id)
                except Noticias.DoesNotExist:
                    return JsonResponse({'error': 'Noticia no encontrada'}, status=status.HTTP_404_NOT_FOUND)

                comentario = Comentarios.objects.create(
                    comentario=v_comentario,
                    nombre=nombre,
                    noticia=noticia,
                    visible=False
                )

                return JsonResponse({'status': 'success', 'comentario_id': comentario.id}, status=status.HTTP_201_CREATED)

            except json.JSONDecodeError:
                return JsonResponse({'error': 'Formato de encabezado de sesión no válido'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'error': 'Encabezado de sesión no encontrado'}, status=status.HTTP_400_BAD_REQUEST)
