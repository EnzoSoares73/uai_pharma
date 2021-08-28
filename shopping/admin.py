from django.contrib import admin

from shopping.models import Produto, Tag, Imagem

class ImagesInLine(admin.StackedInline):
    model = Imagem
    extra = 1

class ProdutoAdmin(admin.ModelAdmin):
    campos = ('nome', 'preco', 'promocao', 'em_estoque', 'ativado')
    list_display = campos
    filter_horizontal = ['tags']
    list_filter = ['em_estoque', 'ativado']
    ordering = ['nome']
    inlines = [ImagesInLine]

class TagAdmin(admin.ModelAdmin):
    campos = ('nome', 'prioridade')
    list_display = campos
    ordering = ['nome']

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Tag, TagAdmin)
