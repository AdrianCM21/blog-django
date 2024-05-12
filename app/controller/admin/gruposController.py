from django.shortcuts import render, redirect, HttpResponse
from ...models import Grupos


def showGrupos(request):
    print(request.session['nivel_usuario'])
    if 'nivel_usuario' in request.session:
        if request.session['nivel_usuario']=='Admin':
            response = Grupos.objects.all()
            variable = {}
            variable["request"] = request
            variable["lista"] = response
            return render(request, "admin/grupos.html", variable)
        else:
            return redirect('login')
    else:
        return redirect('login')
    

def addGrupos(request):
    if request.method=='GET':
        if 'nivel_usuario' in request.session:
            if request.session['nivel_usuario']=='Admin':
                return render(request,"admin/saveGrupos.html")
            else:
               
                return render(request,'admin/acceder.html')
        else:
            return redirect(request,'admin/acceder.html')
    
    if request.method=='POST':
        nombre = request.POST.get('grupo')

        Grupos.objects.create(grupo=nombre)
        return redirect('show_grupos')

def deleteGrupos(request, id):

    if request.method == 'POST':
        try:
            usuario = Grupos.objects.get(id=id)
            usuario.delete()
            return redirect('show_grupos')
        except Grupos.DoesNotExist:
            return HttpResponse("Usuario no encontrado")
    else:
        return HttpResponse("Método no permitido")
