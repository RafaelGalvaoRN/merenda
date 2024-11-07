from fasthtml.common import *
from werkzeug.security import generate_password_hash, check_password_hash
from tabela_valores_nutricionais import valores_nutricionais_dict
import os



enviroment = os.getenv('database_enviroment', 'local')

if enviroment == "render":
    db_path = '/opt/render/persistent/controle_cardapio.db'

else:
    db_path = 'data/controle_cardapio.db'


db = database(db_path)



class controleCardapio:
    id: int;
    escola: str;
    data: str;
    alimentos_cafe_um: str;
    alimentos_cafe_dois: str;
    alimentos_cafe_tres: str;
    alimentos_cafe_quatro: str;
    alimentos_cafe_cinco: str;
    alimentos_cafe_seis: str;

    alimentos_almoco_um: str;
    alimentos_almoco_dois: str;
    alimentos_almoco_tres: str;
    alimentos_almoco_quatro: str;
    alimentos_almoco_cinco: str;
    alimentos_almoco_seis: str;

    alimentos_lanche_um: str;
    alimentos_lanche_dois: str;
    alimentos_lanche_tres: str;
    alimentos_lanche_quatro: str;
    alimentos_lanche_cinco: str;
    alimentos_lanche_seis: str;




    def __ft__(self):
        "`__ft__` defines how FastHTML renders an object"
        return Li("✅ " if self.done else "", self.title)

    def calcular_nutricao_refeicao(self, refeicao):

        total_nutricional = {
            "calorias": 0,
            "proteinas": 0,
            "carboidratos": 0,
            "gorduras": 0
        }

        for alimento in refeicao:
            alimento = alimento.strip().lower()  # Normaliza o nome do alimento
            valores = valores_nutricionais_dict.get(alimento)
            if valores:
                total_nutricional["calorias"] += valores["calorias"]
                total_nutricional["proteinas"] += valores["proteinas"]
                total_nutricional["carboidratos"] += valores["carboidratos"]
                total_nutricional["gorduras"] += valores["gorduras"]

        # Arredonda os totais após a soma
        for nutriente in total_nutricional:
            total_nutricional[nutriente] = round(total_nutricional[nutriente], 2)

        return total_nutricional


    def exibir_nutricao(self):
        cafe = [self.alimentos_cafe_um, self.alimentos_cafe_dois,
                self.alimentos_cafe_tres, self.alimentos_cafe_quatro,
                self.alimentos_cafe_cinco,  self.alimentos_cafe_seis
                ]

        cafe_nutricao = self.calcular_nutricao_refeicao(cafe)

        almoco = [self.alimentos_almoco_um, self.alimentos_almoco_dois,
                self.alimentos_almoco_tres, self.alimentos_almoco_quatro,
                  self.alimentos_almoco_quatro, self.alimentos_almoco_cinco]

        almoco_nutricao = self.calcular_nutricao_refeicao(almoco)

        lanche = [self.alimentos_lanche_um, self.alimentos_lanche_dois,
                  self.alimentos_lanche_tres, self.alimentos_lanche_quatro,
                  self.alimentos_lanche_cinco, self.alimentos_lanche_seis]

        lanche_nutricao = self.calcular_nutricao_refeicao(lanche)

        return {
            "Café da Manhã": cafe_nutricao,
            "Almoço": almoco_nutricao,
            "Lanche da Tarde": lanche_nutricao
        }

    def calcular_nutricao_total_dia(self):
        nutricao_por_refeicao = self.exibir_nutricao()
        total_nutricional = {
            "calorias": 0,
            "proteinas": 0,
            "carboidratos": 0,
            "gorduras": 0
        }

        for refeicao_nutricao in nutricao_por_refeicao.values():
            for nutriente in total_nutricional:
                total_nutricional[nutriente] += refeicao_nutricao.get(nutriente, 0)

        # Arredonda os totais após a soma
        for nutriente in total_nutricional:
            total_nutricional[nutriente] = round(total_nutricional[nutriente], 2)

        return total_nutricional

    def avaliar_cardapio(self):
        # Valores nutricionais totais do dia
        total_nutricional = self.calcular_nutricao_total_dia()
        calorias_totais = total_nutricional["calorias"]
        proteinas_totais = total_nutricional["proteinas"]
        carboidratos_totais = total_nutricional["carboidratos"]
        gorduras_totais = total_nutricional["gorduras"]

        # Recomendações nutricionais diárias
        calorias_recomendadas = 2000  # kcal
        faixa_carboidratos = (0.45, 0.65)  # 45-65%
        faixa_proteinas = (0.10, 0.30)  # 10-30%
        faixa_gorduras = (0.25, 0.35)  # 25-35%

        # Converte gramas em calorias
        calorias_proteinas = proteinas_totais * 4
        calorias_carboidratos = carboidratos_totais * 4
        calorias_gorduras = gorduras_totais * 9

        # Calcula o percentual de cada macronutriente
        percentual_proteinas = calorias_proteinas / calorias_totais
        percentual_carboidratos = calorias_carboidratos / calorias_totais
        percentual_gorduras = calorias_gorduras / calorias_totais

        nota = 0
        max_nota = 10

        # Avaliação das calorias totais (até 4 pontos)
        if calorias_totais >= calorias_recomendadas * 0.9 and calorias_totais <= calorias_recomendadas * 1.1:
            nota += 4  # Dentro da faixa ideal
        elif calorias_totais >= calorias_recomendadas * 0.8 and calorias_totais <= calorias_recomendadas * 1.2:
            nota += 2  # Leve desvio
        else:
            nota += 0  # Desvio significativo

        # Avaliação dos macronutrientes (até 6 pontos)
        pontos_macros = 0

        # Proteínas (2 pontos)
        if faixa_proteinas[0] <= percentual_proteinas <= faixa_proteinas[1]:
            pontos_macros += 2
        elif (faixa_proteinas[0] - 0.05) <= percentual_proteinas <= (faixa_proteinas[1] + 0.05):
            pontos_macros += 1

        # Carboidratos (2 pontos)
        if faixa_carboidratos[0] <= percentual_carboidratos <= faixa_carboidratos[1]:
            pontos_macros += 2
        elif (faixa_carboidratos[0] - 0.05) <= percentual_carboidratos <= (faixa_carboidratos[1] + 0.05):
            pontos_macros += 1

        # Gorduras (2 pontos)
        if faixa_gorduras[0] <= percentual_gorduras <= faixa_gorduras[1]:
            pontos_macros += 2
        elif (faixa_gorduras[0] - 0.05) <= percentual_gorduras <= (faixa_gorduras[1] + 0.05):
            pontos_macros += 1

        nota += pontos_macros

        # Arredonda a nota final
        nota_final = round(nota, 1)
        return nota_final



class User:
    username: str
    pwd: str
    escola: str


class ValorNutricional:
    id: int = None  # Agora aceita um campo `id`
    alimento: str;
    calorias: float;
    proteinas: float;
    carboidratos: float;
    gorduras: float;







def lookuptt_user(username, password):
    try:
        user = users[username]  # Tenta buscar o usuário no banco de dados
    except NotFoundError:
        return False  # Usuário não encontrado, login falha

    # Verifica se a senha fornecida corresponde ao hash armazenado
    return check_password_hash(user.pwd, password)

def lookuptt_user_admin(username, password):

    if username == "rafael":
        try:
            user = users[username]  # Tenta buscar o usuário no banco de dados
        except NotFoundError:
            return False  # Usuário não encontrado, login falha

        # Verifica se a senha fornecida corresponde ao hash armazenado
        return check_password_hash(user.pwd, password)

    return False  # Usuário não corresponde ao admin, login falha


# Verifica se o usuário já existe no banco de dados
def user_exists(username):
    try:
        user = users[username]
        return True
    except NotFoundError:
        return False


# Função para adicionar um usuário ao banco de dados
# Função para adicionar um usuário ao banco de dados
def add_user(username, password, escola):
    if not user_exists(username):
        hashed_pwd = generate_password_hash(password)  # Cria o hash da senha
        print(f"Inserindo usuário com escola: {escola}")  # Verifica o valor de escola

        try:
            # Tenta inserir o usuário
            users.insert(username=username, pwd=hashed_pwd, escola=escola)
            print(f"Usuário '{username}' adicionado com sucesso!")
        except Exception as e:
            print(f"Erro ao adicionar o usuário '{username}': {e}")
    else:
        print(f"Usuário '{username}' já existe no banco de dados.")


def coletar_alimentos_unicos(cardapio_itens):
    alimentos_unicos = set()  # Usar um set para garantir que não haja duplicações

    # Iterar sobre cada item da lista (cada instância de controleCardapio)
    for item in cardapio_itens:
        # Adicionar todos os alimentos do café, almoço e lanche ao set
        alimentos_unicos.update([
            item.alimentos_cafe_um, item.alimentos_cafe_dois, item.alimentos_cafe_tres, item.alimentos_cafe_quatro,
            item.alimentos_cafe_cinco, item.alimentos_cafe_seis,
            item.alimentos_almoco_um, item.alimentos_almoco_dois, item.alimentos_almoco_tres,
            item.alimentos_almoco_quatro, item.alimentos_almoco_cinco, item.alimentos_almoco_seis,
            item.alimentos_lanche_um, item.alimentos_lanche_dois, item.alimentos_lanche_tres,
            item.alimentos_lanche_quatro, item.alimentos_lanche_cinco, item.alimentos_lanche_seis
        ])

    # Remover valores vazios (caso haja alimentos não preenchidos)
    alimentos_unicos = {alimento for alimento in alimentos_unicos if alimento}

    return alimentos_unicos


# Garante que as tabelas existam ou sejam criadas se não existirem
base_cardapio = db.create(controleCardapio, if_not_exists=True)
users = db.create(User, pk="username", if_not_exists=True)
gasto_nutricional = db.create(ValorNutricional, if_not_exists=True)



for alimento, valores in valores_nutricionais_dict.items():
    gasto_nutricional.insert({
        "alimento": alimento,
        "calorias": valores['calorias'],
        "proteinas": valores['proteinas'],
        "carboidratos": valores['carboidratos'],
        "gorduras": valores['gorduras']
    }, pk="alimento")

