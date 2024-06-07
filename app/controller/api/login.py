from ...models import Usuarios
from ...serializers.UsuarioSerializers import UsuariosSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status

from django.contrib.auth.hashers import check_password


class LoginView(APIView):

    @csrf_exempt
    def post(self, request, format=None):
        v_usuario = request.data.get('usuario')
        v_clave = request.data.get('password')
        

        verificar_usuario = Usuarios.objects.filter(usuario=v_usuario, estado='Activo')
        
        if verificar_usuario.exists() and v_clave== verificar_usuario[0].password:
            user = verificar_usuario[0]
            request.session['codigo_usuario'] = user.id
            request.session['nombre_usuario'] = user.nombre
            request.session['nivel_usuario'] = user.nivel

            user_data = UsuariosSerializer(user).data
            response_data = {
                'codigo_usuario': request.session['codigo_usuario'],
                'nombre_usuario': request.session['nombre_usuario'],
                'nivel_usuario': request.session['nivel_usuario'],
                'user_data': user_data,
            }

            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_403_FORBIDDEN)
