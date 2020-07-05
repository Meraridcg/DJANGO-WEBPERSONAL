from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin (admin.ModelAdmin):
#definiendo campos de solo lectura, no se pueden editar
    readonly_fields = ('created', 'updated')


class PostAdmin (admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    #muestra una tabla con las columnas seleccionadas
    list_display = ('title', 'author', 'post_categories')

    #Ordena las columnas de acuerdo a la tupl dada
    ordering = ('author', 'published')

    #Permite hacer una busqueda de acuerdo a los campos dados
    search_fields = ('title',)

    #Permite filtrar por uno o mas campos 
    list_filter = ('author__username', 'categories__name')

    #definir un metodo para crear un campo propio ordena por nombre todas las categorias separadas por comas
    def post_categories(self, obj):
        return (", ".join([c.name for c in obj.categories.all().order_by ("name")]))
    post_categories.short_description= 'CATEGORIAS'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)