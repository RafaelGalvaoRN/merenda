from fasthtml.common import *
from estilos import anchor_css, navbar_css, footer_css, logo_mprn


nav_element = Div(

    Img(src="img/logo-mprn.png", style=logo_mprn),
            A("Início", href='/', style=anchor_css),
            A("Cardápio da Escola", href='/merenda', style=anchor_css),
            A("Área do Gestor", href='/gestor', style=anchor_css),
            A("Escolas Participantes", href='/participantes', style=anchor_css),
            A("Contatos", href='/contato', style=anchor_css),
            A("Login", href='/login', style=anchor_css),
            style=navbar_css
        )

pagina_contato = Div(
    Div(
        H1("Contatos", style={
            "text-align": "center",
            "margin-bottom": "90px",
            "color": "#00420c",
            "font-weight": "bold",
            "font-family": "'Roboto', sans-serif",
            "font-size": "60px",
            "border-bottom": "2px solid #005fff",
            "padding-bottom": "10px",
            "display": "inline-block",
        }),
        # Telefone Funcional com Imagem ao lado
        Div(
            Img(src="/img/img_atendimento.png", alt="Imagem Atendimento", style={
                "width": "50px",  # Tamanho ajustável da imagem
                "margin-right": "10px"
            }),
            H2("Telefone Funcional: +55 84 9972-4630", style={
                "font-size": "20px",
                "color": "#00420c",  # Cor solicitada
                "font-family": "'Roboto', sans-serif",  # Fonte solicitada
            }),
            style={
                "display": "flex",  # Alinha imagem e texto lado a lado
                "align-items": "center",  # Centraliza verticalmente
                "justify-content": "center",  # Centraliza horizontalmente
                "margin-bottom": "15px"
            }
        ),
        # E-mail Funcional com Imagem ao lado
        Div(
            Img(src="/img/img_email.png", alt="Imagem Email", style={
                "width": "50px",  # Tamanho ajustável da imagem
                "margin-right": "10px"
            }),
            H2("E-mail Funcional: pmj.canguaretama@mprn.mp.br", style={
                "font-size": "20px",
                "color": "#00420c",  # Cor solicitada
                "font-family": "'Roboto', sans-serif",  # Fonte solicitada
            }),
            style={
                "display": "flex",  # Alinha imagem e texto lado a lado
                "align-items": "center",  # Centraliza verticalmente
                "justify-content": "center",  # Centraliza horizontalmente
                "margin-bottom": "15px"
            }
        ),
        # Endereço com Imagem ao lado
        Div(
            Img(src="/img/img_localizacao.png", alt="Imagem Localização", style={
                "width": "50px",  # Tamanho ajustável da imagem
                "margin-right": "10px"
            }),
            H2("Endereço: Rua Princesa Isabel, nº 190, Centro, Canguaretama/RN. CEP 59.190-000", style={
                "font-size": "20px",
                "color": "#00420c",  # Cor solicitada
                "font-family": "'Roboto', sans-serif",  # Fonte solicitada
            }),
            style={
                "display": "flex",  # Alinha imagem e texto lado a lado
                "align-items": "center",  # Centraliza verticalmente
                "justify-content": "center",  # Centraliza horizontalmente
                "margin-bottom": "15px"
            }
        ),
        # Horário de Atendimento com Imagem ao lado
        Div(
            Img(src="/img/relogio-final.png", alt="Imagem Horário", style={
                "width": "50px",  # Tamanho ajustável da imagem
                "margin-right": "10px"
            }),
            H2("Horário de atendimento: De segunda a quinta-feira, das 08:00 às 17:00, na sexta-feira, das 08:00 às 14:00 horas", style={
                "font-size": "20px",
                "color": "#00420c",  # Cor solicitada
                "font-family": "'Roboto', sans-serif",  # Fonte solicitada
            }),
            style={
                "display": "flex",  # Alinha imagem e texto lado a lado
                "align-items": "center",  # Centraliza verticalmente
                "justify-content": "center",  # Centraliza horizontalmente
                "margin-bottom": "15px"
            }
        ),
        style={
            "width": "80%",
            "margin": "0 auto",
            "padding": "20px",
        }
    ),
    style={
        "display": "flex",
        "justify-content": "center",
        "align-items": "center",
        "height": "100vh",
        "background-color": "#f0f2f5",
        "text-align": "center",
    }
)



footer = Div(
    Div(
        P("""
        PROMOTORIA DE JUSTIÇA DA COMARCA DE CANGUARETAMA        
        """,
        style={
            "text-align": "center",
            "margin-bottom": "5px",
            "color": "white"  # Texto branco
        }),
        P("""
            Rua Princesa Isabel, nº 190, Centro, Canguaretama/RN. CEP 59.190-000.
            Fone: (84) 9 9972-4630. E-mail: pmj.canguaretama@mprn.mp.br
            """,
          style={
              "text-align": "center",
              "margin-bottom": "5px",
              "color": "white"  # Texto branco
          })
        ,
        Div(
            A("Youtube", href='https://www.youtube.com/user/mprnimprensa', style={**anchor_css, "margin-right": "10px"}),
            A("Instagram", href='https://instagram.com/mprn_oficial', style={**anchor_css, "margin-right": "10px"}),
            A("Twitter", href='https://twitter.com/mprn_oficial', style={**anchor_css, "margin-right": "10px"}),
            A("Facebook", href='https://www.facebook.com/mprnoficial/', style=anchor_css),
            style={
                "display": "flex",
                "justify-content": "center",
                "margin-top": "10px"  # Adicione uma margem superior para separar do texto
            }
        ),
        style={
            "width": "100%",
            "display": "flex",
            "flex-direction": "column",  # Organizar em coluna
            "align-items": "center",  # Centralizar os elementos
            "text-align": "center"  # Centralizar o texto
        }
    ),
    style=footer_css
)


def gerar_datalist_para_refeicao(identificador, alimentos_cadastrados, titulo_refeicao):
    """
    Gera um datalist e os campos de input de uma refeição (ex: café da manhã, almoço, lanche) com título.

    :param identificador: Nome único para identificar os campos da refeição (ex: 'cafe', 'almoco', 'lanche').
    :param alimentos_cadastrados: Lista de alimentos cadastrados no sistema para preencher o datalist.
    :param titulo_refeicao: Texto que será exibido acima dos inputs e do datalist.
    :return: Um Div contendo o título, os inputs e o datalist para a refeição.
    """
    print("dentro da func; imprimindo alimentos cadastrados:", alimentos_cadastrados)

    # Criar o datalist com os alimentos cadastrados
    datalist_id = f"datalist_{identificador}"
    datalist = Datalist(*[Option(alimento) for alimento in alimentos_cadastrados], id=datalist_id)

    # Mapear os nomes dos inputs de acordo com o identificador (cafe, almoco, lanche)
    name_mapping = {
        "cafe": ["alimentos_cafe_um", "alimentos_cafe_dois", "alimentos_cafe_tres", "alimentos_cafe_quatro", "alimentos_cafe_cinco", "alimentos_cafe_seis"],
        "almoco": ["alimentos_almoco_um", "alimentos_almoco_dois", "alimentos_almoco_tres", "alimentos_almoco_quatro", "alimentos_almoco_cinco", "alimentos_almoco_seis"],
        "lanche": ["alimentos_lanche_um", "alimentos_lanche_dois", "alimentos_lanche_tres", "alimentos_lanche_quatro", "alimentos_lanche_cinco", "alimentos_lanche_seis"]
    }

    # Gerar os inputs com os names corretos
    inputs = [
        Input(type="text", list=datalist_id, name=name, placeholder=f"Alimento {i + 1}")
        for i, name in enumerate(name_mapping[identificador])
    ]

    # Criar um H1 acima dos inputs
    h1 = H1(titulo_refeicao)

    # Criar um label (título) acima dos inputs
    titulo = Label(titulo_refeicao)

    # Retornar os inputs, datalist e o título organizados lado a lado
    return Div(h1, titulo, Div(*inputs, datalist, style={"display": "flex", "gap": "10px"}))


def select_element(cardapio_itens):

    escolas = {item.get('escola', '') for item in cardapio_itens if item.get('escola')}

    options = [Option(escola, value=escola) for escola in escolas]

    return Label(
        "Selecione a Escola",
        Select(
            *options,
            cls="escola-selector",
            _id="escola-select",
            name="escola",
            **{'@change': "alert('Escola selecionada: ' + this.value);"}
        ),
        _for="escola-select"
    )