import requests

def obter_usuario_aleatorio():
    url = 'https://randomuser.me/api/'

    try:
        responce = requests.get(url)
        responce.raise_for_status()
        dados = responce.json()['results'][0]
        nome = f"{dados['name']['first']}' {dados['name']['last']}"
        email = dados['email']
        pais = dados['location']['country']
        return f"Nome {nome}\n E-mail {email}\nPais {pais}"
    except requests.RequestException:
        return f"Erro ao obter o usuário."


print("Gerando um usúario aleatório...")
usuario = obter_usuario_aleatorio()
print(usuario)
