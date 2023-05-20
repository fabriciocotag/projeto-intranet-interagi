import logging
import requests

logging.basicConfig()
logger = logging.getLogger("Interagi Listagem")
logger.setLevel(logging.INFO)

BASE_URL="http://localhost:8080/Plone/++api++"

LOGIN = {
    "USUARIO": "admin",
    "SENHA": "admin",
}

session = get_logged_session(LOGIN)

response = session.get(BASE_URL)
data = response.json()
titulo = data["title"]
logger.info(f"O título do portal é {titulo}")

search_url = f"{BASE_URL}/@search?sort_on=path"
response = session.get(BASE_URL)
data = response.json()
total_conteudo = data["items_total"]
logger.info(f"O portal conta com {total_conteudo} itens de conteúdo")



# Funções

def get_logged_session(LOGIN):
    USUARIO = LOGIN["USUARIO"]
    SENHA = LOGIN["SENHA"]
    headers = {
        "Accept": "application/json"
    }
    session = requests.Session()
    session.headers.update(headers)
    login_url = f"{BASE_URL}/@login"
    response = session.post(login_url, json={"login": USUARIO, "password": SENHA})
    if not response.status_code == 200:
        raise ValueError("Usuário ou senha incorretos")
    data = response.json()
    token = data["token"]
    session.headers.update(
        {"Authorization": f"Bearer {token}"}
    )
    return session