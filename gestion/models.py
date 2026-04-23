from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=150)
    correo = models.EmailField(unique=True)
    nacionalidad = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    biografia = models.TextField(blank=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'autor'
        verbose_name_plural = 'autores'

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')

    class Meta:
        ordering = ['titulo']
        verbose_name = 'libro'
        verbose_name_plural = 'libros'

    def __str__(self):
        return self.titulo
