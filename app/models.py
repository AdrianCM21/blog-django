from django.db import models


class Grupos(models.Model):
    grupo = models.CharField(max_length=50)

    def __str__(self):
        return self.grupo


class Usuarios(models.Model):
    nombre = models.CharField(max_length=250)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    nivel = models.CharField(max_length=50)
    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.nombre


class Noticias(models.Model):
    titulo = models.CharField(max_length=250)
    fecha = models.DateField(auto_now=True)
    contenido = models.CharField(max_length=3000)
    imagen = models.ImageField(upload_to='imagenes',null=True)
    grupo = models.ForeignKey(Grupos, on_delete=models.RESTRICT, null=True)
    autor = models.ForeignKey(Usuarios, on_delete=models.RESTRICT)

    def __str__(self):
        return self.titulo


class Comentarios(models.Model):
    noticia = models.ForeignKey(Noticias, on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=250)
    comentario = models.CharField(max_length=3000)
    fecha = models.DateField(auto_now=True)
    visible = models.BooleanField()

    def __str__(self):
        return self.nombre
