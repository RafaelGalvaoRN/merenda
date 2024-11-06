
from fasthtml.common import *
from estilos import *



def generate_id(cardapio_items):
    if not cardapio_items:
        return 1  # Começar o ID em 1 se a lista estiver vazia
    else:
        # Criar uma lista de IDs existentes
        existing_ids = [item.id for item in cardapio_items]
        # Gerar o menor ID disponível que não esteja na lista de IDs existentes
        new_id = max(existing_ids) + 1 if existing_ids else 1
        return new_id


def formatar_nutricao(nutricao):

    # Se nutricao for None, retorna uma string indicando que não há dados
    if nutricao is None:
        return "Dados nutricionais indisponíveis."

    # Cria uma lista de Ul com Li e Ol para cada refeição e seus nutrientes, removendo os bullets
    partes = [
        Ul(
            Li(refeicao.upper(), style="list-style-type: none; padding-left: 0; text-align: center; font-weight: bold; "),
            Ol(
                *[Li(f"{nutriente.title()}: {valor}") for nutriente, valor in valores.items()],
                style="list-style-type: none; padding-left: 0; text-align: center;"  # Remove os bullets e o espaçamento padrão
            ),
            style="list-style-type: none; padding-left: 0; text-align: center;"  # Remove os bullets da lista principal
        )
        for refeicao, valores in nutricao.items()
    ]

    return partes




def get_nav_element(logged_in_user):
    if logged_in_user:
        # Se o usuário estiver autenticado, exibe o menu com a opção de logout
        return Div(
            A(
                Img(src="img/logo-mprn.png", style=logo_mprn),
                href='/admin_login',
                style=anchor_css
            ),
            A("Início", href='/', style=anchor_css),
            A("Cardápio da Escola", href='/merenda', style=anchor_css),
            A("Escolas Participantes", href='/participantes', style=anchor_css),
            A("Painel", href='/painel', style=anchor_css),
            A("Contatos", href='/contato', style=anchor_css),
            A("Área do Gestor", href='/gestor', style=anchor_css),
            A("Logout", href='/logout', style=anchor_css),
            style=navbar_css
        )
    else:
        return Div(
            A(
                Img(src="img/logo-mprn.png", style=logo_mprn),
                href='/admin_login',
                style=anchor_css
            ),            A("Início", href='/', style=anchor_css),
            A("Cardápio da Escola", href='/merenda', style=anchor_css),
            A("Escolas Participantes", href='/participantes', style=anchor_css),
            A("Painel", href='/painel', style=anchor_css),
            A("Contatos", href='/contato', style=anchor_css),
            A("Login", href='/login', style=anchor_css),
            style=navbar_css
        )
        # Se o usuário não estiver autenticado, exibe o menu com a opção de login
