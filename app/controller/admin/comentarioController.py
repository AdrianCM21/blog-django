from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from ...models import Comentarios,Noticias


def showComentarios(request,id):
    print(request.session['nivel_usuario'])
    if 'nivel_usuario' in request.session:
        if request.session['nivel_usuario']=='Admin':
            response = Comentarios.objects.filter(noticia_id=id)
            variable = {}
            variable["request"] = request
            variable["lista"] = response
            variable['noticia_code']=id
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
        

        return JsonResponse({'status': 'success'})

def ocultarComentario(request, id):

    if request.method == 'POST':
        try:
            noticia_id=request.POST.get('noticia_id')
            comentario = Comentarios.objects.get(id=id)
            comentario.visible = not comentario.visible
            comentario.save()
            
            return redirect('show_comentarios', id=noticia_id)
        except Comentarios.DoesNotExist:
             return redirect('show_comentarios', id=noticia_id)
    else:
        return HttpResponse("Método no permitido")
