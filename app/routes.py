from django.urls import path

from .controller.admin import noticiasController, usuarios, administrador as admin,gruposController,comentarioController
from .controller import inicio

urlpatterns = [
    path("", inicio.inicio, name="inicio"),
    path("publicacion/<int:id>", inicio.show_publicacion, name="show_publicacion"),
    path("publicacion_comentar",comentarioController.addComentarios,name="add_comentario"),

    # admin
    path("administrador/usuarios", usuarios.usuarios, name="verusuarios"),
    path("administrador/usuarios/add", usuarios.saveUser, name="addusuarios"),
    path("administrador/usuarios/edit/<int:id>", usuarios.editar_user, name="editarusuarios"),
    path("administrador/usuario/delete/<int:id>/", usuarios.delete_user, name="delete_user"),
    path("administrador/usuario/editar/<int:id>/", usuarios.editar_user, name="editar_user"),
    path('login', admin.acceder, name='login'),
    path("administrador/noticias",noticiasController.showNoticias, name='show_noticias'),
    path("administrador/noticias/add",noticiasController.addNoticias, name='add_noticias'),
    path("administrador/noticias/delete/<int:id>", noticiasController.deleteNoticia, name="delete_noticias"),
    path("administrador/noticias/editar/<int:id>", noticiasController.editarNoticia, name="editar_noticias"),
    path("administrador/grupos",gruposController.showGrupos, name='show_grupos'),
    path("administrador/grupos/add",gruposController.addGrupos, name='add_grupos'),
    path("administrador/grupos/delete/<int:id>/", gruposController.deleteGrupos, name="delete_grupos"),
    path("administrador/comentarios",comentarioController.showComentarios, name='show_comentarios'),
    # path("administrador/comentarios/add",gruposController.addGrupos, name='add_grupos'),
    # path('logout', admin.salir, name='logout'),
]
