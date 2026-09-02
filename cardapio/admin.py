from django.contrib import admin
from cardapio.models import Categoria, Prato


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)


@admin.register(Prato)
class PratoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nome', 'descricao')