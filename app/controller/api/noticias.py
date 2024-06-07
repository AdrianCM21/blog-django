from ...models import Usuarios,Noticias
from ...serializers.UsuarioSerializers import UsuariosSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status

from django.contrib.auth.hashers import check_password
from ...serializers.NoticiasSeralizers import NoticiasSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status

class NoticiasView(APIView):

    @csrf_exempt
    def get(self, request, format=None):
        session_header = request.headers.get('session')
       
        if session_header:
            noticias = Noticias.objects.all()
            noticias_serializer = NoticiasSerializer(noticias, many=True, context={'request': request})
            return JsonResponse(noticias_serializer.data, safe=False, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'Session header not found'}, status=status.HTTP_400_BAD_REQUEST)