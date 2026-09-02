# cardapio/models.py
#
# App sugerida: "cardapio"
# Lembre-se de rodar, após criar/editar estes modelos:
#   python manage.py makemigrations cardapio
#   python manage.py migrate
#
# Requisitos:
#   pip install Pillow   -> necessário para o campo ImageField funcionar

from django.db import models


class Categoria(models.Model):
    """Agrupa os pratos no cardápio (ex.: Entradas, Pratos Principais,
    Sobremesas, Bebidas)."""

    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Prato(models.Model):
    """Cada item vendável do cardápio."""

    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    # As imagens reais dos pratos (enviadas pelo cliente) devem ser
    # cadastradas pelo admin do Django e serão salvas em MEDIA_ROOT/pratos/.
    # Configure no settings.py:
    #   MEDIA_URL = '/media/'
    #   MEDIA_ROOT = BASE_DIR / 'media'
    # E, no urls.py do projeto (apenas em desenvolvimento), sirva a media:
    #   from django.conf import settings
    #   from django.conf.urls.static import static
    #   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    imagem = models.ImageField(upload_to="pratos/", blank=True, null=True)

    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="pratos"
    )
    disponivel = models.BooleanField(
        default=True,
        help_text="Desmarque para ocultar o prato do site sem precisar apagá-lo.",
    )

    class Meta:
        verbose_name = "Prato"
        verbose_name_plural = "Pratos"
        ordering = ["categoria__nome", "nome"]

    def __str__(self):
        return f"{self.nome} ({self.categoria.nome})"
