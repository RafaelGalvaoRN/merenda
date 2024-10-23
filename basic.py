from fasthtml.common import *
from textos import conteudo
from estilos import *
from database import base_cardapio, users, lookuptt_user
from elementos import nav_element, select_element, footer, pagina_contato
from utils_table import create_form, merenda_table, format_date
from datetime import datetime
from templates import template_rota_inicial, template_add_cardapio
from utils import generate_id, get_nav_element


app, rt = fast_app(live=True, debug=True)
dados_gestor = users()
cardapio_itens = base_cardapio()  # Carrega os dados diretamente do banco de dados

logged_in_user = None  # Variável global para rastrear se o usuário está autenticado
usuario_autenticado = None


@app.route("/gestor", methods=["GET", "POST"])
def add_cardapio(id:int = None, escola: str = None, data: str = None, alimentos_cafe: str = None, alimentos_almoco: str = None,
                 alimentos_lanche: str = None, form_submitted: str = None):

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
        base_cardapio.insert(escola=escola_do_gestor, data=data, alimentos_cafe=alimentos_cafe,
                              alimentos_almoco=alimentos_almoco, alimentos_lanche=alimentos_lanche)

    global cardapio_itens
    # Atualiza a lista de cardápios após a inserção
    cardapio_itens = base_cardapio()  # Recarrega os dados do banco de dados

    # Gera a tabela de cardápios já adicionados, se houver itens
    if cardapio_itens:
        try:
            cardapio_item_filtrado = [item for item in cardapio_itens if item.escola == escola_do_gestor ]
        except:
            print("falhei em filtrar cardapio item")
            cardapio_item_filtrado = cardapio_itens


        table_rows = [
            Tr(
                Td(item.id),
                Td(item.escola),
                Td(format_date(item.data)),
                Td(item.alimentos_cafe),
                Td(item.alimentos_almoco),
                Td(item.alimentos_lanche),
                Td(
                    Button("Delete",
                           hx_delete=f"/deletar_cardapio_items/{item.id}",
                           hx_confirm="Tem certeza que deseja deletar?",  # Mensagem de confirmação
                           hx_swap="outerHTML",
                           id=f"delete-{item.id}"  # ID único para cada botão de delete
                           ),
                ),

            ) for item in cardapio_item_filtrado
        ]

    #pega o nav de acordo com o usuário logado ou sem estar logado
    nav_element = get_nav_element(logged_in_user)


    return Div(
        nav_element,
        Div(
            H1("Adicione uma nova Refeição", style=titled_css),


            Form(
                Input(name="escola", type="hidden", value=escola_do_gestor),
                Input(name="form_submitted", type="hidden", value="true"),  # Campo oculto que indica submissão

                H2("Data do Cardápio"),
                Input(name="data", type="date", placeholder="Data da refeição", required=False,
                      style="margin-bottom: 15px; width: 100%; padding: 12px 15px; font-size: 16px;"),
                H2("Café da Manhã"),
                Input(name="alimentos_cafe", placeholder="Alimentos Matutino", type="text", required=False,
                      style="margin-bottom: 15px; width: 100%; padding: 12px 15px; font-size: 16px;"),
                H2("Almoço"),
                Input(name="alimentos_almoco", placeholder="Alimentos do Almoço", type="text", required=False,
                      style="margin-bottom: 15px; width: 100%; padding: 12px 15px; font-size: 16px;"),
                H2("Lanche da Tarde"),
                Input(name="alimentos_lanche", placeholder="Alimentos Vespertino", type="text", required=False,
                      style="margin-bottom: 15px; width: 100%; padding: 12px 15px; font-size: 16px;"),
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
                    Th("ID", style=th_css),
                    Th("Escola", style=th_css),
                    Th("Data", style=th_css),
                    Th("Café da Manhã", style=th_css),
                    Th("Almoço", style=th_css),
                    Th("Lanche da Tarde", style=th_css),
                    Th("Deletar", style=th_css)
                ),
                *table_rows,  # Insere as linhas da tabela
                style="width: 100%; margin-top: 20px; border-collapse: collapse; border: 1px solid black;"
            ) if table_rows else P("Nenhuma refeição adicionada ainda."),
            style= table_css
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


@app.route("/participantes")
def participantes():
    # Obter todas as escolas a partir do banco de dados
    escolas = list(set([item.escola for item in cardapio_itens]))

    # Filtrar as escolas e pegar a última data de envio para cada escola
    escola_data = {}

    for item in cardapio_itens:
        escola = item.escola
        try:
            # Tenta transformar a data do cardápio em um objeto datetime
            data_envio = datetime.strptime(item.data, "%Y-%m-%d") if item.data else None
        except ValueError:
            print("Erro ao processar a data de envio")
            data_envio = None

        # Se a data for válida, atualiza a última data registrada por escola
        if data_envio:
            if escola not in escola_data or data_envio > escola_data[escola]:
                escola_data[escola] = data_envio

    # Cria a lista de status de envio, com a última data registrada para cada escola
    status_envio = [Li(f"{escola.title()}: {data.strftime('%d/%m/%Y')}", style=li_css) for escola, data in escola_data.items()]

    # Gera o menu de navegação para o usuário logado
    nav_element = get_nav_element(logged_in_user)

    return Div(
        nav_element,
        Div(
            H1("Participantes", style=titled_css),
            Ul(
                *[Li(escola.title(), style=li_css) for escola in escolas]),  # Cria um Li para cada escola

            H2("Status de Envio", style=titled_css),
            Ul(
                # Exibir o nome da escola e a última data de envio
                *status_envio,
            ),
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
