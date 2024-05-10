from django.shortcuts import render, redirect, HttpResponse
from ..models import Noticias
from ..form import NoticiasForm


def showNoticias(request):
    if 'nivel_usuario' in request.session:
        if request.session['nivel_usuario']=='Admin' or request.session['nivel_usuario']=='Escritor':
            response = Noticias.objects.all()
            variable = {}
            variable["request"] = request
            variable["lista"] = response
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
                return redirect('show_noticias')  
            else:
               
                return redirect('login')
        else:
             return redirect('login')
        
        

# def delete_user(request, id):

#     if request.method == 'POST':
#         try:
#             usuario = Usuarios.objects.get(id=id)
#             usuario.delete()
#             return redirect('verusuarios')
#         except Usuarios.DoesNotExist:
#             return HttpResponse("Usuario no encontrado")
#     else:
#         return HttpResponse("Método no permitido")
    
# def editar_user(request, id):
#     if request.method == 'GET':
#         try:
#             usuario = Usuarios.objects.get(id=id)
#             variable = {}
#             variable["usuario"] = usuario
#             return render(request, "admin/editarUsuario.html", variable)
#         except Usuarios.DoesNotExist:
#             return HttpResponse("Usuario no encontrado")
#     if request.method == 'POST':
#         try:
#             usuario = Usuarios.objects.get(id=id)
#             usuario.nombre = request.POST.get('nombre')
#             usuario.usuario = request.POST.get('usuario')
#             usuario.password = request.POST.get('password')
#             usuario.estado = request.POST.get('estado')
#             usuario.nivel = request.POST.get('nivel')
#             usuario.grupo = request.POST.get('grupo')
#             usuario.save()
#             return redirect('verusuarios')
#         except Usuarios.DoesNotExist:
#             return HttpResponse("Usuario no encontrado")
#     else:
#         return