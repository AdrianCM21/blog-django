
from django.urls import path 
from rest_framework.urlpatterns import format_suffix_patterns 
from .controller.api import login,noticias,comentarios

  
urlpatterns = [ 
    path("login",login.LoginView.as_view(), name='api-login'),
    path("noticias",noticias.NoticiasView.as_view(), name='api-noticias'),
    path("comentarios",comentarios.ComentariosView.as_view())
    


] 


  
