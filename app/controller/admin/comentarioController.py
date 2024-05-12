from django.shortcuts import render, redirect, HttpResponse
from ...models import Comentarios,Noticias


def showComentarios(request):
    print(request.session['nivel_usuario'])
    if 'nivel_usuario' in request.session:
        if request.session['nivel_usuario']=='Admin':
            response = Comentarios.objects.all()
            variable = {}
            variable["request"] = request
            variable["lista"] = response
            return render(request, "admin/comentarios.html", variable)
        else:
            return redirect('login')
    else:
        return redirect('login')
    

def addComentarios(request):
    if request.method=='POST':
        nombre = request.session['nombre_usuario']
        comentario = request.POST.get('comentario')
        id_publicacion= request.POST.get('id_publicacion')
        try:
            noticia = Noticias.objects.get(id=id_publicacion)
        except Noticias.DoesNotExist:
            return HttpResponse('Noticia no encontrada')


        Comentarios.objects.create(comentario=comentario,nombre=nombre,noticia=noticia,visible=True)
        

        return HttpResponse('ok')

def deleteGrupos(request, id):

    if request.method == 'POST':
        try:
            usuario = Comentarios.objects.get(id=id)
            usuario.delete()
            return redirect('show_grupos')
        except Comentarios.DoesNotExist:
            return HttpResponse("Usuario no encontrado")
    else:
        return HttpResponse("Método no permitido")
