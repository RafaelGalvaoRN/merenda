from fasthtml.common import *
from elementos import footer, nav_element, pagina_contato
from estilos import *
from textos import conteudo


template_rota_inicial = Div(
        nav_element,
        Div(
            H1("Merenda Legal", style=titled_css),
            H2(conteudo, style=h1_css),
            style=landing_page_css
        ),
        footer,
        style=div_principal
    )


# template_contato = Div(nav_element, pagina_contato, footer, style=div_principal)


template_add_cardapio = Div(
        nav_element,
        Div(
            H1("Adicione uma nova Refeição", style=titled_css),
            Form(
                Input(name="escola", placeholder="Escola", type="text", required=False, style="margin-bottom: 15px; width: 100%; padding: 12px 15px; font-size: 16px;"),  # Aumentando o espaço do input

                Input(name="data", type="date", placeholder="Data da refeição", required=False, style="margin-bottom: 15px; width: 100%; padding: 12px 15px; font-size: 16px;"),  # Date picker

                H2("Café da manhã"),
                Input(name="alimentos_cafe", placeholder="Alimentos Matutino", type="text", required=False, style="margin-bottom: 15px; width: 100%; padding: 12px 15px; font-size: 16px;"),  # Input maior

                H2("Almoço"),
                Input(name="alimentos_almoco", placeholder="Alimentos do Almoço", type="text", required=False,
                      style="margin-bottom: 15px; width: 100%; padding: 12px 15px; font-size: 16px;"),  # Input maior

                H2("Lanche da Tarde"),
                Input(name="alimentos_lanche", placeholder="Alimentos Vespertino", type="text", required=False,
                      style="margin-bottom: 15px; width: 100%; padding: 12px 15px; font-size: 16px;"),  # Input maior

                Button("Adicionar Refeição", type="submit", style="padding: 12px 20px; border: none; border-radius: 4px; font-size: 16px;"),
                method="post",
                action="/adicionar_merenda",
                style="display: flex; flex-direction: column; gap: 15px; width: 50%;"  # Flexbox para espaçamento adequado
            ),
            footer,
            style=div_principal
        )
    )