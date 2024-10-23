from fasthtml.common import *
from werkzeug.security import generate_password_hash, check_password_hash


db = database('data/controle_cardapio.db')

class controleCardapio:
    id: int;
    escola: str;
    data: str;
    alimentos_cafe: str;
    alimentos_almoco: str;
    alimentos_lanche: str;


    def __ft__(self):
        "`__ft__` defines how FastHTML renders an object"
        return Li("✅ " if self.done else "", self.title)

class User:
    username: str
    pwd: str
    escola: str



base_cardapio = db.create(controleCardapio)
users = db.create(User, pk="username")




def lookuptt_user(username, password):
    try:
        user = users[username]  # Tenta buscar o usuário no banco de dados
    except NotFoundError:
        return False  # Usuário não encontrado, login falha

    # Verifica se a senha fornecida corresponde ao hash armazenado
    return check_password_hash(user.pwd, password)


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

add_user("galvao", "123", "floca")
add_user("andreya", "123", "severiano melo")