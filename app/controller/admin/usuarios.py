from django.shortcuts import render, redirect, HttpResponse
from ...models import Usuarios


def usuarios(request):
    print(request.session['nivel_usuario'])
    if 'nivel_usuario' in request.session:
        if request.session['nivel_usuario']=='Admin':
            response = Usuarios.objects.all()
            variable = {}
            variable["request"] = request
            variable["lista"] = response
            return render(request, "admin/usuarios.html", variable)
        else:
            return redirect('login')
    else:
        return redirect('login')
    

def saveUser(request):
    if request.method=='GET':
        if 'nivel_usuario' in request.session:
            if request.session['nivel_usuario']=='Admin':
                return render(request,"admin/saveUsers.html")
            else:
               
                return render(request,'admin/acceder.html')
        else:
            return redirect(request,'admin/acceder.html')
    
    if request.method=='POST':
        nombre = request.POST.get('nombre')
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        estado = request.POST.get('estado')
        nivel = request.POST.get('nivel')

        Usuarios.objects.create(nombre=nombre,usuario=usuario,password=password,estado=estado,nivel=nivel)
        return redirect('verusuarios')

def delete_user(request, id):

    if request.method == 'POST':
        try:
            usuario = Usuarios.objects.get(id=id)
            usuario.delete()
            return redirect('verusuarios')
        except Usuarios.DoesNotExist:
            return HttpResponse("Usuario no encontrado")
    else:
        return HttpResponse("Método no permitido")
    
def editar_user(request, id):
    if request.method == 'GET':
        try:
            usuario = Usuarios.objects.get(id=id)
            variable = {}
            variable["usuario"] = usuario
            return render(request, "admin/editarUsuario.html", variable)
        except Usuarios.DoesNotExist:
            return HttpResponse("Usuario no encontrado")
    if request.method == 'POST':
        try:
            usuario = Usuarios.objects.get(id=id)
            usuario.nombre = request.POST.get('nombre')
            usuario.usuario = request.POST.get('usuario')
            usuario.password = request.POST.get('password')
            usuario.estado = request.POST.get('estado')
            usuario.nivel = request.POST.get('nivel')
            usuario.grupo = request.POST.get('grupo')
            usuario.save()
            return redirect('verusuarios')
        except Usuarios.DoesNotExist:
            return HttpResponse("Usuario no encontrado")
    else:
        return