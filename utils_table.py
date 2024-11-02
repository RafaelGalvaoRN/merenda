from fasthtml.common import *
from database import base_cardapio
from estilos import *
from datetime import datetime
from utils import formatar_nutricao


# cardapio_itens = base_cardapio()  # Carrega os dados diretamente do banco de dados




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
    # Definir o estilo das linhas, alternando entre pares e ímpares
    row_style = tbody_css + row_even_css

    valor_nutricional = formatar_nutricao(cardapio.exibir_nutricao())

    # Retornar duas linhas: uma para os alimentos, outra para o valor nutricional
    return [
        # Primeira linha com os dados dos alimentos
        Tr(
            # Td(cardapio.id, style=row_style),
            Td(cardapio.escola, style=row_style),
            Td(format_date(cardapio.data), style=row_style),  # Formata a data corretamente

            # Alimentos do Café da Manhã
            Td(cardapio.alimentos_cafe_um, style=row_style),
            Td(cardapio.alimentos_cafe_dois, style=row_style),
            Td(cardapio.alimentos_cafe_tres, style=row_style),
            Td(cardapio.alimentos_cafe_quatro, style=row_style),
            Td(cardapio.alimentos_cafe_cinco, style=row_style),
            Td(cardapio.alimentos_cafe_seis, style=row_style + 'border-right: 1px solid #000'),

            # Alimentos do Almoço
            Td(cardapio.alimentos_almoco_um, style=row_style),
            Td(cardapio.alimentos_almoco_dois, style=row_style),
            Td(cardapio.alimentos_almoco_tres, style=row_style),
            Td(cardapio.alimentos_almoco_quatro, style=row_style),
            Td(cardapio.alimentos_almoco_cinco, style=row_style),
            Td(cardapio.alimentos_almoco_seis, style=row_style + 'border-right: 1px solid #000'),

            # Alimentos do Lanche da Tarde
            Td(cardapio.alimentos_lanche_um, style=row_style),
            Td(cardapio.alimentos_lanche_dois, style=row_style),
            Td(cardapio.alimentos_lanche_tres, style=row_style),
            Td(cardapio.alimentos_lanche_quatro, style=row_style),
            Td(cardapio.alimentos_lanche_cinco, style=row_style),
            Td(cardapio.alimentos_lanche_seis, style=row_style + 'border-right: 1px solid #000'),


        ),

        # Segunda linha com os dados nutricionais (abaixo da linha principal)
        Tr(
            Td("Valor Nutricional", style="font-weight: bold;", colspan="2"),

            Td(
                Div(*valor_nutricional[0], style='padding: 10px;'),  # Exibe valor nutricional do café da manhã
                colspan="6"
            ),
            Td(
                Div(*valor_nutricional[1], style='padding: 10px;'),  # Exibe valor nutricional do almoço
                colspan="6"
            ),
            Td(
                Div(*valor_nutricional[2], style='padding: 10px;'),  # Exibe valor nutricional do lanche da tarde
                colspan="6"
            ),
        )
    ]




def merenda_table(cardapio_items):
    # Verificar se os itens estão chegando corretamente
    if not cardapio_items:
        return Div(
            H2("Nenhum item disponível no cardápio."),
            style=content_css
        )

    # Gerar a tabela apenas se houver dados
    return Table(
        # Cabeçalho das Categorias
        Thead(
            Tr(
                # Th("ID", scope="col", style=th_css, rowspan="2"),
                Th("Escola", scope="col", style=th_css, rowspan="2"),
                Th("Data", scope="col", style=th_css, rowspan="2"),

                # Café da Manhã com borda divisória
                Th("Café da Manhã", scope="col", style=th_titulo_refeicao_css, colspan="6"),

                # Almoço com borda divisória
                Th("Almoço", scope="col", style=th_titulo_refeicao_css, colspan="6"),

                # Lanche da Tarde sem borda, pois é o último
                Th("Lanche da Tarde", scope="col", style=th_titulo_refeicao_css, colspan="6"),
            ),
            Tr(
                # Subcolunas para os alimentos de cada refeição
                Th("Alimento", scope="col", style=th_css_b_left),
                Th("Alimento", scope="col", style=th_css),
                Th("Alimento", scope="col", style=th_css),
                Th("Alimento", scope="col", style=th_css),
                Th("Alimento", scope="col", style=th_css),

                Th("Alimento", scope="col", style={**th_css, 'border-right': '1px solid #000'}),

                Th("Alimento", scope="col", style=th_css),
                Th("Alimento", scope="col", style=th_css),
                Th("Alimento", scope="col", style=th_css),
                Th("Alimento", scope="col", style=th_css),
                Th("Alimento", scope="col", style=th_css),

                Th("Alimento", scope="col", style={**th_css, 'border-right': '1px solid #000'}),

                Th("Alimento", scope="col", style=th_css),
                Th("Alimento", scope="col", style=th_css),
                Th("Alimento", scope="col", style=th_css),
                Th("Alimento", scope="col", style=th_css),
                Th("Alimento", scope="col", style=th_css),

                Th("Alimento", scope="col", style={**th_css, 'border-right': '1px solid #000'}),
            ),
            style=th_css
        ),

        # Corpo da tabela com os dados
        Tbody(
            *[row for index, item in enumerate(cardapio_items) for row in merenda_row(item, index)],
            style="list-style-type: none; text-align: center; padding-left: 0;",
    # Passar o índice da linha
            # Passar o índice da linha
            id="cardapio-list"
        ),
        style=table_css

    )
