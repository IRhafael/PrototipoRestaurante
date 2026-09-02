from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cardapio.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# cardapio/urls.py

from django.urls import path

from . import views

app_name = "cardapio"

urlpatterns = [
    path("", views.home, name="home"),
]


# ---------------------------------------------------------------------------
# No urls.py do PROJETO (ex.: recanto/urls.py), inclua este app assim:
#
#   from django.contrib import admin
#   from django.urls import path, include
#   from django.conf import settings
#   from django.conf.urls.static import static
#
#   urlpatterns = [
#       path('admin/', admin.site.urls),
#       path('', include('cardapio.urls')),
#   ]
#
#   if settings.DEBUG:
#       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
# E lembre-se de registrar os modelos no admin.py para o cliente conseguir
# cadastrar categorias e pratos sem precisar mexer no código:
#
#   from django.contrib import admin
#   from .models import Categoria, Prato
#
#   admin.site.register(Categoria)
#   admin.site.register(Prato)
# ---------------------------------------------------------------------------
