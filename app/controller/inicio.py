from django.shortcuts import render, redirect,HttpResponse
from django.core.paginator import Paginator
from ..models import Noticias ,Comentarios
def inicio(request):
    if 'nivel_usuario' in request.session:
        page = request.GET.get('page',1)
        response = Noticias.objects.all()
        try:
            paginator = Paginator(response,5)
            publicaciones=paginator.page(page)
            print(publicaciones.count)
        except:
            return HttpResponse("Pagina no encontrada")
        variable = {}
        variable["request"] = request
        variable["lista"] = publicaciones
        variable["paginator"]=paginator
        return render(request, "home/inicio.html",variable)
       
    else:
        return redirect('login')
    
def show_publicacion(request, id):
    if 'nivel_usuario' in request.session:
        try:
            publicacion = Noticias.objects.get(id=id)
            comentarios = Comentarios.objects.filter(noticia_id=id)
            variable = {}
            variable["publicacion"] = publicacion
            variable["comentarios"] = comentarios
            print(comentarios)

            return render(request, "home/post_show.html", variable)
        except Noticias.DoesNotExist:
            return HttpResponse("Usuario no encontrado")
        
    else:
        return redirect('login')


