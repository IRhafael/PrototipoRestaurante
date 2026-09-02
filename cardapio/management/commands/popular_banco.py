from django.core.management.base import BaseCommand
from cardapio.models import Categoria, Prato
from decimal import Decimal
# python manage.py popular_banco

class Command(BaseCommand):
    help = 'Popula o banco de dados com categorias e pratos de teste para o MVP.'

    def handle(self, *args, **kwargs):
        # Dicionário com a carga de dados
        dados_iniciais = {
            "Entradas & Caldos": [
                {"nome": "Caldo de Feijão Manteiga", "descricao": "Caldo grosso acompanhado de torresmo e torradas de alho.", "preco": "18.90"},
                {"nome": "Dadinhos de Tapioca", "descricao": "Porção de dadinhos fritos de tapioca com queijo coalho, acompanha geleia de pimenta.", "preco": "24.50"},
                {"nome": "Queijo Coalho Assado", "descricao": "Fatias de queijo coalho na brasa com melaço de cana.", "preco": "22.00"},
            ],
            "Pratos Principais": [
                {"nome": "Carne de Sol do Sertão", "descricao": "Carne de sol artesanal acebolada, acompanha macaxeira frita, feijão tropeiro e arroz branco.", "preco": "65.00"},
                {"nome": "Bode Guisado", "descricao": "Tradicional bode guisado com temperos da casa, servido com pirão, arroz e salada.", "preco": "58.90"},
                {"nome": "Galinha Caipira", "descricao": "Porção bem servida de galinha caipira ao molho, com arroz, fava e farofa na manteiga de garrafa.", "preco": "72.00"},
            ],
            "Bebidas": [
                {"nome": "Suco Natural de Caju", "descricao": "Jarra de 1 litro de suco natural da fruta.", "preco": "15.00"},
                {"nome": "Cerveja Pilsen 600ml", "descricao": "Bem gelada, diversas marcas.", "preco": "12.50"},
                {"nome": "Refrigerante Lata", "descricao": "Coca-Cola, Guaraná, etc.", "preco": "6.00"},
            ],
            "Sobremesas": [
                {"nome": "Cartola Piauiense", "descricao": "Banana assada, queijo manteiga derretido, açúcar e canela.", "preco": "18.00"},
                {"nome": "Doce de Leite com Queijo", "descricao": "Doce de leite em pedaços servido com fatias de queijo coalho fresco.", "preco": "14.50"},
            ]
        }

        self.stdout.write("Iniciando a carga de dados...")

        # Limpando dados antigos para evitar duplicidade durante os testes
        Prato.objects.all().delete()
        Categoria.objects.all().delete()

        for nome_categoria, pratos in dados_iniciais.items():
            # Cria a categoria
            categoria, created = Categoria.objects.get_or_create(nome=nome_categoria)
            
            # Prepara a lista de objetos Prato para bulk_create
            pratos_objs = []
            for p in pratos:
                pratos_objs.append(
                    Prato(
                        categoria=categoria,
                        nome=p["nome"],
                        descricao=p["descricao"],
                        preco=Decimal(p["preco"]),
                        disponivel=True
                    )
                )
            
            # Insere os pratos da categoria de uma vez
            Prato.objects.bulk_create(pratos_objs)
            
            self.stdout.write(self.style.SUCCESS(f'Categoria "{nome_categoria}" e {len(pratos)} pratos inseridos.'))

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))