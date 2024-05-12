from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from ...models import Noticias,Usuarios
from ...form import NoticiasForm


def showNoticias(request):
    if 'nivel_usuario' in request.session:
        if request.session['nivel_usuario']=='Admin' or request.session['nivel_usuario']=='Escritor':
            response = Noticias.objects.all()
            variable = {}
            variable["request"] = request
            variable["lista"] = response
            noticias_list = list(response)


            return render(request, "admin/noticias.html", variable)
        else:
            return redirect('login')
    else:
        return redirect('login')
    

def addNoticias(request):
    if request.method=='GET':
        if 'nivel_usuario' in request.session:   
            if request.session['nivel_usuario']=='Admin' or request.session['nivel_usuario']=='Escritor':
                form = NoticiasForm()
                
                autor = Usuarios.objects.get(id=request.session['codigo_usuario' ]) 
                if(not autor):
                    return redirect('show_noticias')

                form = NoticiasForm(initial={'autor': autor})
        
                return render(request,"admin/saveNoticias.html",{"form":form})
            else:
               
                return redirect('login')
        else:
             return redirect('login')
    
    if request.method=='POST':
        if 'nivel_usuario' in request.session:   
            if request.session['nivel_usuario']=='Admin' or request.session['nivel_usuario']=='Escritor':
                form = NoticiasForm(request.POST,request.FILES)
              
                if form.is_valid():
                    form.save()
                    return redirect('show_noticias')
                else:
                    print(form.errors)
                return render(request,"admin/saveNoticias.html",{"form":form}) 
            else:
                return redirect('login')
        else:
             return redirect('login')
        
        

def deleteNoticia(request, id):

    if request.method == 'POST':
        try:
            usuario = Noticias.objects.get(id=id)
            usuario.delete()
            return redirect('show_noticias')
        except Noticias.DoesNotExist:
            return HttpResponse("Noticia no encontrada")
    else:
        return HttpResponse("Método no permitido")
    
def editarNoticia(request, id):
    object=get_object_or_404(Noticias, pk=id)
    if request.method == 'GET':
        try:            
            form= NoticiasForm(instance=object)
            return render(request, "admin/editarNoticias.html", {"form":form})
        except Noticias.DoesNotExist:
            return HttpResponse("Noticia no encontrado")
    if request.method == 'POST':
        try:
            form = NoticiasForm(request.POST,instance=object)
            form.save()
            return redirect('show_noticias')
        except Noticias.DoesNotExist:
            return HttpResponse("Noticia no encontrado")
    else:
        return