from fasthtml.common import *
from textos import conteudo
from estilos import *
from database import base_cardapio, users, lookuptt_user, lookuptt_user_admin, coletar_alimentos_unicos, add_user
from elementos import nav_element, select_element, footer, pagina_contato, gerar_datalist_para_refeicao
from utils_table import create_form, merenda_table, format_date
from datetime import datetime
from templates import template_rota_inicial, template_add_cardapio
from utils import generate_id, get_nav_element, formatar_nutricao
from database import controleCardapio
from tabela_valores_nutricionais import valores_nutricionais_dict
from io import BytesIO
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

import pandas as pd


app, rt = fast_app(live=True, debug=True)
dados_gestor = users()
cardapio_itens = base_cardapio()  # Carrega os dados diretamente do banco de dados



logged_in_user = None  # Variável global para rastrear se o usuário está autenticado
usuario_autenticado = None
admin_logged_in_user = None


@app.route("/gestor", methods=["GET", "POST"])
def add_cardapio(id: int = None, escola: str = None, data: str = None,
                 alimentos_cafe_um: str = None, alimentos_cafe_dois: str = None,
                 alimentos_cafe_tres: str = None, alimentos_cafe_quatro: str = None,
                 alimentos_cafe_cinco: str = None,alimentos_cafe_seis: str = None,
                 alimentos_almoco_um: str = None, alimentos_almoco_dois: str = None,
                 alimentos_almoco_tres: str = None, alimentos_almoco_quatro: str = None,
                 alimentos_almoco_cinco: str = None, alimentos_almoco_seis: str = None,
                 alimentos_lanche_um: str = None, alimentos_lanche_dois: str = None,
                 alimentos_lanche_tres: str = None, alimentos_lanche_quatro: str = None,
                 alimentos_lanche_cinco: str = None, alimentos_lanche_seis: str = None,

                 form_submitted: str = None):



    # Verifica se o usuário está logado
    if not logged_in_user:
        return RedirectResponse(url="/login")  # Redireciona para a página de login se não autenticado


    #pesquisa na base o nome da escola do usuário autenticado
    for usuario in dados_gestor:
        if usuario.username == usuario_autenticado:
            escola_do_gestor = usuario.escola
            break

    if form_submitted == "true" and escola_do_gestor:
        # insere na base
        base_cardapio.insert(
            escola=escola_do_gestor,
            data=data,
            alimentos_cafe_um=alimentos_cafe_um,
            alimentos_cafe_dois=alimentos_cafe_dois,
            alimentos_cafe_tres=alimentos_cafe_tres,
            alimentos_cafe_quatro=alimentos_cafe_quatro,
            alimentos_cafe_cinco=alimentos_cafe_cinco,
            alimentos_cafe_seis=alimentos_cafe_seis,
            alimentos_almoco_um=alimentos_almoco_um,
            alimentos_almoco_dois=alimentos_almoco_dois,
            alimentos_almoco_tres=alimentos_almoco_tres,
            alimentos_almoco_quatro=alimentos_almoco_quatro,
            alimentos_almoco_cinco=alimentos_almoco_cinco,
            alimentos_almoco_seis=alimentos_almoco_seis,
            alimentos_lanche_um=alimentos_lanche_um,
            alimentos_lanche_dois=alimentos_lanche_dois,
            alimentos_lanche_tres=alimentos_lanche_tres,
            alimentos_lanche_quatro=alimentos_lanche_quatro,
            alimentos_lanche_cinco=alimentos_lanche_cinco,
            alimentos_lanche_seis=alimentos_lanche_seis,
        )


    global cardapio_itens
    # Atualiza a lista de cardápios após a inserção
    cardapio_itens = base_cardapio()  # Recarrega os dados do banco de dados




    for item in cardapio_itens:
        # # Aqui você garante que cada item seja convertido para a classe controleCardapio
        # cardapio = controleCardapio(**item.__dict__)  # Transforma o dicionário do item em uma instância da sua classe


        # Agora chamamos o método calcular_nutricao_refeicao da classe controleCardapio
        refeicao = [
            item.alimentos_cafe_um,
            item.alimentos_cafe_dois,
            item.alimentos_cafe_tres,
            item.alimentos_cafe_quatro,
            item.alimentos_cafe_cinco,
            item.alimentos_cafe_seis,

            item.alimentos_almoco_um,
            item.alimentos_almoco_dois,
            item.alimentos_almoco_tres,
            item.alimentos_almoco_quatro,
            item.alimentos_almoco_cinco,
            item.alimentos_almoco_seis,

            item.alimentos_lanche_um,
            item.alimentos_lanche_dois,
            item.alimentos_lanche_tres,
            item.alimentos_lanche_quatro,
            item.alimentos_lanche_cinco,
            item.alimentos_lanche_seis,

        ]

        # Exibe o resultado da função que calcula a nutrição para esta refeição

    table_rows = []

    # Gera a tabela de cardápios já adicionados, se houver itens
    if cardapio_itens:
        try:
            cardapio_item_filtrado = [item for item in cardapio_itens if item.escola == escola_do_gestor ]
        except:
            print("falhei em filtrar cardapio item")
            cardapio_item_filtrado = cardapio_itens




        partes_nutricao = formatar_nutricao(item.exibir_nutricao())

        table_rows = [
            # Primeira linha com os dados dos alimentos
            (Tr(
                Td(item.id, style=th_css_grey),
                Td(item.escola, style=th_css_grey),
                Td(format_date(item.data), style=th_css_grey),
                Td(item.alimentos_cafe_um, style=th_css_left),
                Td(item.alimentos_cafe_dois, style=th_css_grey),
                Td(item.alimentos_cafe_tres, style=th_css_grey),
                Td(item.alimentos_cafe_quatro, style=th_css_grey),
                Td(item.alimentos_cafe_cinco, style=th_css_grey),
                Td(item.alimentos_cafe_seis, style=th_css_right),


                Td(item.alimentos_almoco_um, style=th_css_grey),
                Td(item.alimentos_almoco_dois, style=th_css_grey),
                Td(item.alimentos_almoco_tres, style=th_css_grey),
                Td(item.alimentos_almoco_quatro, style=th_css_grey),
                Td(item.alimentos_almoco_cinco, style=th_css_grey),
                Td(item.alimentos_almoco_seis, style=th_css_b_right),

                Td(item.alimentos_lanche_um, style=th_css_grey),
                Td(item.alimentos_lanche_dois, style=th_css_grey),
                Td(item.alimentos_lanche_tres, style=th_css_grey),
                Td(item.alimentos_lanche_quatro, style=th_css_grey),
                Td(item.alimentos_lanche_cinco, style=th_css_grey),
                Td(item.alimentos_lanche_seis, style=th_css_right),

                Td(
                    Button("Delete",
                           hx_delete=f"/deletar_cardapio_items/{item.id}",
                           hx_confirm="Tem certeza que deseja deletar?",  # Mensagem de confirmação
                           hx_swap="outerHTML",
                           id=f"delete-{item.id}",

                           )
                ,  style=th_css_grey),

            ),

            # Segunda linha com os dados nutricionais (abaixo da linha principal)
            Tr(
                Td("Valor Nutricional", style="font-weight: bold;"),

                Td(colspan="3"),
                Td(
                    Div(*partes_nutricao[0], style='padding: 10px; text-align: center; list-style-type: none;'),  # Exibe partes_nutricao com estilo personalizado
                    colspan="4"  # Usa colspan para ocupar toda a largura da tabela
                ),
                Td(colspan="2"),

                Td(
                    Div(*partes_nutricao[1], style='padding: 10px; text-align: center; list-style-type: none;'),  # Exibe partes_nutricao com estilo personalizado
                    colspan="4"  # Usa colspan para ocupar toda a largura da tabela
                ),
                Td(colspan="2"),

                Td(
                    Div(*partes_nutricao[2], style='padding: 10px; text-align: center; list-style-type: none;'),  # Exibe partes_nutricao com estilo personalizado
                    colspan="4"  # Usa colspan para ocupar toda a largura da tabela
                ),
            ))
        for item in cardapio_item_filtrado  # Loop for
        ]

    #pega o nav de acordo com o usuário logado ou sem estar logado
    nav_element = get_nav_element(logged_in_user)

    #pega nome de alimentos do dic e da base
    alimentos_cadastrados = coletar_alimentos_unicos(cardapio_itens)
    alimentos_valores_nutricionais =[chave for chave in valores_nutricionais_dict]
    alimentos_cadastrados = list(alimentos_cadastrados) + alimentos_valores_nutricionais



    return Div(
        nav_element,
        Div(
            H1("Adicione uma nova Refeição", style=titled_css),


            Form(
                Input(name="escola", type="hidden", value=escola_do_gestor),
                Input(name="form_submitted", type="hidden", value="true"),  # Campo oculto que indica submissão

                H1("Data do Cardápio"),
                Input(name="data", type="date", placeholder="Data da refeição", required=True,
                      style="margin-bottom: 15px; width: 100%; padding: 12px 15px; font-size: 16px;"),
                Div(gerar_datalist_para_refeicao("cafe", alimentos_cadastrados, "Café da Manhã"),
                    gerar_datalist_para_refeicao("almoco", alimentos_cadastrados, "Almoço"),
                    gerar_datalist_para_refeicao("lanche", alimentos_cadastrados, "Lanche da Tarde")),

                Button("Adicionar Refeição", type="submit",
                       style="padding: 12px 20px; border: none; border-radius: 4px; font-size: 16px;"),
                method="post",
                action="/gestor",
                style="display: flex; flex-direction: column; gap: 15px; width: 50%;"
            ),
            style=landing_page_css
        ),

        # Adiciona a tabela após o formulário
        Div(
            H1("Refeições Adicionadas", style=titled_css),
            Table(

                Tr(
                    Th("ID", style=th_css, rowspan="2"),  # Mantém o ID na mesma posição
                    Th("Escola", style=th_css, rowspan="2"),  # Mesma lógica para Escola
                    Th("Data", style=th_css, rowspan="2"),  # Data com rowspan de 2 para alinhar
                    Th("CAFÉ DA MANHÃ", style=th_titulo_refeicao_css, colspan="6"),  # Cabeçalho de Café da Manhã, ocupa 4 colunas
                    Th("ALMOÇO", style=th_titulo_refeicao_css, colspan="6"),  # Cabeçalho de Almoço
                    Th("LANCHE DA TARDE", style=th_titulo_refeicao_css, colspan="6"),  # Cabeçalho de Lanche da Tarde
                    Th("DELETAR", style=th_css, rowspan="2"),  # Cabeçalho de Lanche da Tarde

                ),

                Tr(

                    # Colunas para o Café da Manhã
                    Th("Café da Manhã", style=th_css_b_left),
                    Th("Café da Manhã", style=th_css),
                    Th("Café da Manhã", style=th_css),
                    Th("Café da Manhã", style=th_css),
                    Th("Café da Manhã", style=th_css),
                    Th("Café da Manhã", style=th_css_b_right),

                    # Colunas para o Almoço
                    Th("Almoço", style=th_css),
                    Th("Almoço", style=th_css),
                    Th("Almoço" , style=th_css),
                    Th("Almoço", style=th_css),
                    Th("Almoço", style=th_css),
                    Th("Almoço", style=th_css_b_right),

                    # Colunas para o Lanche da Tarde
                    Th("Lanche da Tarde", style=th_css),
                    Th("Lanche da Tarde", style=th_css),
                    Th("Lanche da Tarde", style=th_css),
                    Th("Lanche da Tarde", style=th_css),
                    Th("Lanche da Tarde", style=th_css),
                    Th("Lanche da Tarde" , style=th_css_b_right),


                ),
                *table_rows,  # Insere as linhas da tabela geradas anteriormente
                style="width: 100%; margin-top: 20px; border-collapse: collapse; border: 1px solid black;"
            ) if table_rows else P("Nenhuma refeição adicionada ainda."),
            style=table_css
        ),

        # Renderiza o footer ao final de tudo
        Div(
            footer,
            style="position: relative; bottom: 0; width: 100%; margin-top: 30px;"
        ),
        style=div_principal
    )


@app.route("/deletar_cardapio_items/{cardapio_id:int}")
def delete(cardapio_id: int):

    # Remove o item da base de dados usando o ID fornecido
    try:

        base_cardapio.delete(cardapio_id)
        global cardapio_itens
        cardapio_itens = base_cardapio()

        print(f"Item com ID {cardapio_id} removido da base.")
    except Exception as e:
        print(f"Falha ao remover o item com ID {cardapio_id}: {e}")


    # Retorna uma resposta vazia, que pode ser atualizada dinamicamente na interface
    return HTMLResponse("<tr></tr>")  # A remoção do <tr> pode ser feita via hx_swap ou JavaScript



@app.route("/deletar_usuario/{usuario:str}")
def delete(usuario: str):

    # Remove o item da base de dados usando o ID fornecido
    try:
        users.delete(usuario)
        global dados_gestor
        dados_gestor = users()

        print(f"Usuário {usuario} removido da base.")
    except Exception as e:
        print(f"Falha ao remover o usuário {usuario}: {e}")


    # Retorna uma resposta vazia, que pode ser atualizada dinamicamente na interface
    return HTMLResponse("<tr></tr>")  # A remoção do <tr> pode ser feita via hx_swap ou JavaScript



# Rota de login simplificada
@app.route("/")
def home():
    nav_element = get_nav_element(logged_in_user)

    return Div(
        nav_element,
        Div(
            H1("Merenda Pública", style=titled_css),
            H2(conteudo, style=h1_css),
            Img(src="/img/merenda.png", style="width: 30%; height: auto; margin: 20px auto; display: block; border-radius: 30px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);"),
            style=landing_page_css
        ),
        footer,
        style=div_principal
    )


@app.route("/contato")
def contato():
    nav_element = get_nav_element(logged_in_user)

    return Div(nav_element, pagina_contato, footer, style=div_principal)


@app.route("/admin_login", methods=["GET", "POST"])
def admin_login(username: str = None, password: str = None):
    global admin_logged_in_user
    global logged_in_user

    nav_element = get_nav_element(logged_in_user)

    if username and password:

        if lookuptt_user_admin(username, password):
            admin_logged_in_user = username  # Usuário autenticado

            return RedirectResponse(url="/admin_painel")


        else:
            return Div(
                nav_element,
                H1("Login", style=h1_login),
                H1("Credenciais Admin Inválidas", style=h1_credencial_invalida),
                Form(
                    Input(name="username", placeholder="Nome de usuário", type="text"),
                    Input(name="password", placeholder="Senha", type="password"),
                    Button("Entrar", type="submit"),
                    method="post",
                    style=form_logout
                ),
                footer,
                style=div_principal
            )

    return Div(
        nav_element,
        H1("Login Admin", style=h1_login),
        Form(
            Input(name="username", placeholder="Nome de usuário", type="text"),
            Input(name="password", placeholder="Senha", type="password"),
            Button("Entrar", type="submit"),
            method="post",
            style=form_logout
        ),
        footer,
        style=div_principal
    )



@app.route("/admin_painel", methods=["GET", "POST"])
def admin_painel(username: str = None, password: str = None,
                 usuario: str = None, escola: str = None,
                 senha:str = None, form_submitted: str = None):


   global dados_gestor

   if not admin_logged_in_user:
       return RedirectResponse(url="/admin_login")  # Redireciona para a página de login se não autenticado


   if form_submitted == "true" and usuario and escola and senha:
       add_user(usuario, senha, escola)
       dados_gestor = users()

       print("USUÁRIO CADASTRADO:", usuario, escola, senha)


   nav_element = get_nav_element(logged_in_user)

   table_rows = [(Tr
                (Td(usuario.username, style=th_css_grey),
                (Td(usuario.escola, style=th_css_grey),
                 Td(
                     Button("Delete",
                            hx_delete=f"/deletar_usuario/{usuario.username}",
                            hx_confirm="Tem certeza que deseja deletar?",  # Mensagem de confirmação
                            hx_swap="outerHTML",
                            id=f"delete-{usuario.username}",

                            )
                     , style=th_css_grey),
                 ))) for usuario in dados_gestor]

   return Div(
       nav_element,
       Div(
           H1("Cadastrar Usuário", style=titled_css),
           Form(
               Input(name="usuario", type="text", placeholder="Usuário", required=True),
               Input(name="escola", type="text", placeholder="Escola", required=True),
               Input(name="senha", type="text", placeholder="Senha", required=True),
               Input(name="form_submitted", type="hidden", value="true"),  # Campo oculto que indica submissão

               Button("Adicionar Usuário", type="submit",
                      style="padding: 12px 20px; border: none; border-radius: 4px; font-size: 16px;"),
               method="post",
               action="/admin_painel",
               style="display: flex; flex-direction: column; gap: 15px; width: 50%;"
           ),
           style=landing_page_css
       ),
       # Adiciona a tabela após o formulário

       Div(
           H1("Usuários na base", style=titled_css_no_margin),
           Table(
               Tr(
                   Th("Nome", style=th_css),
                   Th("Escola", style=th_css),
                   Th("Deletar", style=th_css),
               ),
               *table_rows,
               style="width: 50%;"

           ),
           style=landing_page_css2,
       ),
       footer,
       style=div_principal
   )


@app.route("/login", methods=["GET", "POST"])
def login(username: str = None, password: str = None):
    global logged_in_user
    global usuario_autenticado

    if username and password:
        if lookuptt_user(username, password):
            logged_in_user = username  # Usuário autenticado
            usuario_autenticado = username
            return RedirectResponse(url="/gestor")
        else:
            nav_element = get_nav_element(logged_in_user)

            return Div(
                nav_element,
                H1("Login", style=h1_login),
                H1("Credenciais Inválidas", style=h1_credencial_invalida),
                Form(
                    Input(name="username", placeholder="Nome de usuário", type="text"),
                    Input(name="password", placeholder="Senha", type="password"),
                    Button("Entrar", type="submit"),
                    method="post",
                    style=form_logout
                ),
                footer,
                style=div_principal
            )


    nav_element = get_nav_element(logged_in_user)
    # Página de login simples
    return Div(
        nav_element,
        H1("Login", style=h1_login),
        Form(
            Input(name="username", placeholder="Nome de usuário", type="text"),
            Input(name="password", placeholder="Senha", type="password"),
            Button("Entrar", type="submit"),
            method="post",
            style=form_logout
        ),
        footer,
        style=div_principal
    )


@app.route("/logout")
def logout():
    global logged_in_user  # Declara a variável global
    logged_in_user = None  # Define o valor para None, efetivamente deslogando o usuário
    return RedirectResponse(url="/")  # Redireciona para a página inicial após o logout




@app.route("/painel", methods=["GET", "POST"])
def painel(escola: str = None):
    nav_element = get_nav_element(logged_in_user)
    nota_final = None

    if escola:
        cardapio_filtrado = [item for item in cardapio_itens if item.escola == escola]

        notas_diarias = []

        nutrition_data = []

        for item in cardapio_filtrado:
            date = item.data

            nutrition = item.calcular_nutricao_total_dia()
            nutrition["date"] = date
            nutrition_data.append(nutrition)

            # Avalia o cardápio do dia e armazena a nota
            nota_dia = item.avaliar_cardapio()
            notas_diarias.append(nota_dia)

        if notas_diarias:
            # Calcula a nota final da escola
            nota_final = sum(notas_diarias) / len(notas_diarias)
            nota_final = round(nota_final, 2)
        else:
            nota_final = 0  # Se não houver notas, a nota final é 0


        if nutrition_data:

            df = pd.DataFrame(nutrition_data)
            df['date'] = pd.to_datetime(df['date'])
            df = df.sort_values('date')


            # Cria o gráfico
            plt.figure(figsize=(10, 5))

            # Melhora o estilo das linhas e adiciona suavização
            plt.plot(df['date'], df['calorias'], marker='o', linestyle='-', linewidth=2, label='Calorias', alpha=1)
            plt.plot(df['date'], df['proteinas'], marker='o', linestyle='-', linewidth=2, label='Proteínas', alpha=1)
            plt.plot(df['date'], df['carboidratos'], marker='o', linestyle='-', linewidth=2, label='Carboidratos',
                     alpha=1)
            plt.plot(df['date'], df['gorduras'], marker='o', linestyle='-', linewidth=2, label='Gorduras', alpha=1)

            plt.title(f'Nutrição por Dia da Escola: {escola.upper()}', fontsize=14, fontweight='bold')
            plt.xlabel('Data')
            plt.ylabel('Quantidade (g ou kcal)')

            plt.legend(loc='upper right', frameon=True, shadow=True, fontsize=10, title='Componentes',
                       title_fontsize=11)

            plt.xticks(rotation=45, ha='right')
            plt.gca().xaxis.set_major_formatter(DateFormatter("%d/%m/%Y"))  # Define o formato para dia/mês/ano

            plt.tight_layout()

            # Salva o gráfico em um buffer
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_png = buffer.getvalue()
            buffer.close()
            plt.close()  # Fecha a figura para liberar memória

            # Codifica a imagem em Base64
            graphic = base64.b64encode(image_png).decode('utf-8')

            # Cria o elemento de imagem
            img_element = Img(src="data:image/png;base64,{}".format(graphic), style=img_style)
        else:
            img_element = P("Nenhum dado disponível para esta escola.", style=img_style)
    else:
        img_element = P("Por favor, selecione uma escola para visualizar os dados", style=titled_css)

    if nota_final:
        return Div(
            nav_element,
            Div(
                H1("Painel", style=titled_css),
                Form(
                    Input(
                        type="text",
                        list="escolas",  # Associa o datalist ao input
                        name="escola",  # Certifique-se de que o name seja correto
                        placeholder="Digite ou selecione a escola",
                        style=select_css  # Aqui, 'select_css' pode ser ajustado para um estilo de input mais apropriado
                    ),
                    Datalist(
                        *[Option(escola_item, value=escola_item) for escola_item in
                          {item.escola for item in cardapio_itens}],
                        id="escolas"  # O id deve corresponder ao valor do atributo 'list' no input
                    ),
                    Button("Filtrar", type="submit", style="margin-top: 10px;"),  # Botão de submit tradicional
                    method="post",  # Método POST para enviar os dados
                    style="margin: 20px;"
                ), style=form_container_css),
            H1(f"Nota Nutricional da Escola {escola.upper()}: {nota_final}", style=titled_css),

            img_element,
            footer,
            style=div_principal
        )

    else:
        return Div(
            nav_element,
            Div(
                H1("Painel", style=titled_css),
                Form(
                    Input(
                        type="text",
                        list="escolas",  # Associa o datalist ao input
                        name="escola",  # Certifique-se de que o name seja correto
                        placeholder="Digite ou selecione a escola",
                        style=select_css  # Aqui, 'select_css' pode ser ajustado para um estilo de input mais apropriado
                    ),
                    Datalist(
                        *[Option(escola_item, value=escola_item) for escola_item in
                          {item.escola for item in cardapio_itens}],
                        id="escolas"  # O id deve corresponder ao valor do atributo 'list' no input
                    ),
                    Button("Filtrar", type="submit", style="margin-top: 10px;"),  # Botão de submit tradicional
                    method="post",  # Método POST para enviar os dados
                    style="margin: 20px;"
                ), style=form_container_css),
            img_element,
            footer,
            style=div_principal
        )




@app.route("/participantes")
def participantes():
    # Obter todas as escolas a partir do banco de dados
    escolas = list(set([item.escola for item in cardapio_itens]))

    # Filtrar as escolas para obter a última data e todas as datas de envio para cada escola
    escola_data = {}

    for item in cardapio_itens:
        escola = item.escola
        try:
            data_envio = datetime.strptime(item.data, "%Y-%m-%d") if item.data else None
        except ValueError:
            print("Erro ao processar a data de envio")
            data_envio = None

        # Se a data for válida, adiciona à lista de datas para a escola
        if data_envio:
            if escola not in escola_data:
                escola_data[escola] = []  # Inicializa a lista de datas para a escola nova
            escola_data[escola].append(data_envio)  # Adiciona a data à lista

    # Ordena as datas de envio para cada escola e obtém a última data
    ultima_data_envio = {escola: max(datas) for escola, datas in escola_data.items()}

    # Criar elementos de lista para cada seção

    # Seção 1: Lista de participantes
    participantes_list = [Li(escola.title(), style=li_css) for escola in escolas]

    # Seção 2: Última data de envio por participante
    ultima_data_list = [
        Li(f"{escola.title()}: {data.strftime('%d/%m/%Y')}", style=li_css)
        for escola, data in ultima_data_envio.items()
    ]

    # Seção 3: Todas as datas de envio por participante
    todas_datas_list = [
        Li(f"{escola.title()}: " + ", ".join([data.strftime('%d/%m/%Y') for data in sorted(datas)]), style=li_css)
        for escola, datas in escola_data.items()
    ]

    # Gera o menu de navegação para o usuário logado
    nav_element = get_nav_element(logged_in_user)

    # Renderizar a página com as três seções
    return Div(
        nav_element,
        Div(
            H1("Escolas Participantes", style=titled_css),
            Ul(*participantes_list),  # Seção 1: Lista de participantes

            H2("Última Data de Envio por Escola Participante", style=titled_css),
            Ul(*ultima_data_list),  # Seção 2: Última data de envio

            H2("Todas as Datas de Envio por Escola Participante", style=titled_css),
            Ul(*todas_datas_list),  # Seção 3: Todas as datas de envio

            style=landing_page_css
        ),
        footer,
        style=div_principal
    )

@app.route("/merenda", methods=["GET", "POST"])
def merenda(escola: str = None):

    # Filtrar o cardápio de acordo com a escola selecionada
    if escola:

       cardapio_filtrado = [item for item in cardapio_itens if item.escola == escola]
    else:
        cardapio_filtrado = cardapio_itens

    nav_element = get_nav_element(logged_in_user)
    return Div(
        nav_element,
        Div(
            H1("Cardápio Escolar", style=titled_css),
            Form(
                Input(
                    type="text",
                    list="escolas",  # Associa o datalist ao input
                    name="escola",  # Certifique-se de que o name seja correto
                    placeholder="Digite ou selecione a escola",
                    style=select_css  # Aqui, 'select_css' pode ser ajustado para um estilo de input mais apropriado
                ),
                Datalist(
                    *[Option(escola_item, value=escola_item) for escola_item in
                      {item.escola for item in cardapio_itens}],
                    id="escolas"  # O id deve corresponder ao valor do atributo 'list' no input
                ),
                Button("Filtrar", type="submit", style="margin-top: 10px;"),  # Botão de submit tradicional
                method="post",  # Método POST para enviar os dados
                style="margin: 20px;"
            ), style=form_container_css

        ),
        Div(
            merenda_table(cardapio_filtrado),  # Apenas a tabela será exibida filtrada
            id="tabela_cardapio",  # O ID para referenciar a tabela
            style= table_css
        ),
        footer,
        style=div_principal

    )
    nav_element = get_nav_element(logged_in_user)




serve()
