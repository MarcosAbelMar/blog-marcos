from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class BlogPost(models.Model):
    OPCIONES_CATEGORIA = [
        ('Plataforma', 'Plataforma'),
        ('Curso', 'Curso'),
        ('Canal', 'Canal'),
    ]
    titulo = models.CharField(max_length=250, null=False, blank=False, default="Sin titulo")
    categoria = models.CharField(max_length=30, null=False, choices=OPCIONES_CATEGORIA, blank=False, default="Sin categoría")
    fecha = models.DateField(null=True, default='2023-01-01') 
    portada = models.CharField(max_length=250, null=False, blank=False, default="Sin portada")
    lenguaje = models.CharField(max_length=250, null=False, blank=False, default="Sin categoría")
    resumen = models.TextField(max_length=250, null=False, blank=False, default="Sin resumen")
    publicacion = RichTextUploadingField()

    def __str__(self):
        return self.titulo
