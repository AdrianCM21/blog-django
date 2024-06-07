from django.shortcuts import render, redirect
from ...models import Usuarios


def acceder(request):
    if request.method=='GET':
        if 'codigo_usuario' in request.session:
            variables={}
            if request.session['nivel_usuario']=='Usuario':
                variables['nombre_usuario']= request.session['nombre_usuario']
                return render(request,'home/inicio.html', variables)
            else:
                
                variables['nombre_usuario']= request.session['nombre_usuario']
                return render(request,'admin/inicioAdmin.html', variables)
        else:
            
            return render(request,'admin/acceder.html')
    
    if request.method=='POST':
        v_usuario=request.POST.get('usuario')
        v_clave=request.POST.get('password')
        verificar_usuario=Usuarios.objects.filter(usuario=v_usuario, estado='Activo')
        variables={}
        if verificar_usuario.count()>0:
            if verificar_usuario[0].password==v_clave:
                request.session['codigo_usuario']=verificar_usuario[0].id
                request.session['nombre_usuario']=verificar_usuario[0].nombre
                request.session['nivel_usuario']=verificar_usuario[0].nivel
                variables['nombre_usuario']= request.session['nombre_usuario']
                if request.session['nivel_usuario']=='Usuario':
                     return render(request,'home/inicio.html', variables)
                else:
                    
                    return render(request,'admin/usuarios.html', variables)
            else:
                variables['m_error']='La contraseña es incorrecta'
                return render (request, 'admin/acceder.html', variables)
        else:
            variables['m_error']='El usuario no esta registrado'
            return render (request, 'admin/acceder.html', variables)

def salir(request):

    del request.session['codigo_usuario']
    del request.session['nombre_usuario']
    del request.session['nivel_usuario'] 
    return render(request,'admin/acceder.html')