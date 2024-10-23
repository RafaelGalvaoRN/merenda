from fasthtml.common import *
from database import base_cardapio
from estilos import *
from datetime import datetime



Cardapio = base_cardapio.dataclass()



def format_date(date_str):
    try:
        # Tenta converter a data de 'YYYY-MM-DD' para 'DD/MM/YYYY'
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%d/%m/%Y')
    except (ValueError, TypeError):
        # Retorna 'N/A' caso a data seja inválida ou não exista
        return 'N/A'


def create_form():
    return Form(id="create-form", hx_post="/", hx_target="#client-list", hx_swap="beforeend")




def merenda_row(cardapio, index):
    row_style = tbody_css + (row_even_css if index % 2 == 0 else "")

    return Tr(
        Td(cardapio.id, style=row_style),
        Td(cardapio.escola, style=row_style),
        Td(format_date(cardapio.data), style=row_style),  # Formata a data corretamente
        Td(cardapio.alimentos_cafe, style=row_style),
        Td(cardapio.alimentos_almoco, style=row_style),
        Td(cardapio.alimentos_lanche, style=row_style),

        id=f"client-{cardapio.id}"
    )

def merenda_table(cardapio_items):
    # Verificar se os itens estão chegando corretamente

    if not cardapio_items:
        return Div(
            H2("Nenhum item disponível no cardápio."),
            style=content_css
        )

    # Gerar a tabela apenas se houver dados
    return Table(
        Thead(
            Tr(
                Th("ID", scope="col", style=th_css),
                Th("Escola", scope="col", style=th_css),
                Th("Data", scope="col", style=th_css),
                Th("Lanche Matutino", scope="col", style=th_css),
                Th("Almoço", scope="col", style=th_css),
                Th("Lanche Vespertino", scope="col", style=th_css),

            ),
            style=th_css
        ),
        Tbody(
            *[merenda_row(item, index) for index, item in enumerate(cardapio_items)],  # Passar o índice da linha
            id="cardapio-list"
        ),
        style=table_css
    )