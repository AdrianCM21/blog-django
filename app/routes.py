from django.urls import path
from .controller import inicio, usuarios, administrador as admin,noticiasController,gruposController

urlpatterns = [
    path("", inicio.inicio, name="inicio"),
    path("usuarios", usuarios.usuarios, name="verusuarios"),
    path("usuarios/add", usuarios.saveUser, name="addusuarios"),
    path("usuarios/edit/<int:id>", usuarios.editar_user, name="editarusuarios"),
    path("usuario/delete/<int:id>/", usuarios.delete_user, name="delete_user"),
    path("usuario/editar/<int:id>/", usuarios.editar_user, name="editar_user"),
    path('login', admin.acceder, name='login'),

    path("noticias",noticiasController.showNoticias, name='show_noticias'),
    path("noticias/add",noticiasController.addNoticias, name='add_noticias'),
    path("grupos",gruposController.showGrupos, name='show_grupos'),
    path("grupos/add",gruposController.addGrupos, name='add_grupos'),
    path("grupos/delete/<int:id>/", gruposController.deleteGrupos, name="delete_grupos"),
    # path('logout', admin.salir, name='logout'),
]
