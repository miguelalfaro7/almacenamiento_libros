from django.contrib import admin

from .models import Autor, Libro


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'nacionalidad', 'fecha_nacimiento')
    search_fields = ('nombre', 'correo', 'nacionalidad')
    list_filter = ('nacionalidad', 'fecha_nacimiento')


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'isbn', 'fecha_publicacion', 'autor')
    search_fields = ('titulo', 'isbn', 'genero', 'autor__nombre')
    list_filter = ('genero', 'fecha_publicacion', 'autor')
