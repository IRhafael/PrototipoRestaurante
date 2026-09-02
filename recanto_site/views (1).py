# cardapio/views.py

from django.shortcuts import render

from .models import Categoria


def home(request):
    """Renderiza a página institucional/cardápio.

    Monta uma lista de grupos no formato:
        [
            {"categoria": <Categoria>, "pratos": <QuerySet[Prato]>},
            ...
        ]
    contendo apenas categorias que tenham ao menos um prato disponível,
    e dentro delas apenas os pratos marcados como disponível=True.
    """
    categorias = Categoria.objects.prefetch_related("pratos").all()

    cardapio = []
    for categoria in categorias:
        pratos_disponiveis = categoria.pratos.filter(disponivel=True)
        if pratos_disponiveis.exists():
            cardapio.append(
                {
                    "categoria": categoria,
                    "pratos": pratos_disponiveis,
                }
            )

    contexto = {
        "cardapio": cardapio,
        # TODO: troque pelo número real de WhatsApp do restaurante,
        # no formato internacional sem espaços/símbolos (DDI+DDD+número).
        "whatsapp_numero": "5589900000000",
    }
    return render(request, "cardapio/index.html", contexto)
